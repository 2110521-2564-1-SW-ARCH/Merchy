const User = require('../models/User')
const jwt = require('jsonwebtoken')

module.exports.login = async (req, res) => {
    const {salt, hash, __v, _id, ...user} = req.user.toObject()
    const token = jwt.sign(user, process.env.SECRET, {expiresIn: "2 days"})
    return res.json({token, user})
}

module.exports.logout = async (req, res) => {
    // create token and send it back to user
    req.logout();
    res.send('Logout Success!')
}

module.exports.authorize = async (req, res) => {
    // use passport authorize
}

module.exports.protected = async (req, res) => {
    // use passport authorize
    console.log(req.user)
    res.send('yay')
}

