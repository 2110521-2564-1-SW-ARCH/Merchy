// const User = require('../models/User')
const db = require("../models");
const {User, LazadaInfo} = db

module.exports.getAllUsers = async(req, res) => {
    const users = await User.findAll()
    return res.json(users)
}

module.exports.getUser = async(req, res) => {
    const { id } = req.params
    try {
        let user = await User.findByPk(id)
        const platforms = []
        const hasLazada = await LazadaInfo.findOne({
            where: {userId: id}
        })
        if (hasLazada) platforms.push('lazada')
        if (!user) return res.json({message: "No User"})

        user = user.toJSON()
        user.platforms = platforms
        return res.json(user)
    } catch (e) {
        return res.json(e)
    }
}

module.exports.addUser = async(req, res) => {
    const { password, ...info } = req.body
    User.register(info, password, (err, user) => {
        if (err) return res.json(err)
        if (user) return res.json(user)
    })
}

module.exports.updateUser = async(req, res) => {
    const { id } = req.params
    await User.update(req.body, {where: {id}})
    const user = await User.findByPk(id)
    return res.json(user)
}

module.exports.deleteUser = async(req, res) => {
    try {
        await User.destroy({where: {id: req.params.id}})
        return res.json({ message: "User was deleted sucessful" })
    }
    catch (e) {
        return res.json(e)
    }
}