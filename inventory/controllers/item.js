const Item = require('../models/Item');
const grpc = require('@grpc/grpc-js');

module.exports.getAllItems = async function ({ request }, cb) {
    const items = await Item.find();
    cb(null, { items });
};

module.exports.getItem = async function ({ request: { id } }, cb) {
    const item = await Item.findById(id);
    if (item) cb(null, item);
    else cb({ code: grpc.status.NOT_FOUND, details: 'Not found' });
};

module.exports.createItem = async function ({ request }, cb) {
    const createdItem = await Item.create(request);
    cb(null, createdItem);
};

module.exports.updateItem = async function ({ request: { id, ...others } }, cb) {
    const existingItem = await Item.findById(id);
    if (existingItem) {
        const updatedItem = await Item.findByIdAndUpdate(id, others, { new: true });
        cb(null, updatedItem);
    } else {
        cb({ code: grpc.status.NOT_FOUND, details: 'Not Found' });
    }
};

module.exports.deleteItem = async function ({ request: { id } }, cb) {
    const deletedEntryItem = await Item.findByIdAndDelete(id);
    if (deletedEntryItem) cb(null, {});
    else cb({ code: grpc.status.NOT_FOUND, details: 'NOT Found' });
};