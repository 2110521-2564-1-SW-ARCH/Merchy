require("dotenv").config()
const { consume, produce } = require("./amqp")

function consumeHandler(msg) {
    // add to db
    msg = JSON.parse(msg.content.toString())
    console.log(`[x] Received ${msg}`)
    produce("response", `Server received ${msg}`)
}

consume("request", consumeHandler)