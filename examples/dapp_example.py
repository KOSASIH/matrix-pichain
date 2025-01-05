from flask import Flask, request, jsonify
from wallet.wallet import Wallet

app = Flask(__name__)

# In-memory storage for demonstration purposes
wallets = {}

@app.route('/create_wallet', methods=['POST'])
def create_wallet():
    wallet_name = request.json.get('wallet_name')
    wallet = Wallet(wallet_name)
    wallet.create_wallet()
    wallets[wallet_name] = wallet
    return jsonify({"message": "Wallet created", "wallet_name": wallet_name}), 201

@app.route('/wallet/<wallet_name>/balance', methods=['GET'])
def get_balance(wallet_name):
    wallet = wallets.get(wallet_name)
    if wallet:
        return jsonify({"balance": wallet.get_balance()})
    return jsonify({"error": "Wallet not found"}), 404

@app.route('/wallet/<wallet_name>/send', methods=['POST'])
def send_funds(wallet_name):
    wallet = wallets.get(wallet_name)
    if not wallet:
        return jsonify({"error": "Wallet not found"}), 404

    recipient = request.json.get('recipient')
    amount = request.json.get('amount')
    try:
        wallet.send_funds(recipient, amount)
        return jsonify({"message": "Funds sent", "new_balance": wallet.get_balance()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
