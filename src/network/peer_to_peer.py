import socket
import threading
import json

class PeerToPeer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.peers = set()  # Set of connected peers
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Listening for connections on {self.host}:{self.port}")

    def accept_connections(self):
        while True:
            client_socket, address = self.server.accept()
            print(f"Connection from {address} has been established.")
            self.peers.add(address)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                self.broadcast(message)
            except ConnectionResetError:
                break
        client_socket.close()

    def broadcast(self, message):
        for peer in self.peers:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(peer)
                    sock.send(message.encode())
            except Exception as e:
                print(f"Failed to send message to {peer}: {e}")

    def __repr__(self):
        return f"PeerToPeer(host={self.host}, port={self.port})"

# To run the P2P server
if __name__ == "__main__":
    p2p = PeerToPeer()
    p2p.accept_connections()
