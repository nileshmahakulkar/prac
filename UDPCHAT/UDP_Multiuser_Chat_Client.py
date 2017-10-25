import socket
import threading
import sys


class Client:
    fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_port = 1024

    def sendMsg(self):
        address = input("Enter Address: ")
        username = input("Enter Username:")
        while True:
            msg = username+":"+input("")
            self.fd.sendto(bytearray(msg,"utf-8"), (address, self.udp_port))

    def __init__(self):
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.fd.recvfrom(1024)
            if not data:
                break
            print(str(data[0],"utf-8"))

client = Client()