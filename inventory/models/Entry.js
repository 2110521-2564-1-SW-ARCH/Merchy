const mongoose = require("mongoose")
const Schema = mongoose.Schema

const addressBilling = new Schema({
    firstName: {
        type: String,
        required: true
    },
    postCode: {
        type: String,
        required: true
    },
    country: {
        type: String,
        required: true
    },
    city: {
        type: String,
        required: true
    }
}, { _id: false })

const addressShipping = new Schema({
    firstName: {
        type: String,
        required: true
    },
    postCode: {
        type: String,
        required: true
    },
    country: {
        type: String,
        required: true
    },
    city: {
        type: String,
        required: true
    }
}, { _id: false })

const orderItem = new Schema({
    item: {
        type: Schema.Types.ObjectId,
        ref: "Item",
        required: true
    },
    itemPrice: {
        type: String,
        required: true
    },
    taxAmount: {
        type: String,
        required: true
    },
    buyerId: {
        type: String,
        required: true
    },
    shippingProvider: {
        type: String,
        required: true
    },
    trackingCode: {
        type: String,
        required: true
    },
    skuId: {
        type: String,
        required: true
    },
    statuses: {
        type: [String],
        required: true
    }
}, { _id: false })

const entrySchema = new Schema({
    userId: {
        type: String,
        required: true
    },
    platform: {
        type: String,
        required: true
    },
    shippingFee: {
        type: String,
        required: true
    },
    paymentMethod: {
        type: String,
        required: true
    },
    orderId: {
        type: String,
        required: true
    },
    itemsCount: {
        type: Number,
        required: true
    },
    price: {
        type: String,
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
    addressBilling: {
        type: addressBilling,
        required: true
    },
    addressShipping: {
        type: addressShipping,
        required: true
    },
    orderItems: {
        type: [orderItem],
        required: true
    }
})

module.exports = mongoose.model("Entry", entrySchema)
