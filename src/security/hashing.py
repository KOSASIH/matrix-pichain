import hashlib

class Hashing:
    def sha256(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def blake2(self, data):
        return hashlib.blake2b(data.encode()).hexdigest()

    def __repr__(self):
        return "Hashing()"
