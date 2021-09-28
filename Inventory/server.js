const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const path = require('path');
require('dotenv').config()

// Connect to Database
require('./db')

const IP = process.env.IP
const PORT = process.env.PORT || 3000

const PROTO_PATH = path.join(__dirname, '..', 'merchy.proto');
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true,
});

const merchyProto = grpc.loadPackageDefinition(packageDefinition);

const functions = require("./controllers")

const server = new grpc.Server();
server.addService(merchyProto.InventoryService.service, functions);

server.bindAsync(`${IP}:${PORT}`, grpc.ServerCredentials.createInsecure(), () => { 
    console.log(`server running at ${IP}:${PORT}`)
    server.start()
})