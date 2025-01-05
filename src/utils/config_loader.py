import json
import os

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __repr__(self):
        return f"ConfigLoader(config_file={self.config_file})"

# Example usage
if __name__ == "__main__":
    config_loader = ConfigLoader()
    print(config_loader.get("some_key", "default_value"))
