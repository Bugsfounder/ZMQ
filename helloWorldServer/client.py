import zmq

# INITIALIZING HOSTNAME AND PORT
hostname = 'localhost'
port = 2323

# INITIALIZING CONTEXT AND SOCKET
context = zmq.Context()
socket = context.socket(zmq.REQ)

try:
    # CONNECTINT TO THE SERVER WHICH IS HOSTER ON GIVEN PORT
    socket.connect(f"tcp://{hostname}:{port}")
    print("Connected To Server") # IF CONNECTED
except Exception as e:
    print("Unable to Connect to the Server")

while True:
    try:
        # SENDING MESSAGE TO THE SERVER ==> REQUEST
        requestMsg = input("Enter message to Send: ")
        socket.send_string(requestMsg)

        # RECEIVE MESSAGE FROM THE SERVER ==> RESPONSE
        responseMsg = socket.recv()
        print(f"From Server: [ {responseMsg} ]")
    except Exception as e:
        print("SomeError Occured")