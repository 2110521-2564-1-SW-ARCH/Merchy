import pika
import json

HOST = "localhost"


def produce(queue, msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue=queue, exclusive=False)
    channel.basic_publish(exchange="", routing_key="request", body=json.dumps(msg))
    connection.close()


class Consumer:
    def __init__(self, *args, **kwargs):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.conn.channel()

    def consume(self, queue, callback):
        self.channel.queue_declare(queue)
        self.channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True
        )
        self.channel.start_consuming()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('haha')
        self.channel.close()
        self.conn.close()


def consume(queue, cb):

    with Consumer() as consumer:
        consumer.consume(queue=queue, callback=cb)
        print("here")
