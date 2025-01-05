class Node:
    def __init__(self, node_id, host='localhost', port=5000):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.is_active = True

    def start(self):
        print(f"Node {self.node_id} is starting on {self.host}:{self.port}")

    def stop(self):
        self.is_active = False
        print(f"Node {self.node_id} has stopped.")

    def __repr__(self):
        return f"Node(id={self.node_id}, host={self.host}, port={self.port}, active={self.is_active})"
