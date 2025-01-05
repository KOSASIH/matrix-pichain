class MultiSigWallet:
    def __init__(self, required_signatures, owners):
        self.required_signatures = required_signatures
        self.owners = owners
        self.transactions = []
        self.pending_transactions = {}

    def create_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "signatures": []
        }
        self.transactions.append(transaction)
        self.pending_transactions[transaction] = []
        return transaction

    def sign_transaction(self, transaction, owner):
        if owner not in self.owners:
            raise Exception("Owner not authorized.")
        if transaction not in self.pending_transactions:
            raise Exception("Transaction not found.")
        if owner in self.pending_transactions[transaction]:
            raise Exception("Transaction already signed by this owner.")
        
        self.pending_transactions[transaction].append(owner)
        transaction["signatures"].append(owner)

        if len(self.pending_transactions[transaction]) >= self.required_signatures:
            self.execute_transaction(transaction)

    def execute_transaction(self, transaction):
        # Logic to execute the transaction
        print(f"Transaction executed: {transaction}")
        del self.pending_transactions[transaction]

    def __repr__(self):
        return f"MultiSigWallet(required_signatures={self.required_signatures}, owners={self.owners})"
