import json
import zmq

"""
CLIENT REQUEST DATA FORMATE : "{"opCode": "RM"}"
CLIENT RESPONSE DATA FORMATE : {"opCode":"RRM", "model":"v0.1A"}
"""

class Client:
    def __init__(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connectToServer(self, hostname, port):
        self.socket.connect(f"tcp://{hostname}:{port}")
        print("Connected to Server")
    
    def sendRequest(self, requestString):
        try:
            print("Sending...")
            self.socket.send_string(requestString)
            print("Sended")
        except Exception as e:
            print("Something went wrong")

    def getResponse(self):
        try:
            responseJson = self.socket.recv_json()
            print("From Server: ", responseJson)
        except Exception as e:
            print("Something went wrong")

client = Client()
client.connectToServer('127.0.0.1', 1212)
client.sendRequest('{"opCode": "SSP"}')
client.getResponse()