import hashlib

class Crypto():
    # Calculate the hash given:
    # 1. Block index
    # 2. Previous block's hash
    # 3. Timestamp for the block
    # 4. Payload to be included in the block (this would include transactions)
    #       -- In Bitcoin this would be the Merkle Tree Root hash
    # 5. Nonce is an integer incremented with each iteration until a valid hash is found
    # To mimic Bitcoin's block header hash we do double SHA256
    # Reference: https://en.bitcoin.it/wiki/Block_hashing_algorithm
    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, payload, nonce):
        hash = [str(v) for v in locals().values()]
        hash = hashlib.sha256(''.join(hash).encode()).hexdigest()
        hash = hashlib.sha256(hash.encode()).hexdigest()
        return hash
