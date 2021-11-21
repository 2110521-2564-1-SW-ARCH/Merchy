const express = require('express')
const router = express.Router()
const LAZADA = require('../controllers/lazada')

router.route('/login')
    .get(LAZADA.getAuthorizeSellerLink)

router.route('/callback')
    .get(LAZADA.handleAuthorizeCallback)

module.exports = router