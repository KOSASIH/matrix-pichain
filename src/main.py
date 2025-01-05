import logging
import time
from constants import (
    PI_COIN_SYMBOL,
    PI_COIN_GENESIS_BLOCK_TIMESTAMP,
    PI_COIN_NETWORK_PROTOCOL,
    PI_COIN_MAX_PEERS,
    PI_COIN_API_REQUEST_LIMIT,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MatrixPiChain:
    def __init__(self):
        self.peers = []
        self.blockchain = []
        self.current_transactions = []
        self.node_id = self.generate_node_id()
        self.initialize_blockchain()

    def generate_node_id(self):
        # Generate a unique node ID (could be based on IP, UUID, etc.)
        return f"node-{int(time.time())}"

    def initialize_blockchain(self):
        # Create the genesis block
        genesis_block = {
            "index": 0,
            "timestamp": PI_COIN_GENESIS_BLOCK_TIMESTAMP,
            "transactions": [],
            "previous_hash": "1",
            "nonce": 0,
        }
        self.blockchain.append(genesis_block)
        logger.info("Genesis block created.")

    def add_transaction(self, transaction):
        # Add a transaction to the current list
        self.current_transactions.append(transaction)
        logger.info(f"Transaction added: {transaction}")

    def mine_block(self):
        # Mine a new block and add it to the blockchain
        if not self.current_transactions:
            logger.warning("No transactions to mine.")
            return

        last_block = self.blockchain[-1]
        new_block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.current_transactions,
            "previous_hash": self.hash(last_block),
            "nonce": self.proof_of_work(last_block),
        }
        self.blockchain.append(new_block)
        self.current_transactions = []  # Reset the current transactions
        logger.info(f"New block mined: {new_block}")

    def hash(self, block):
        # Create a SHA-256 hash of a block
        import hashlib
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        # Simple proof of work algorithm
        nonce = 0
        while not self.valid_proof(last_block, nonce):
            nonce += 1
        return nonce

    def valid_proof(self, last_block, nonce):
        # Validate the proof of work
        guess = f"{last_block['previous_hash']}{nonce}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Example difficulty level

    def run(self):
        logger.info("Matrix PiChain node is starting...")
        while True:
            # Main loop for the node
            time.sleep(1)  # Simulate work being done

if __name__ == "__main__":
    node = MatrixPiChain()
    node.run()
