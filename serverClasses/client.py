import zmq

# CREATING A CLASS CLIENT
class Client:
    # CREATING CONSTRUCTOR 
    def __init__(self) -> None:
        """CONSTRUCTOR THAT CREATER CONTEXT AND SOCKET"""
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    # CREATING A METHOD TO CONNECT TO SERVER 
    def connectToServer(self, hostname, port):
        """METHOD TO CONNECT TO THE SERVER: TAKE "hostname" AND "port" AS PARAMETERS AND RETURN NOTHING"""
        self.socket.connect(f"tcp://{hostname}:{port}")
        print("Connected To Server") 

    # CREATING A FUNCTION TO SEND REQUEST TO THE SERVER
    def sendRequest(self):
        """THIS METHOD IS SEND REQUEST TO THE SERVER"""
        requestMsg = input("Enter message to Send: ")
        self.socket.send_string(requestMsg)

    # CREATING A FUNCTION TO GET RESPONSE THAT COMMING FROM SERVER 
    def acceptReponse(self):
        
        responseMsg = self.socket.recv_string()
        print(f"From Server: {responseMsg}")

client = Client()

client.connectToServer('127.0.0.1', 1212)

while True:
    client.sendRequest()
    client.acceptReponse()