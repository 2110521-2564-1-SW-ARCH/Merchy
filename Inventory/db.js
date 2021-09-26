const mongoose = require("mongoose");

mongoose.connect(process.env.DB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;

// * Successfully connected
db.on("connected", () => console.log("Database Connected"));

// ! If the connection throws an error
db.on("error", console.error.bind(console, "Connection error:"));

// ! When the connection is disconnected
db.on("disconnected", () => console.log("Database Disconnected"));

// * Close connection when the app close
process.on("SIGINT", () => {
  db.close(() => {
    console.log("Database Disconected via App Termination");
    process.exit(0);
  });
});
