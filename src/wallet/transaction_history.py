class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": time.time()
        }
        self.history.append(transaction)

    def get_history(self):
        return self.history

    def __repr__(self):
        return f"TransactionHistory(history={self.history})"
