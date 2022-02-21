import zmq

# INITIALIZING PORT
port = 2323

# INITIALIZING COTNEXT
context = zmq.Context()

# INITIALIZING SOCKET
socket = context.socket(zmq.REP)
socket.bind(f"tcp://*:{port}")

while True:
    # RECEIVE MESSAGE THAT COMMING FROM CLIENT
    msg = socket.recv()
    print(f"From Client: [{msg}]")

    # SENDING MESSAGE TO CLIENT AS RESPONSE
    socket.send_string(f"{msg} World")