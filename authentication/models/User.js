const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const passportLocalMongoose = require('passport-local-mongoose');

// userexample = {
//     fname: garky,
//     lname: garky,
//     email: gark@gark.com,
//     password: garkgark
// }

const userSchema = new Schema({
    fname: {
        type: String,
        required: true,
    },
    lname: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
    }
})


userSchema.plugin(passportLocalMongoose, { usernameField: "email" })
module.exports = mongoose.model('User', userSchema)