const axios = require("axios")
const qs = require("qs")
const crypto = require("crypto")

const APP_KEY = process.env.LAZADA_APP_KEY
const APP_SECRET = process.env.LAZADA_APP_SECRET

LAZADA = {}

async function getAccessToken(code) {
    const getAccessTokenUrl = "https://api.lazada.com/rest"
    const apiName = "/auth/token/create"
    const timestamp = Date.now()
    const signMethod = "sha256"
    let paramsString = `${apiName}app_key${APP_KEY}code${code}sign_method${signMethod}timestamp${timestamp}`
    let sign = crypto.createHmac("sha256", APP_SECRET).update(paramsString).digest("hex").toUpperCase()
    let params = {
        app_key: APP_KEY,
        code,
        sign_method: signMethod,
        timestamp,
        sign
    }
    let {data: token} = await axios.get(`${getAccessTokenUrl}${apiName}`, {params})
    return {success: true, token}
}

LAZADA.getAuthorizeSellerLink = (req, res) => {
    const authorizeUrl = "https://auth.lazada.com/oauth/authorize"
    const callbackUrl = "https://authenmerchy.run.goorm.io/api/lazada/callback"
    let queryString = qs.stringify({
        client_id: APP_KEY,
        redirect_uri: callbackUrl,
        response_type: "code"
    })
    return res.redirect(`${authorizeUrl}?${queryString}`)
}

LAZADA.handleAuthorizeCallback = async (req, res) => {
    let result = await getAccessToken(req.query.code)
    if(result.success) {
        // store token in the database
        return res.send(result)
    }
    return res.send("Error")
}

module.exports = LAZADA