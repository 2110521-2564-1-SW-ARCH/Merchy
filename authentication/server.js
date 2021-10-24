const express = require('express')
const passport = require('passport')
const JwtStrategy = require('passport-jwt').Strategy,
    ExtractJwt = require('passport-jwt').ExtractJwt

const cors = require('cors')
require('dotenv').config()
const User = require('./models/User')
const app = express()

// require('./db')
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

passport.use("jwt", new JwtStrategy(opts, async function(jwtPayload, done){
    try {
        const user = User.findOne({where: {email: jwtPayload.email}})
        if (user) return done(null,user)
        else return done(null,false)
    }
    catch (err) {
        return done(err, false)
    }
}))

// Serialization
passport.serializeUser(User.serializeUser())
passport.deserializeUser(User.deserializeUser())

// Register Routes
app.use('/api/user', require('./routes/users'))
app.use('/api', require('./routes/auth'))

app.use((err, req, res, next) => {
    res.json(err)
})

const PORT = process.env.PORT || 3001

app.listen(PORT, () => {
    console.log(`Authentication service running on port ${PORT}`)
})