const axios = require("axios")
const qs = require("qs")
const crypto = require("crypto")

const APP_KEY = process.env.LAZADA_APP_KEY
const APP_SECRET = process.env.LAZADA_APP_SECRET

const db = require("../models");
const {User, LazadaInfo} = db

LAZADA = {}

function signRequest(apiName, params, secret) {
    // only accepts the sha256 sign method
    let paramsString = apiName
    for (let [param, value] of Object.entries(params)) {
        paramsString += `${param}${value}`
    }
    return crypto.createHmac("sha256", secret).update(paramsString).digest("hex").toUpperCase()
}


async function getAccessToken(code) {
    const getAccessTokenUrl = "https://api.lazada.com/rest"
    const apiName = "/auth/token/create"
    const timestamp = Date.now()
    const signMethod = "sha256"
    let params = {
        app_key: APP_KEY,
        code,
        sign_method: signMethod,
        timestamp
    }
    params.sign = signRequest(apiName, params, APP_SECRET)
    let { data: token } = await axios.get(`${getAccessTokenUrl}${apiName}`, { params })
    return { success: true, token }
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
    if (result.success) {
        // store token in the database
        const {token} = result
        const lazadaInfo = {
            accessToken: token.access_token,
            refreshToken: token.refresh_token,
            expiresIn: token.expires_in,
            refreshExpiresIn: token.refresh_expires_in,
            lazadaUserId: token.country_user_info.user_id,
            sellerId: token.country_user_info.user_id,
            userId: req.query.userId
        }
        await LazadaInfo.create(lazadaInfo)
        
        return res.send(result)
    }
    return res.send("Error")
}

module.exports = LAZADA