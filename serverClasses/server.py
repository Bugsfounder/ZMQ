import zmq

class Server:
    def __init__(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
    
    def crateServerAndBind(self, port):
        self.socket.bind(f"tcp://*:{port}")
        print(f"Server Listernning at Port: {port}")

    def acceptRequest(self):
        requestString =  self.socket.recv_string()
        print(f"From Client:", requestString)
        self.socket.send_string(f"Hello {requestString.capitalize()}")

server = Server()
server.crateServerAndBind(1212)
while True:
    server.acceptRequest()