const Item = require('../models/Item');
const grpc = require('@grpc/grpc-js');
const LAZADA = require("./lazada")
const { Platform } = require("../models/enum")

module.exports.getAllItems = async function ({ request: { userId } }, cb) {
    if (!userId) return cb({ code: grpc.status.NOT_FOUND, details: 'Missing userId' });
    const items = await Item.find({ userId });
    cb(null, { items });
};

module.exports.getItem = async function ({ request: { id } }, cb) {
    if (!id) return cb({ code: grpc.status.NOT_FOUND, details: 'Missing id' });
    const item = await Item.findById(id);
    if (item) return cb(null, item);
    else return cb({ code: grpc.status.NOT_FOUND, details: 'Not found' });
};

module.exports.createItem = async function ({ request }, cb) {
    if(request.platform == Platform.LAZADA) return cb(null, await LAZADA.createItem(request))
    cb({ code: grpc.status.NOT_FOUND, details: 'Platform is invalid' })
};

module.exports.updateItem = async function ({ request }, cb) {
    if (!request.id) return cb({ code: grpc.status.NOT_FOUND, details: 'Missing id' });
    const response = await LAZADA.updateItem(request)
    if(response.success) return cb(null, response.updatedItem)
    else return cb({ code: grpc.status.NOT_FOUND, details: 'Not Found' });
};

module.exports.deleteItem = async function ({ request: { id } }, cb) {
    const deletedEntryItem = await Item.findByIdAndDelete(id);
    if (deletedEntryItem) return cb(null, {});
    else return cb({ code: grpc.status.NOT_FOUND, details: 'NOT Found' });
};