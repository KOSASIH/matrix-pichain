import unittest
import json
from api.v1.endpoints import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_balance(self):
        response = self.app.get('/api/v1/wallet/balance?user_id=test_user')
        self.assertEqual(response.status_code, 200)
        self.assertIn('balance', json.loads(response.data))

    def test_send_transaction(self):
        response = self.app.post('/api/v1/transaction/send', json={
            'sender': 'test_user',
            'recipient': 'recipient_address',
            'amount': 50
        })
        self.assertEqual(response.status_code, 201)

    def test_rate_limit(self):
        for _ in range(70):  # Assuming the limit is 60 requests per minute
            self.app.get('/api/v1/wallet/balance?user_id=test_user')
        response = self.app.get('/api/v1/wallet/balance?user_id=test_user')
        self.assertEqual(response.status_code, 429)

if __name__ == '__main__':
    unittest.main()
