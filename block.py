from crypto import Crypto

class Block:
    def __init__(self, index, previous_hash, timestamp, payload, nonce):
        """Initialize a new block"""

        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.payload = payload
        self.nonce = nonce
        self.hash = None

    def calculate_hash(self, hash_fn=Crypto.calculate_hash):
        """Calculate the hash of this block given a hashing function"""

        self.hash = hash_fn(
            self.index, self.previous_hash, self.timestamp, self.payload, self.nonce
        )

    def __eq__(self, other):
        """Equality operator"""

        equal =  self.index == other.index
        equal &= self.previous_hash == other.previous_hash
        equal &= self.timestamp == other.timestamp
        equal &= self.payload == other.payload
        equal &= self.nonce == other.nonce
        equal &= self.hash == other.hash
        return equal
