import socket
import threading
import sys


class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.s.bind(('0.0.0.0', 10000))
        self.s.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                print(str(a[0]) + ':' + str(a[1]) + "Disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.s.accept()

            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()

            self.connections.append(c)
            print(str(a[0]) + ":" + str(a[1]) + "Connected")

class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        username = input("Enter Username:")
        while True:
            msg = username+":"+input("")
            self.s.send(bytearray(msg, 'utf-8'))

    def __init__(self,address):
        self.s.connect((address,10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(str(data,'utf-8'))

if(len(sys.argv)>1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()