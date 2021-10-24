const User = require('../models/User')

module.exports.getAllUsers = async(req, res) => {
    const users = await User.findAll()
    return res.json(users)
}

module.exports.getUser = async(req, res) => {
    const { id } = req.params
    try {
        const user = await User.findByPk(id)
        if (!user) return res.json({message: "No User"})
        return res.json(user.toJSON())
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