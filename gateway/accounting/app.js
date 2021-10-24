const amqp = require('amqplib/callback_api');
const express = require('express')
const app = express()

PORT = 3000

function consumeHandler(msg){
    msg = JSON.parse(msg.content.toString())
    console.log(`[x] App Received ${msg}`)
}

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var queue = 'response';

        channel.assertQueue(queue, {
            durable: false
        });

        console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);

        channel.consume(queue, consumeHandler, {
            noAck: true
        });

    });
});

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
    let msg = req.query.msg
    sendMessage(msg)
    res.send("eiei")
})

app.listen(PORT, () => console.log(`RabbitMQ client running at ${PORT}`))

function sendMessage(msg) {
    amqp.connect('amqp://localhost', function (error0, connection) {
        if (error0) {
            throw error0;
        }
        connection.createConfirmChannel(function (error1, channel) {
            if (error1) {
                throw error1;
            }
            var queue = 'request';

            channel.assertQueue(queue, {
                durable: false
            });

            channel.sendToQueue(queue, Buffer.from(JSON.stringify(msg)), { persistent: false }, function (err) {
                if (err !== null) console.log("Message NACKED")
                channel.close()
                connection.close()
            });
            console.log(" [x] Sent %s", msg);
        });
    });
}