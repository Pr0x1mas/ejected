import socket
import decode

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 22023
ip = "127.0.0.1"

serverAddress = (ip, port)

sock.bind(serverAddress)

def acknowledge(nonce, address):
    sock.sendto(b'0x0a' + nonce + b'\0xFF', address)

class packet:
    def __init__(self, inputData):
        self.rawData  = inputData[0]
        self.clientAddress = inputData[1]
        self.opcode = self.rawData[0]

        if self.opcode == 0:
            self.data = decode.Unreliable(self.rawData)
        elif self.opcode == 1:
            self.data = decode.Reliable(self.rawData)
        elif self.opcode == 8:
            self.data = decode.Hello(self.rawData)
            acknowledge(self.data["nonce"], self.clientAddress)
            self.acknowledged = True
        elif self.opcode == 9:
            self.data = decode.Disconnect(self.rawData)
        elif self.opcode == 10:
            self.data = decode.Acknowledge(self.rawData)
        elif self.opcode == 12:
            self.data = decode.Ping(self.rawData)
        else:
            raise Exception("Unknown opcode " + str(self.opcode) + "\n data: " + str(self.rawData))

        print(self.data)



while True:
    input = packet(sock.recvfrom(1024))