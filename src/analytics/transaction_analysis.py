class TransactionAnalysis:
    def __init__(self):
        self.transactions = []  # List to store transaction data

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def total_transactions(self):
        return len(self.transactions)

    def total_volume(self):
        return sum(tx['amount'] for tx in self.transactions)

    def average_transaction_value(self):
        if not self.transactions:
            return 0
        return self.total_volume() / self.total_transactions()

    def transaction_distribution(self):
        distribution = {}
        for tx in self.transactions:
            amount = tx['amount']
            if amount not in distribution:
                distribution[amount] = 0
            distribution[amount] += 1
        return distribution

    def __repr__(self):
        return f"TransactionAnalysis(total_transactions={self.total_transactions()}, total_volume={self.total_volume()})"
