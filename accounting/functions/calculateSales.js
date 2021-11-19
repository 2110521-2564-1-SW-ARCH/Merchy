const axios = require("axios")
const dayjs = require('dayjs')
dayjs.extend(require('dayjs/plugin/isBetween'))

ORDER_TRACKING_IP = process.env.ORDER_TRACKING_IP
ORDER_TRACKING_PORT = process.env.ORDER_TRACKING_PORT
ORDER_TRACKING_PROTOL = process.env.ORDER_TRACKING_PROTOL
ORDER_TRACKING_URL = `${ORDER_TRACKING_PROTOL}://${ORDER_TRACKING_IP}:${ORDER_TRACKING_PORT}`

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

module.exports.calculateSales = async function (request) {
    let orders = await getAllOrders(request.startDate, request.endDate)
    return orders
}
