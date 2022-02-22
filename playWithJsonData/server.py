import json
import zmq

"""
SERVER REQUESTED DATA FORMATE :  "{"opCode": "RM"}"
SERVER RESPONSE DATA FORMATE : {"opCode":"RRM", "model":"v0.1A"}
"""

class Server:
    def __init__(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)

    def processCommand(self, stringMessage):
        try:
            parsed = json.loads(stringMessage)
            return parsed
        except Exception as e:
            print("Not a Valid JSON String")
        
    def createServer(self, port):
        self.socket.bind(f"tcp://*:{port}")
        print(f"Server Listernning at Port: {port}")

    def acceptRequest(self):
        requestedString = self.socket.recv_string()
        print(f"From Client:", requestedString)
        getJsonData = self.processCommand(requestedString)
        getJsonData['opCode'] = "R"+getJsonData['opCode']
        getJsonData['model'] = "v0.1A"
        self.socket.send_json(getJsonData)


server = Server()
server.createServer(1212)
while True:
    server.acceptRequest()
