from flask import Flask, request, jsonify
from authentication import Authentication
from analytics import Analytics
from rate_limiting import RateLimiter
from transaction_history import TransactionHistory

app = Flask(__name__)
auth = Authentication()
analytics = Analytics()
rate_limiter = RateLimiter()
transaction_history = TransactionHistory()

@app.route('/api/v1/wallet/balance', methods=['GET'])
@rate_limiter.limit_requests
def get_balance():
    user_id = request.args.get('user_id')
    balance = auth.get_user_balance(user_id)
    return jsonify({"balance": balance})

@app.route('/api/v1/transaction/send', methods=['POST'])
@rate_limiter.limit_requests
def send_transaction():
    data = request.json
    sender = data['sender']
    recipient = data['recipient']
    amount = data['amount']
    
    if auth.validate_transaction(sender, recipient, amount):
        transaction_history.add_transaction(sender, recipient, amount)
        return jsonify({"status": "success", "message": "Transaction sent."}), 201
    else:
        return jsonify({"status": "error", "message": "Transaction failed."}), 400

@app.route('/api/v1/analytics/transactions', methods=['GET'])
@rate_limiter.limit_requests
def get_transaction_analytics():
    analytics_data = analytics.get_transaction_data()
    return jsonify(analytics_data)

if __name__ == '__main__':
    app.run(debug=True)
