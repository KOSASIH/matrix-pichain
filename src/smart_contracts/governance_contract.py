from collections import defaultdict

class GovernanceContract:
    def __init__(self):
        self.proposals = []
        self.votes = defaultdict(lambda: defaultdict(int))  # proposal_id -> voter -> vote_count
        self.token_holders = set()  # Set of addresses that hold governance tokens

    def add_proposal(self, proposal):
        self.proposals.append(proposal)
        return len(self.proposals) - 1  # Return proposal ID

    def vote(self, proposal_id, voter, support):
        if voter not in self.token_holders:
            raise Exception("Voter must be a token holder.")
        self.votes[proposal_id][voter] = support

    def tally_votes(self, proposal_id):
        total_votes = sum(self.votes[proposal_id].values())
        return total_votes

    def __repr__(self):
        return f"GovernanceContract(proposals={self.proposals})"
