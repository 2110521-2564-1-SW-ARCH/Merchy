const Entry = require('../models/Entry');
const grpc = require('@grpc/grpc-js');

module.exports.getAllEntries = async function ({ request: { id } }, cb) {
    const entries = await Entry.find({ userId: id }).populate('item');
    cb(null, { entries });
};

module.exports.getEntry = async function ({ request }, cb) {
    const entry = await Entry.findById(request.id).populate('item');
    if (entry) cb(null, entry);
    else cb({ code: grpc.status.NOT_FOUND, details: 'Not found' });
};

module.exports.createEntry = async function (
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

module.exports.updateEntry = async function ({ request: { id, item: { id: itemId }, ...others } }, cb) {
    const existingEntry = await Entry.findById(id);
    if (existingEntry) {
        const updatedEntry = await Entry.findByIdAndUpdate(id, { item: itemId, ...others }, {
            new: true,
        });
        cb(null, updatedEntry);
    } else {
        cb({ code: grpc.status.NOT_FOUND, details: 'Not Found' });
    }
};

module.exports.deleteEntry = async function ({ request: { id } }, cb) {
    const deletedEntryItem = await Entry.findByIdAndDelete(id);
    if (deletedEntryItem) cb(null, {});
    else cb({ code: grpc.status.NOT_FOUND, details: 'NOT Found' });
};