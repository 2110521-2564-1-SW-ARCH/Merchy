const mongoose = require("mongoose")
const Schema = mongoose.Schema

const entrySchema = new Schema({
	item: {
		type: Schema.Types.ObjectId,
        ref: 'Item',
		required: true,
	},
	price: {
		type: Number,
		required: true,
	},
    amount: {
        type: Number,
        required: true,
    },
    note: {
        type: String,
        required: true,
    },
    time: {
        type: Date,
        required: true,
    }
})

module.exports = mongoose.model("Entry", entrySchema)
