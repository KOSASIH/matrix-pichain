class InsuranceContract:
    def __init__(self):
        self.policies = defaultdict(dict)  # user_address -> {'premium': premium_amount, 'coverage': coverage_amount}

    def purchase_policy(self, user_address, premium, coverage):
        self.policies[user_address] = {'premium': premium, 'coverage': coverage}

    def claim(self, user_address):
        if user_address not in self.policies:
            raise Exception("No active policy found.")
        # Logic for processing claims
        return self.policies[user_address]['coverage']

    def __repr```python
__(self):
        return f"InsuranceContract(policies={self.policies})"
