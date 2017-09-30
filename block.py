from crypto import Crypto

class Block():
    def __init__(self, index, previous_hash, timestamp, payload, nonce, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.payload = payload
        self.nonce = nonce
        self.hash = hash

    def calculate_hash(self):
        return Crypto.calculate_hash(self.index, self.previous_hash, self.timestamp, self.payload, self.nonce)
