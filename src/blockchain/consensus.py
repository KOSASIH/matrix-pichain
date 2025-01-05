class Consensus:
    def __init__(self, protocol="PoS"):
        self.protocol = protocol

    def validate_block(self, block, blockchain):
        if self.protocol == "PoS":
            return self.validate_pos(block, blockchain)
        elif self.protocol == "DPoS":
            return self.validate_dpos(block, blockchain)
        else:
            raise ValueError("Unsupported consensus protocol")

    def validate_pos(self, block, blockchain):
        # Implement PoS validation logic
        return True  # Placeholder for actual validation logic

    def validate_dpos(self, block, blockchain):
        # Implement DPoS validation logic
        return True  # Placeholder for actual validation logic

    def __repr__(self):
        return f"Consensus(protocol='{self.protocol}')"
