import sqlite3

class Migrate:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def migrate(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            # Example migration: create a new table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    balance REAL DEFAULT 0
                )
            ''')
            conn.commit()
            print("Migration completed successfully.")

if __name__ == "__main__":
    migrator = Migrate(db_path='path/to/database.db')
    migrator.migrate()
