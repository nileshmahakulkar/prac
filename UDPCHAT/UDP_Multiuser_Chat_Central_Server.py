import socket
import threading
import sys


class Server:
    udp_ip = '127.0.0.1'
    udp_port = 1024
    fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connections = set()

    def __init__(self):
        self.fd.bind((self.udp_ip, self.udp_port))

    def sendtoall(self,connections,r):
        for i in connections:
            self.fd.sendto(r[0], i)


    def run(self):
        while True:
            r = self.fd.recvfrom(1024)
            if str(r[0],"utf-8").find("_exit_") != -1:
                print("[-]" + str(r[1]) + "Disconnected")
                self.connections.remove(r[1])
            else:
                print("[+]" + str(r[1]) + "Messaged")
                self.connections.add(r[1])
                self.sendtoall(self.connections,r)


server = Server()
server.run()