const zmq = require('zeromq');

const sock = zmq.socket('pub');

const run = async() => {
    await socket.bind("tcp://127.0.0.1:7000");
    console.log("Server is Ready listenning on port 7000");
    console.log("press any key to start sending the jobs");
    process.stdin.once("data", send);
}

// sending the jobs to the workers
const send = async() => {
    console.log("About to send Jobs");

    for (let i = 0; i < 100; i++) {
        await sock.send(`Sending JOB_ID: ${i}`);

        // WAIT 500ms
        await new Promise(resolve => setTimeout(resolve, 500));
    }
}

run();