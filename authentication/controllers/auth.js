const User = require('../models/User')
const jwt = require('jsonwebtoken')

module.exports.login = async (req, res) => {
    // create token and send it back to user
    const user = {};
    ['fname','lname','email','id'].forEach(prop => user[prop] = req.user[prop])
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
    res.send('yay')
}

