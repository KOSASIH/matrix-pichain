import hashlib
import json
from time import time

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time()
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, transactions={self.transactions}, previous_hash='{self.previous_hash}', timestamp={self.timestamp}, nonce={self.nonce})"
