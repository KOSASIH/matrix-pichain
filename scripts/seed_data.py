import sqlite3

class SeedData:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def seed(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            # Example seed data
            cursor.execute("INSERT INTO users (username, balance) VALUES (?, ?)", ("user1", 1000))
            cursor.execute("INSERT INTO users (username, balance) VALUES (?, ?)", ("user2", 2000))
            conn.commit()
            print("Seed data inserted successfully.")

if __name__ == "__main__":
    seeder = SeedData(db_path='path/to/database.db')
    seeder.seed()
