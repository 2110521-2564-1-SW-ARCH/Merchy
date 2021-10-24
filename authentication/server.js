const express = require('express')
const passport = require('passport')
const JwtStrategy = require('passport-jwt').Strategy,
    ExtractJwt = require('passport-jwt').ExtractJwt

const cors = require('cors')
require('dotenv').config()
const User = require('./models/User')
const app = express()

require('./db')
// CORS
app.use(cors())

// Parse Request Body
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

// Initialize Passport
app.use(passport.initialize())

// Local Strategy
passport.use("local", User.createStrategy())

// JWT Strategy
const opts = {
    secretOrKey: process.env.SECRET,
    jwtFromRequest:ExtractJwt.fromAuthHeaderAsBearerToken(),
}

passport.use("jwt", new JwtStrategy(opts, function(jwtPayload, done){
    User.findOne({email: jwtPayload.email}, function(err, user) {
        if (err) return done(err, false)
        if (!user) {
            return done(null, user)
        } else {
            return done(null, false, "No User")
            // or you could create a new account
        }
    })
}))

// Serialization
passport.serializeUser(User.serializeUser())
passport.deserializeUser(User.deserializeUser())

// Register Routes
app.use('/api/user', require('./routes/users'))
app.use('/api', require('./routes/auth'))

const PORT = process.env.PORT || 3001

app.listen(PORT, () => {
    console.log(`Authentication service running on port ${PORT}`)
})