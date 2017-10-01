import hashlib

class Crypto:
    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, payload, nonce):
        """Calculate a hash.

        To mimic Bitcoin's block header hash we do double SHA256
        Reference: https://en.bitcoin.it/wiki/Block_hashing_algorithm

        Keyword arguments:

        index - The height of the block
        previous_hash - A hash reference to teh previous block
        timestamp - An integer representation of Unix epoch time
        payload - A string representing the block's payload
        nonce - A positive integer representing the nonce
        """

        hash = [str(v) for v in locals().values()]
        hash = hashlib.sha256(''.join(hash).encode()).hexdigest()
        hash = hashlib.sha256(hash.encode()).hexdigest()
        return hash
