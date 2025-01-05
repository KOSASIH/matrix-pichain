import socket

class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")

    def send(self, message):
        if self.socket:
            self.socket.send(message.encode())
            print(f"Sent message: {message}")

    def receive(self):
        if self.socket:
            return self.socket.recv(1024).decode()

    def close(self):
        if self.socket:
            self.socket.close()
            print(f"Connection to {self.host}:{self.port} closed.")

    def __repr__(self):
        return f"Connection(host={self.host}, port={self.port})"
