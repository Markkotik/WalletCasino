import threading


class NodeRotator:
    def __init__(self, nodes):
        self.nodes = nodes
        self.index = 0
        self.lock = threading.Lock()

    def get_next_node(self):
        with self.lock:
            node = self.nodes[self.index]
            self.index = (self.index + 1) % len(self.nodes)
            return node
