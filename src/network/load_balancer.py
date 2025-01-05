class LoadBalancer:
    def __init__(self):
        self.nodes = []  # List of active nodes

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def get_next_node(self):
        if not self.nodes:
            raise Exception("No available nodes.")
        return self.nodes[0]  # Simple round-robin for demonstration

    def __repr__(self):
        return f"LoadBalancer(nodes={self.nodes})"
