import pika
import json
import os

HOST = os.getenv("RABBIT_MQ_IP")
PRODUCING_QUEUE = "request"
CONSUMING_QUEUE = "response"

producing_connection = pika.BlockingConnection(pika.URLParameters(HOST))
producing_channel = producing_connection.channel()
producing_channel.queue_declare(queue=PRODUCING_QUEUE, exclusive=False)


def produce(msg):
    producing_channel.basic_publish(exchange="", routing_key=PRODUCING_QUEUE, body=json.dumps(msg))


def consume(cb):
    consuming_connection = pika.BlockingConnection(pika.URLParameters(HOST))
    consuming_channel = consuming_connection.channel()
    consuming_channel.queue_declare(queue=CONSUMING_QUEUE)
    consuming_channel.basic_consume(queue=CONSUMING_QUEUE, on_message_callback=cb, auto_ack=True)
    consuming_channel.start_consuming()