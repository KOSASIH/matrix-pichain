import unittest
from security.encryption import Encryption
from security.hashing import Hashing
from security.signature import Signature

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.encryption = Encryption()
        self.hashing = Hashing()
        self.signature = Signature()

    def test_aes_encryption(self):
        plaintext = "Hello, World!"
        encrypted = self.encryption.encrypt_aes(plaintext)
        decrypted = self.encryption.decrypt_aes(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_sha256_hashing(self):
        data = "test_data"
        hashed = self.hashing.hash_sha256(data)
        self.assertNotEqual(data, hashed)

    def test_signature_verification(self):
        message = "Sign this message"
        private_key, public_key = self.signature.generate_keys()
        signature = self.signature.sign_message(message, private_key)
        self.assertTrue(self.signature.verify_signature(message, signature, public_key))

if __name__ == '__main__':
    unittest.main()
