class LendingContract:
    def __init__(self):
        self.loans = defaultdict(dict)  # user_address -> {'amount': loan_amount, 'collateral': collateral_amount}
        self.interest_rate = 0.1  # 10% interest rate

    def lend(self, lender, amount):
        # Logic for lending tokens
        pass

    def borrow(self, borrower, amount, collateral):
        if collateral < amount * 2:  # Require 200% collateral
            raise Exception("Insufficient collateral.")
        self.loans[borrower] = {'amount': amount, 'collateral': collateral}

    def repay(self, borrower):
        # Logic for repaying loans
        pass

    def __repr__(self):
        return f"LendingContract(loans={self.loans})"
