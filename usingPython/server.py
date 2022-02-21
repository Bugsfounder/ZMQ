import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:7777")

while True:
    msg = socket.recv()
    print("From Client" ,msg)
    smsg = input("Enter Your Message Here: ")
    socket.send_string(smsg)
    print("")