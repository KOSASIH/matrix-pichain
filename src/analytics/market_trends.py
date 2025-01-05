class MarketTrends:
    def __init__(self):
        self.price_data = []  # List to store price data

    def add_price_data(self, timestamp, price, volume):
        self.price_data.append({"timestamp": timestamp, "price": price, "volume": volume})

    def average_price(self):
        if not self.price_data:
            return 0
        return sum(data['price'] for data in self.price_data) / len(self.price_data)

    def price_volatility(self):
        if len(self.price_data) < 2:
            return 0
        prices = [data['price'] for data in self.price_data]
        return max(prices) - min(prices)

    def trading_volume(self):
        return sum(data['volume'] for data in self.price_data)

    def __repr__(self):
        return f"MarketTrends(average_price={self.average_price()}, trading_volume={self.trading_volume()})"
