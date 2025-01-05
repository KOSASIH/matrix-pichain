class TokenContract:
    def __init__(self, initial_supply):
        self.balances = defaultdict(int)  # user_address -> balance
        self.total_supply = initial_supply
        self.balances['contract_owner'] = initial_supply  # Assign initial supply to the contract owner

    def transfer(self, sender, recipient, amount):
        if self.balances[sender] < amount:
            raise Exception("Insufficient balance.")
        self.balances[sender] -= amount
        self.balances[recipient] += amount

    def balance_of(self, user_address):
        return self.balances[user_address]

    def __repr__(self):
        return f"TokenContract(total_supply={self.total_supply}, balances={self.balances})"
