const axios = require("axios")
const qs = require("qs")

LAZADA = {}

const APP_KEY = process.env.LAZADA_APP_KEY
const APP_SECRET = process.env.LAZADA_APP_SECRET

LAZADA.getAuthorizeSellerLink = function () {
    const authorizeUrl = "https://auth.lazada.com/oauth/authorize"
    let queryString = qs.stringify({
        client_id: APP_KEY,
        redirect_uri: "http://dontknow.com",
        response_type: "code"
    })
    return `${authorizeUrl}?${queryString}`
}

module.exports = LAZADA