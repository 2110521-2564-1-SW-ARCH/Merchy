require("dotenv").config()
const { consume, produce } = require("./amqp")
const dayjs = require('dayjs')
const isBetween = require('dayjs/plugin/isBetween')
dayjs.extend(isBetween)

let orders = require("./mock_order")

/* request schema
{
    resourceType: "sales",
    startDate: "2020-10-11",
    endDate: "2021-10-25",
    scale: "month" <-- filter ขึ้นกับ scale ละกัน มี day week month year,
    status: "delivering" <-- เราอาจจะแบ่ง status เองง่ายๆ แบบ shipped delivering arrived
    paymentStatus: "paid"
}
*/

function consumeHandler(msg) {
    let request = null
    try{
        request = JSON.parse(msg.content.toString())
    } catch(e) {
        console.log(e)
    }
    if (request.resourceType == "sales") produce("response", calculateSales(request))
}

consume("request", consumeHandler)

function calculateSales(request) {
    // query orders from startDate to endDate and make a summary in "scale"
    let sales = []

    if (request.scale === "year") {
        for (order of orders) {
            let day = dayjs(order.createdAt)
            if (day.isBetween(request.startDate, request.endDate, 'year', "[]")) {
                let y = day.get('year')
                if (sales.length == 0) {
                    sales.push({ year: y, sales: order.totalPrice })
                    continue
                }

                let found = false
                for (s of sales) {
                    if (s.year === y) {
                        s.sales += order.totalPrice
                        found = true
                        break
                    }
                }

                if (!found) sales.push({ year: y, sales: order.totalPrice })

            }
        }
    }

    else if (request.scale === "month") {
        for (order of orders) {
            let day = dayjs(order.createdAt)

            if (day.isBetween(request.startDate, request.endDate, 'month', "[]")) {
                let y = day.get('year')
                let m = day.get('month') + 1

                if (sales.length == 0) {
                    sales.push({ year: y, month: m, sales: order.totalPrice })
                    continue
                }

                let found = false
                for (s of sales) {
                    if (s.year === y && s.month == m) {
                        s.sales += order.totalPrice
                        found = true
                        break
                    }
                }

                if (!found) sales.push({ year: y, month: m, sales: order.totalPrice })
            }
        }
    }

    else if (request.scale === "day") {
        for (order of orders) {
            let day = dayjs(order.createdAt)

            if (day.isBetween(request.startDate, request.endDate, 'day', "[]")) {
                let y = day.get('year')
                let m = day.get('month') + 1
                let d = day.get('date')

                if (sales.length == 0) {
                    sales.push({ year: y, month: m, date: d, sales: order.totalPrice })
                    continue
                }

                let found = false
                for (s of sales) {
                    if (s.year == y && s.month == m && s.date == d) {
                        s.sales += order.totalPrice
                        found = true
                        break
                    }
                }
                if (!found) sales.push({ year: y, month: m, date: d, sales: order.totalPrice })
            }
        }
    }

    return sales
}