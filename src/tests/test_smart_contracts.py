import unittest
from smart_contracts.token_contract import TokenContract

class TestTokenContract(unittest.TestCase):
    def setUp(self):
        self.token_contract = TokenContract(initial_supply=1000)

    def test_initial_supply(self):
        self.assertEqual(self.token_contract.total_supply, 1000)

    def test_transfer(self):
        self.token_contract.transfer("contract_owner", "recipient_address", 100)
        self.assertEqual(self.token_contract.balance_of("contract_owner"), 900)
        self.assertEqual(self.token_contract.balance_of("recipient_address"), 100)

    def test_insufficient_balance(self):
        with self.assertRaises(Exception):
            self.token_contract.transfer("contract_owner", "recipient_address", 2000)

if __name__ == '__main__':
    unittest.main()
