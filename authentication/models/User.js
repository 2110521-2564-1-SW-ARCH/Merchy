const {Sequelize, DataTypes} = require('sequelize')
const passportLocalSequelize = require('passport-local-sequelize');
 
// Define a User yourself and use attachToUser

module.exports = (sequelize, DataTypes) => {
    const User = sequelize.define('User', {
        fname: {
            type: DataTypes.STRING,
            allowNull: false
        },
        lname: {
            type: DataTypes.STRING,
            allowNull: false
        },
        email: {
            type: DataTypes.STRING,
            allowNull: false,
            validate: {isEmail: true}
        },
        hash: {
            type: DataTypes.STRING(2048),
            allowNull: false
        },
        salt: {
            type: DataTypes.STRING(2048),
            allowNull: false
        }
    },{
        // defaultScope: {
        //     attributes: { exclude: ['hash', 'salt'] },
        // }
    })

    // User.sync({alter: true})
 
    passportLocalSequelize.attachToUser(User, {
        usernameField: 'email',
        hashField: 'hash',
        saltField: 'salt'
    })

    return User
}

 
// // Setup sequelize db connection
// var db = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
//     host: 'localhost',
//     dialect: 'mysql',
//     logging: false
// })
 
 
// const User = db.define('User', {
//     fname: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     lname: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     email: {
//         type: DataTypes.STRING,
//         allowNull: false,
//         validate: {isEmail: true}
//     },
//     hash: {
//         type: DataTypes.STRING(2048),
//         allowNull: false
//     },
//     salt: {
//         type: DataTypes.STRING(2048),
//         allowNull: false
//     }
// },{
//     // defaultScope: {
//     //     attributes: { exclude: ['hash', 'salt'] },
//     // }
// })

// User.sync({alter: true})
 
// passportLocalSequelize.attachToUser(User, {
//     usernameField: 'email',
//     hashField: 'hash',
//     saltField: 'salt'
// });
 
// module.exports = User