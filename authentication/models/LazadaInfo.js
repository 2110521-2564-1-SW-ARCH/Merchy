const {Sequelize, DataTypes} = require('sequelize')
const User = require('./User')
 
 
// Define a User yourself and use attachToUser

module.exports = (sequelize, DataTypes) => {
    const LazadaInfo = db.define('LazadaInfo', {
        accessToken: {
            type: DataTypes.STRING,
            allowNull: false
        },
        refreshToken: {
            type: DataTypes.STRING,
            allowNull: false
        },
        expiresIn: {
            type: DataTypes.INTEGER,
            allowNull: false,
            validate: {isEmail: true}
        },
        refreshExpiresIn: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        sellerId: {
            type: DataTypes.STRING,
            allowNull: false
        },
        lazadaUserId: {
            type: DataTypes.STRING,
            allowNull: false
        }
    },{
        // defaultScope: {
        //     attributes: { exclude: ['hash', 'salt'] },
        // }
    })

    // LazadaInfo.sync({alter: true})
    return LazadaInfo
}
 
// const LazadaInfo = db.define('LazadaInfo', {
//     accessToken: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     refreshToken: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     expiresIn: {
//         type: DataTypes.INTEGER,
//         allowNull: false,
//         validate: {isEmail: true}
//     },
//     refreshExpiresIn: {
//         type: DataTypes.INTEGER,
//         allowNull: false
//     },
//     sellerId: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     lazadaUserId: {
//         type: DataTypes.STRING,
//         allowNull: false
//     }
// },{
//     // defaultScope: {
//     //     attributes: { exclude: ['hash', 'salt'] },
//     // }
// })

// User.hasOne(LazadaInfo)
 
// module.exports = LazadaInfo
