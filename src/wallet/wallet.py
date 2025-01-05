import json
from collections import defaultdict
from key_management import KeyManagement
from transaction_history import TransactionHistory

class Wallet:
    def __init__(self, wallet_name):
        self.wallet_name = wallet_name
        self.key_manager = KeyManagement()
        self.transaction_history = TransactionHistory()
        self.balance = 0.0  # Initial balance

    def create_wallet(self):
        private_key, public_key = self.key_manager.generate_key_pair()
        self.private_key = private_key
        self.public_key = public_key
        print(f"Wallet created: {self.wallet_name} with public key: {self.public_key}")

    def send_funds(self, recipient, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance.")
        self.balance -= amount
        self.transaction_history.add_transaction(self.public_key, recipient, amount)
        print(f"Sent {amount} to {recipient}. New balance: {self.balance}")

    def receive_funds(self, amount):
        self.balance += amount
        self.transaction_history.add_transaction("System", self.public_key, amount)
        print(f"Received {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history.get_history()

    def __repr__(self):
        return f"Wallet(name={self.wallet_name}, balance={self.balance})"
