const axios = require("axios")
const dayjs = require('dayjs')
dayjs.extend(require('dayjs/plugin/isBetween'))

ORDER_TRACKING_IP = process.env.ORDER_TRACKING_IP
ORDER_TRACKING_PORT = process.env.ORDER_TRACKING_PORT
ORDER_TRACKING_PROTOL = process.env.ORDER_TRACKING_PROTOL
ORDER_TRACKING_URL = `${ORDER_TRACKING_PROTOL}://${ORDER_TRACKING_IP}:${ORDER_TRACKING_PORT}`

// startDate and endDate must be a str of ISO8601 format
async function getAllOrders(startDate = null, endDate = null) {
    let { data } = await axios.get(`${ORDER_TRACKING_URL}/orders`, {
        params: {
            user_id: 5,
            start_date: startDate,
            end_date: endDate
        }
    })
    return data
}

function getScaleNotation(createdAt, scale) {
    createdAt = dayjs(createdAt)
    switch (scale) {
        case "year":
            return createdAt.format("YYYY")
        case "month":
            return createdAt.format("YYYY-MM")
        case "day":
            return createdAt.format("YYYY-MM-DD")
    }
}

function sortObject(obj) {
    return Object.keys(obj).sort().reduce(function (result, key) {
        result[key] = obj[key]
        return result
    }, {})
}

module.exports.calculateSales = async function (request) {
    if (!request.scale) return { success: false, message: "Missing scale parameter" }
    let response = {}
    let { scale } = request
    let { orders } = await getAllOrders(request.startDate, request.endDate)

    for (order of orders) {
        let orderPrice = Number(order.price)
        let orderCreatedAt = order.createdAt
        let scaleNotation = getScaleNotation(orderCreatedAt, scale)
        if (response[scaleNotation]) response[scaleNotation] += orderPrice
        else response[scaleNotation] = orderPrice
    }

    return sortObject(response)
}
