def Unreliable(inputData):
    data = {
        "opcode": inputData[0],
        "length": inputData[1:3],
        "ID": inputData[3],
        "data": inputData[4:len(inputData) + 2]
    }
    return data

def Reliable(inputData):
    data = {
        "opcode": inputData[0],
        "nonce": inputData[1:3],
        "length": inputData[3:5],
        "ID": inputData[5],
        "data": inputData[6:len(inputData) + 1]
    }
    return data

def Hello(inputData):
    data = {
        "opcode": inputData[0],
        "nonce": inputData[1:3],
        "hazelVersion": inputData[3],
        "clientVersion": inputData[4:8],
        "username": inputData[8:len(inputData) + 1].decode('utf-8')
    }

    return data

def Disconnect(inputData):
    data = {
        "opcode": inputData[0],
        "length": inputData[2:4]
    }

    return data

def Acknowledge(inputData):
    data = {
        "opcode": inputData[0],
        "nonce": inputData[1:3],
    }

    return data

def Ping(inputData):
    data = {
        "opcode": inputData[0],
        "nonce": inputData[1:3],
    }

    return data