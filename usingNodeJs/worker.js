const zmq = require('zeromq');
const socket = zmq.socket('sub')

run();

async function run() {
    await socket.connect("tcp://127.0.0.1:7000");
    console.log("Connecte to Server");
}