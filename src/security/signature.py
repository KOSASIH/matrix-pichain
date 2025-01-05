from Crypto.Signature import DSS
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256

class Signature:
    def generate_keypair(self):
        key = ECC.generate(curve='P-256')
        return key.export_key(format='PEM'), key.public_key().export_key(format='PEM')

    def sign(self, private_key, message):
        key = ECC.import_key(private_key)
        h = SHA256.new(message.encode())
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(h)
        return signature

    def verify(self, public_key, message, signature):
        key = ECC.import_key(public_key)
        h = SHA256.new(message.encode())
        verifier = DSS.new(key, 'fips-186-3')
        try:
            verifier.verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

    def __repr__(self):
        return "Signature()"
