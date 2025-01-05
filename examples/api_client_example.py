import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_balance(self, user_id):
        response = requests.get(f"{self.base_url}/api/v1/wallet/balance", params={"user_id": user_id})
        return response.json()

    def send_transaction(self, sender, recipient, amount):
        response = requests.post(f"{self.base_url}/api/v1/transaction/send", json={
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })
        return response.json()

def main():
    api_client = APIClient(base_url="http://localhost:5000")

    # Get balance
    user_id = "test_user"
    balance = api_client.get_balance(user_id)
    print(f"Balance for {user_id}: {balance}")

    # Send transaction
    transaction_response = api_client.send_transaction(sender=user_id, recipient="recipient_address", amount=50)
    print(f"Transaction response: {transaction_response}")

if __name__ == "__main__":
    main()
