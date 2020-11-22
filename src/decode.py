import byteReader

def unreliable(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "length": byteReader.uint16(),
        "ID": byteReader.uint8(),
        "data": byteReader.endBytes()
    }
    return data

def reliable(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "nonce": byteReader.uint16(),
        "length": byteReader.uint16(),
        "ID": byteReader.uint8(),
        "data": byteReader.endBytes()
    }
    '''
    if data["ID"] == 0x00:
        hostGameRequest(data)
    '''
    return data

def hello(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "nonce": byteReader.uint16(),
        "hazelVersion": byteReader.uint8(),
        "clientVersion": byteReader.int32(),
        "username": byteReader.endBytes().decode('utf-8')
    }

    return data

def disconnect(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "length": byteReader.uint16()
    }

    return data

def acknowledge(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "nonce": byteReader.uint16()
    }

    return data

def ping(inputData):
    byteReader.init(inputData)
    data = {
        "opcode": byteReader.byte(),
        "nonce": byteReader.uint16()
    }

    return data

'''
def hostGameRequest(inputData):
    options = {
        "length": inputData[1],
        "version": inputData[2],
        "maxPlayers": inputData[3],
        "language": inputData[3],
    }
'''