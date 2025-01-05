from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

class Encryption:
    def __init__(self):
        self.aes_key = get_random_bytes(32)  # AES-256 key

    def encrypt_aes(self, plaintext):
        cipher = AES.new(self.aes_key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt_aes(self, encrypted):
        data = base64.b64decode(encrypted.encode())
        nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
        cipher = AES.new(self.aes_key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()

    def generate_rsa_keypair(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    def encrypt_rsa(self, public_key, plaintext):
        rsa_key = RSA.import_key(public_key)
        ciphertext = rsa_key.encrypt(plaintext.encode(), None)[0]
        return base64.b64encode(ciphertext).decode()

    def decrypt_rsa(self, private_key, encrypted):
        rsa_key = RSA.import_key(private_key)
        ciphertext = base64.b64decode(encrypted.encode())
        return rsa_key.decrypt(ciphertext).decode()

    def __repr__(self):
        return "Encryption()"
