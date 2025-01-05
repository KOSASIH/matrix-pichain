import unittest
from blockchain.block import Block
from blockchain.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].index, 0)

    def test_add_block(self):
        block = Block(index=1, transactions=[], previous_hash=self.blockchain.chain[0].compute_hash())
        self.blockchain.add_block(block)
        self.assertEqual(len(self.blockchain.chain), 2)

    def test_invalid_block(self):
        block = Block(index=2, transactions=[], previous_hash="invalid_hash")
        result = self.blockchain.add_block(block)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
