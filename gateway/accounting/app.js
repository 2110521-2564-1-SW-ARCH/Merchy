require("dotenv").config()
const express = require('express')
const app = express()
const { consume, produce } = require("./amqp")

PORT = process.env.PORT

function consumeHandler(msg) {
    msg = JSON.parse(msg.content.toString())
    console.log(`[x] App Received ${msg}`)
}

consume("response", consumeHandler)

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
    let msg = req.query.msg
    produce("request", msg)
    res.send("eiei")
})

app.listen(PORT, () => console.log(`RabbitMQ client running at ${PORT}`))