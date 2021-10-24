const {Sequelize, DataTypes} = require('sequelize')
const passportLocalSequelize = require('passport-local-sequelize');
 
// Setup sequelize db connection
var db = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
    host: 'localhost',
    dialect: 'mariadb',
    logging: false
})

const db = {};


require("./tutorial.model.js")(sequelize, DataTypes);

module.exports = db;