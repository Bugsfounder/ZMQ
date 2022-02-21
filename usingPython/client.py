import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:7777")

while True:
    msg = input("Enter Your Message Here: ");
    socket.send_string(msg)
    print(f"Sending {msg}")
    print(f"From Server : {socket.recv()}")
    print("")