require("dotenv").config()
const { consume, produce } = require("./amqp")
const { calculateSales } = require("./functions/calculateSales")

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