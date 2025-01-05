import unittest
from wallet.wallet import Wallet

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet("TestWallet")
        self.wallet.create_wallet()

    def test_initial_balance(self):
        self.assertEqual(self.wallet.get_balance(), 0)

    def test_receive_funds(self):
        self.wallet.receive_funds(100)
        self.assertEqual(self.wallet.get_balance(), 100)

    def test_send_funds(self):
        self.wallet.receive_funds(100)
        self.wallet.send_funds("recipient_address", 50)
        self.assertEqual(self.wallet.get_balance(), 50)

    def test_insufficient_funds(self):
        with self.assertRaises(Exception):
            self.wallet.send_funds("recipient_address", 100)

if __name__ == '__main__':
    unittest.main()
