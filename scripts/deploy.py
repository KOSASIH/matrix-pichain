from web3 import Web3
import json

class Deploy:
    def __init__(self, contract_path, provider_url):
        self.provider_url = provider_url
        self.web3 = Web3(Web3.HTTPProvider(self.provider_url))
        self.contract_path = contract_path

    def load_contract(self):
        with open(self.contract_path) as f:
            contract_json = json.load(f)
        return contract_json['abi'], contract_json['bytecode']

    def deploy_contract(self, account, private_key):
        abi, bytecode = self.load_contract()
        contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)

        # Build transaction
        transaction = contract.constructor().buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })

        # Sign transaction
        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)

        # Send transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Contract deployed! Transaction hash: {tx_hash.hex()}")

if __name__ == "__main__":
    deployer = Deploy(contract_path='path/to/contract.json', provider_url='https://your.ethereum.node')
    deployer.deploy_contract(account='your_account_address', private_key='your_private_key')
