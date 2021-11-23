const {Sequelize, DataTypes} = require('sequelize')
const passportLocalSequelize = require('passport-local-sequelize');
 
// Setup sequelize db connection
var sequelize = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
    host: 'localhost',
    dialect: 'mariadb',
    logging: false
})

const db = {sequelize}

db.User = require("./User.js")(sequelize, DataTypes)
db.LazadaInfo = require("./LazadaInfo.js")(sequelize, DataTypes)

module.exports = db