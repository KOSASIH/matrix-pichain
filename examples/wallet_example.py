from wallet.wallet import Wallet

def main():
    # Create a new wallet
    wallet = Wallet("MyTestWallet")
    wallet.create_wallet()

    # Display initial balance
    print(f"Initial Balance: {wallet.get_balance()}")

    # Receive funds
    wallet.receive_funds(100)
    print(f"Balance after receiving funds: {wallet.get_balance()}")

    # Send funds
    try:
        wallet.send_funds("recipient_address", 50)
        print(f"Balance after sending funds: {wallet.get_balance()}")
    except Exception as e:
        print(f"Error sending funds: {e}")

if __name__ == "__main__":
    main()
