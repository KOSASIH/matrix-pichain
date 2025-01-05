import shutil
import os

class Backup:
    def __init__(self, db_path, backup_path):
        self.db_path = db_path
        self.backup_path = backup_path

    def create_backup(self):
        if os.path.exists(self.backup_path):
            shutil.rmtree(self.backup_path)  # Remove existing backup
        shutil.copytree(self.db_path, self.backup_path)
        print(f"Backup created successfully at {self.backup_path}")

if __name__ == "__main__":
    backup = Backup(db_path='path/to/database.db', backup_path='path/to/backup')
    backup.create_backup()
