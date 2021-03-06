const amqp = require('amqplib/callback_api');
const HOST = process.env.AMQP_IP

module.exports.consume = (queue, cb) => {
    amqp.connect(HOST, function (error0, connection) {
    // amqp.connect(`amqp://${HOST}`, function (error0, connection) {
        if (error0) {
            throw error0;
        }
        connection.createChannel(function (error1, channel) {
            if (error1) {
                throw error1;
            }

            channel.assertQueue(queue, {
                durable: false
            });

            console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);
            try {
                channel.consume(queue, cb, {
                    noAck: true
                });
            } catch(e) {
                print(e)
            }

        });
    });
}

module.exports.produce = (queue, msg) => {
    amqp.connect(HOST, function (error0, connection) {
        if (error0) {
            throw error0;
        }
        connection.createConfirmChannel(function (error1, channel) {
            if (error1) {
                throw error1;
            }

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