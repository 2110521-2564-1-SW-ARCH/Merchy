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

entrySchema.statics.findByIdProto = async function(id) {
    const entry = await this.findById(id).populate('Item')
    if (!entry) return null
    const {item, ...others} = entry
    return {...others, name: item.name, itemId: item._id}
}

entrySchema.statics.findAllProto = async function() {
    const entries = await this.find().populate('Item')
    const result = entries.map(({item, ...others}) => ({...others, name: item.name, itemId: item._id}))
    return result
}

module.exports = mongoose.model("Entry", entrySchema)
