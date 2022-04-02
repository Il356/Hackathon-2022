import socket

class Network:
    def _init_(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sever = "138.38.242.150"
        self.port = 5555
        self.addr = (self.server , self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    
n = Network()