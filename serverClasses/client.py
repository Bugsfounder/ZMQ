import zmq

class Client:
    def __init__(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connectToServer(self, hostname, port):
        self.socket.connect(f"tcp://{hostname}:{port}")
        print("Connected To Server") 

    def sendRequest(self):
        requestMsg = input("Enter message to Send: ")
        self.socket.send_string(requestMsg)

    def acceptReponse(self):
        responseMsg = self.socket.recv_string()
        print(f"From Server: {responseMsg}")

client = Client()

client.connectToServer('127.0.0.1', 1212)

while True:
    client.sendRequest()
    client.acceptReponse()