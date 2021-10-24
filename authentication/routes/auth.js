const passport = require('passport')
const express = require('express')
const router = express.Router()

const {login, logout, protected} = require('../controllers/auth')

router.route('/login')
    .post(passport.authenticate('local', { session: false }), login)

router.route('/logout')
    .post(logout)

router.route('/protected')
    .get(passport.authenticate('jwt', {session: false}), protected)

module.exports = router