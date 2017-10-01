import sys
import time

from block import Block

class Blockchain():
    def __init__(self, difficulty=1e71):
        """Initialize a new blockchain"""

        # Blockchain begins with only the genesis block
        # https://en.bitcoin.it/wiki/Genesis_block
        self.blockchain = [self.__class__.get_genesis_block()]

        # Statically defined difficulty measure for simplicity
        # https://en.bitcoin.it/wiki/Difficulty
        self.difficulty = difficulty

    @staticmethod
    def get_genesis_block():
        """Return the genesis block, the first block in the blockchain"""

        genesis_block = Block(0, None, 1506721343, "All journeys begin with a single step", 0)
        genesis_block.calculate_hash()
        return genesis_block

    @staticmethod
    def valid_block(previous_block, block):
        """Test whether a new block is valid given its previous block"""

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
        """Add a new block to the blockchain if it is valid"""

        current_block = self.get_current_block()
        if self.__class__.valid_block(current_block, block):
            self.blockchain.append(block)
        else:
            raise ValueError("Received invalid block {0}".format(block.hash))

    def generate_block(self, payload):
        """Use proof-of-work to generate a new block given a payload"""

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
        """Get the current latest block in the blockchain"""

        return self.blockchain[-1]
