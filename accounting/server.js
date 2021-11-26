require("dotenv").config()
const { consume, produce } = require("./amqp")
const { calculateSales } = require("./functions/calculateSales")
// const express = require("express")
// const app = express()

// app.use(express.json())

async function consumeHandler(msg) {
    let request = null
    try {
        request = JSON.parse(msg.content.toString())
    } catch (e) {
        console.log(e)
    }
    if (request.resourceType == "sales") produce("response", await calculateSales(request))
}

consume("request", consumeHandler)

// app.get("/", (req, res) => res.send("accounting works"))
// app.listen(3008, () => console.log("Accounting running with Express"))