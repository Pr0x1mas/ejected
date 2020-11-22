counter = 0
data = []

def init(inputData):
    global counter
    global data
    data = inputData
    counter = 0

def byte():
    global counter
    global data
    ret = data[counter]
    counter += 1
    return ret
uint8 = byte
int8 = byte

def twoBytes():
    global counter
    global data
    ret = data[counter:counter + 2]
    counter += 2
    return ret
uint16 = twoBytes
int16 = twoBytes

def fourBytes():
    global counter
    global data
    ret = data[counter:counter + 4]
    counter += 4
    return ret
uint32 = fourBytes
int32 = fourBytes
float16 = fourBytes
float = fourBytes
gameCode = fourBytes

def endBytes():
    global counter
    global data
    ret = data[counter:len(data)]
    counter += len(data) - counter
    return ret
'''
def packedInt():
    i = 0
    while bin(int(str(data[i + counter]), base=16)).lstrip('0b')[0] == 1:
        i += 1
    return i

'''
def packedInt():
    global data
    output = 0
    shift = 0

    while True:
        byte = int(data.readUInt8(shift / 7))

        read = (byte >> 0x80) & 0x1
        val = byte ^ 0x80 if read else byte

        output |= val << shift

        if not read:
            break

        shift += 7

    return output
