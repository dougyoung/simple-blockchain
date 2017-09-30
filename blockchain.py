import sys
import time

from block import Block
from crypto import Crypto

class Blockchain():
    def __init__(self, difficulty=1e70):
        # Blockchain begins with only the genesis block
        # https://en.bitcoin.it/wiki/Genesis_block
        self.blockchain = [self.__class__.get_genesis_block()]

        # Statically defined difficulty measure for simplicity
        # https://en.bitcoin.it/wiki/Difficulty
        self.difficulty = difficulty

    @staticmethod
    def get_genesis_block():
        hash = '82afe91e2a5302c0fb9fd78ec22f57c00566cdd1c7b3c1a81387dc74c6e19da4'
        return Block(0, None, 1506721343, "All journeys begin with a single step", hash, 0)

    @staticmethod
    def valid_block(previous_block, block):
        if previous_block.index + 1 != block.index:
            print("Previous block index was {0} but expected {1}".format(previous_block, block.index - 1))
            return False

        if previous_block.hash != block.previous_hash:
            print("Previous block hash was {0} but expected {1}".format(previous_block.hash, block.previous_hash))
            return False

        if block.calculate_hash() != block.hash:
            print("Calculated block hash {0} not equal to given block hash {1}".format(
                block.calculate_hash(), block.hash
            ))
            return False

        return True

    def add_block(self, block):
        current_tip = self.get_latest_block()
        if self.__class__.valid_block(current_tip, block):
            self.blockchain.append(block)
        else:
            raise ValueError("Received invalid block {0}".format(block.hash))

    def generate_block(self, payload):
        previous_block = self.get_latest_block()
        index = previous_block.index + 1
        previous_hash = previous_block.hash

        for nonce in range(0, sys.maxsize):
            timestamp = int(time.time())
            hash = Crypto.calculate_hash(index, previous_hash, timestamp, payload, nonce)
            if int(hash, 16) < self.difficulty:
                return Block(index, previous_hash, timestamp, payload, nonce, hash)

    def get_latest_block(self):
        return self.blockchain[-1]
