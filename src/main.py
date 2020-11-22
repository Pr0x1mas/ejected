import socket
import decode

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 22023
ip = ""

serverAddress = (ip, port)

sock.bind(serverAddress)

def acknowledge(nonce, address):
    sock.sendto(b'\x0a' + nonce + b'\xFF', address)




class packet:
    def __init__(self, inputData):
        self.rawData  = inputData[0]
        self.clientAddress = inputData[1]
        self.opcode = self.rawData[0]
        self.acknowledged = False

        if self.opcode == 0:
            self.data = decode.unreliable(self.rawData)
        
        elif self.opcode == 1:
            self.data = decode.reliable(self.rawData)
            acknowledge(self.data["nonce"], self.clientAddress)
            self.acknowledged = True
        
        elif self.opcode == 8:
            self.data = decode.hello(self.rawData)
            acknowledge(self.data["nonce"], self.clientAddress)
            self.acknowledged = True
        
        elif self.opcode == 9:
            self.data = decode.disconnect(self.rawData)
        
        elif self.opcode == 10:
            self.data = decode.acknowledge(self.rawData)
        
        elif self.opcode == 12:
            self.data = decode.ping(self.rawData)
            acknowledge(self.data["nonce"], self.clientAddress)
            self.acknowledged = True
        
        else:
            raise Exception("Unknown opcode " + str(self.opcode) + "\n data: " + str(self.rawData))
        
        #print(self.data)
        print(self.rawData)

        if not self.acknowledged:

            #print(self.rawData)
            pass

while True:
    input = packet(sock.recvfrom(1024))
    pass