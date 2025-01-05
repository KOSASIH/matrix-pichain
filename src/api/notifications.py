class Notifications:
    def send_email(self, recipient, subject, message):
        # Logic to send an email (placeholder)
        print(f"Email sent to {recipient}: {subject} - {message}")

    def send_sms(self, recipient, message):
        # Logic to send an SMS (placeholder)
        print(f"SMS sent to {recipient}: {message}")

    def __repr__(self):
        return "Notifications()"
