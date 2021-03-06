const express = require('express')
const router = express.Router()
const { isJwtLoggedIn } = require('../middleware')

const { getAllUsers, getUser, addUser, updateUser, deleteUser } = require('../controllers/users')


router.route('/')
    .get(getAllUsers)
    .post(addUser)

router.route('/:id')
    .get(getUser)
    .put(updateUser)
    .delete(deleteUser)

module.exports = router