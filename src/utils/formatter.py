class Formatter:
    @staticmethod
    def format_currency(amount):
        return f"${amount:,.2f}"

    @staticmethod
    def format_timestamp(timestamp):
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def format_transaction(transaction):
        return f"Transaction from {transaction['sender']} to {transaction['recipient']} of amount {Formatter.format_currency(transaction['amount'])}"

    def __repr__(self):
        return "Formatter()"

# Example usage
if __name__ == "__main__":
    formatter = Formatter()
    print(formatter.format_currency(1234.5678))
