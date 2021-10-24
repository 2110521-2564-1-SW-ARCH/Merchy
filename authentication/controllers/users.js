const User = require('../models/User')

module.exports.getAllUsers = async (req, res) => {
    const users = await User.find()
    return res.json(users)
}

module.exports.getUser = async (req, res) => {
    const {id} = req.params
    const user = await User.findById(id)
    return res.json(user)
}

module.exports.addUser = async (req, res) => {
    const { password,...info } = req.body
    const user = new User(info)
    const registeredUser = await User.register(user, password);
    return res.json(registeredUser)
}

module.exports.updateUser = async (req, res) => {
    const {id} = req.params
    const user = await User.findByIdAndUpdate(id, req.body, {new: true})
    return res.json(user)
}

module.exports.deleteUser = async (req, res) => {
    await User.findByIdAndDelete(req.params.id)
    return res.json({message: "User was deleted sucessful"})
}