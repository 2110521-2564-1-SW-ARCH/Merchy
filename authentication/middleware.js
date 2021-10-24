const passport = require('passport')

module.exports.isJwtLoggedIn = passport.authenticate('jwt', { session: false })