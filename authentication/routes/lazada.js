const express = require('express')
const router = express.Router()
const LAZADA = require('../controllers/lazada')

router.route('/login')
    .get(LAZADA.getAuthorizeSellerLink)

router.route('/callback')
    .get(LAZADA.handleAuthorizeCallback)

router.route('/access-token/:userId')
    .get(LAZADA.getAccessTokenByUserId)

router.route('/seller-id/:userId')
    .get(LAZADA.getSellerIdByUserId)

module.exports = router