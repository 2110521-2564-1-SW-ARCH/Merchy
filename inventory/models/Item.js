const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const attributeSchema = new Schema({
	name: {
		type: String,
		required: true
	},
	description: {
		type: String,
		required: true
	},
	brand: {
		type: String,
		required: true
	}
}, { _id: false })

const skuSchema = new Schema({
	sellerSku: {
		type: String,
		required: true
	},
	quantity: {
		type: Number,
		required: true
	},
	price: {
		type: Number,
		required: true
	},
	skuId: {
		type: Number,
		required: true,
		default: -1
	},
	images: {
		type: [String],
		required: true
	},
	packageHeight: {
		type: Number,
		required: true
	},
	packageLength: {
		type: Number,
		required: true
	},
	packageWidth: {
		type: Number,
		required: true
	},
	packageWeight: {
		type: Number,
		required: true
	}
}, { _id: false })

const itemSchema = new Schema({
	userId: {
		type: String,
		required: true
	},
	platform: {
		type: String,
		required: true
	},
	itemId: {
		type: Number,
		required: true,
		default: -1
	},
	primaryCategory: {
		type: Number,
		required: true
	},
	createdAt: {
		type: Date,
		required: true,
		default: Date.now
	},
	updatedAt: {
		type: Date,
		required: true,
		default: Date.now
	},
	attributes: {
		type: attributeSchema,
		required: true
	},
	skus: {
		type: [skuSchema],
		required: true
	}
});

module.exports = mongoose.model("Item", itemSchema);
