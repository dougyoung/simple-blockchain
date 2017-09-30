import sys
import time

from block import Block

class Blockchain():
    def __init__(self, difficulty=1e71):
        # Blockchain begins with only the genesis block
        # https://en.bitcoin.it/wiki/Genesis_block
        self.blockchain = [self.__class__.get_genesis_block()]

        # Statically defined difficulty measure for simplicity
        # https://en.bitcoin.it/wiki/Difficulty
        self.difficulty = difficulty

    @staticmethod
    def get_genesis_block():
        genesis_block = Block(0, None, 1506721343, "All journeys begin with a single step", 0)
        genesis_block.calculate_hash()
        return genesis_block

    @staticmethod
    def valid_block(previous_block, block):
        if previous_block.index != block.index - 1:
            print("Previous block index was {0} but expected {1}".format(previous_block.index, block.index - 1))
            return False

        if previous_block.hash != block.previous_hash:
            print("Previous block hash was {0} but expected {1}".format(previous_block.hash, block.previous_hash))
            return False

        block_hash = block.hash
        block.calculate_hash()

        if block_hash != block.hash:
            print("Given block hash {0} not equal to re-calculated block hash {1}".format(block_hash, block.hash))
            return False

        return True

    def add_block(self, block):
        current_block = self.get_current_block()
        if self.__class__.valid_block(current_block, block):
            self.blockchain.append(block)
        else:
            raise ValueError("Received invalid block {0}".format(block.hash))

    def generate_block(self, payload):
        previous_block = self.get_current_block()
        index = previous_block.index + 1
        previous_hash = previous_block.hash

        for nonce in range(0, sys.maxsize):
            timestamp = int(time.time())
            block = Block(index, previous_hash, timestamp, payload, nonce)
            block.calculate_hash()
            if int(block.hash, 16) < self.difficulty:
                return block

    def get_current_block(self):
        return self.blockchain[-1]
