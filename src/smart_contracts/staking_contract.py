class StakingContract:
    def __init__(self):
        self.stakes = defaultdict(int)  # user_address -> staked_amount
        self.reward_rate = 0.05  # 5% annual reward rate

    def stake(self, user_address, amount):
        if amount <= 0:
            raise Exception("Amount must be greater than zero.")
        self.stakes[user_address] += amount

    def unstake(self, user_address, amount):
        if self.stakes[user_address] < amount:
            raise Exception("Insufficient staked amount.")
        self.stakes[user_address] -= amount

    def calculate_rewards(self, user_address):
        staked_amount = self.stakes[user_address]
        return staked_amount * self.reward_rate

    def __repr__(self):
        return f"StakingContract(stakes={self.stakes})"
