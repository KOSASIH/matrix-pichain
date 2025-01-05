class HardwareWallet:
    def __init__(self, device):
        self.device = device

    def connect(self):
        # Logic to connect to the hardware wallet
        print(f"Connected to hardware wallet: {self.device}")

    def get_public_key(self):
        # Logic to retrieve the public key from the hardware wallet
        return "public_key_from_hardware_wallet"

    def sign_transaction(self, transaction):
        # Logic to sign a transaction using the hardware wallet
        print(f"Transaction signed: {transaction}")

    def disconnect(self):
        # Logic to safely disconnect from the hardware wallet
        print(f"Disconnected from hardware wallet: {self.device}")

    def __repr__(self):
        return f"HardwareWallet(device={self.device})"
