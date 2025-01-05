import shutil
import os

class Restore:
    def __init__(self, backup_path, db_path):
        self.backup_path = backup_path
        self.db_path = db_path

    def restore_backup(self):
        if os.path.exists(self.db_path):
            shutil.rmtree(self.db_path)  # Remove existing database
        shutil.copytree(self.backup_path, self.db_path)
        print(f"Database restored successfully from {self.backup_path}")

if __name__ == "__main__":
    restore = Restore(backup_path='path/to/backup', db_path='path/to/database.db')
    restore.restore_backup()
