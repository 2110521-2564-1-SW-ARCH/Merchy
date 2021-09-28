const Entry = require('../models/Entry');
const Item = require('../models/Item');

module.exports.getAllEntries = async function (_, cb) {
    const entries = await Entry.find().populate('item');
    cb(null, { entries });
};

module.exports.get = async function ({ request }, cb) {
    const entry = await Entry.findById(request.id).populate('item');
    if (entry) cb(null, entry );
    else cb({ code: grpc.status.NOT_FOUND, details: 'Not found' });
};

module.exports.insert = async function (
    {
        request: {
            item: { id: itemId },
            ...others
        },
    },
    cb
) {
    const createdEntry = await Entry.create({
        item: itemId,
        ...others,
    });
    cb(null, createdEntry);
};

module.exports.update = async function ({ request: { id, ...others } }, cb) {
    const existingEntry = await Entry.findById(id);
    if (existingEntry) {
        const updatedEntry = await Entry.findByIdAndUpdate(id, others, {
            new: true,
        });
        cb(null, updatedEntry);
    } else {
        cb({ code: grpc.status.NOT_FOUND, details: 'Not Found' });
    }
};

module.exports.remove = async function ({ request: { id } }, cb) {
    const deletedEntryItem = await Entry.findByIdAndDelete(id);
    if (deletedEntryItem) cb(null, {});
    else cb({ code: grpc.status.NOT_FOUND, details: 'NOT Found' });
};

module.exports.createItem = async function ({ request }, cb) {
    const createdItem = await Item.create(request);
    cb(null, createdItem);
};