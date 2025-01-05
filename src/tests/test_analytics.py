import unittest
from analytics.transaction_analysis import TransactionAnalysis
from analytics.user_behavior import UserBehavior
from analytics.market_trends import MarketTrends

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.transaction_analysis = TransactionAnalysis()
        self.user_behavior = UserBehavior()
        self.market_trends = MarketTrends()

    def test_transaction_analysis(self):
        self.transaction_analysis.add_transaction({'amount': 100})
        self.transaction_analysis.add_transaction({'amount': 200})
        self.assertEqual(self.transaction_analysis.total_transactions(), 2)
        self.assertEqual(self.transaction_analysis.total_volume(), 300)
        self.assertEqual(self.transaction_analysis.average_transaction_value(), 150)

    def test_user_behavior(self):
        self.user_behavior.log_action("user1", "login")
        self.user_behavior.log_action("user1", "logout")
        self.assertEqual(self.user_behavior.user_activity_count("user1"), 2)
        self.assertEqual(self.user_behavior.most_active_users(), [("user1", 2)])

    def test_market_trends(self):
        self.market_trends.add_price_data("2023-01-01", 100, 10)
        self.market_trends.add_price_data("2023-01-02", 150, 20)
        self.assertEqual(self.market_trends.average_price(), 125)
        self.assertEqual(self.market_trends.price_volatility(), 50)
        self.assertEqual(self.market_trends.trading_volume(), 30)

if __name__ == '__main__':
    unittest.main()
