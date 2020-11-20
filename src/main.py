# main.py - Created for Ejected by TheProgramableTurtle and Pr0x1mas - 20/11/2020
# what
import socket
import threading


class ThreadMain(threading.Thread):
    def __init__(self, priority):
        self.priority = priority

    def run(self):
        main()


def main():
    servSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('127.0.0.1', 22023)

    servSock.bind(addr)

    return


if __name__ == "__main__":
    threadMain = ThreadMain(1)
    threadMain.start()
