from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, transactions=[], previous_hash="1")
        self.chain.append(genesis_block)

    def add_block(self, block):
        if self.is_valid_block(block, self.chain[-1]):
            self.chain.append(block)
            self.current_transactions = []  # Reset current transactions
            return True
        return False

    def is_valid_block(self, block, previous_block):
        if block.index != previous_block.index + 1:
            return False
        if block.previous_hash != previous_block.compute_hash():
            return False
        if not self.valid_proof(previous_block, block.nonce):
            return False
        return True

    def valid_proof(self, last_block, nonce):
        guess = f"{last_block.compute_hash()}{nonce}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example difficulty level

    def __repr__(self):
        return f"Blockchain(chain={self.chain})"
