import time

from block import Block
from crypto import Crypto

class Blockchain():
    def __init__(self):
        self.blockchain = [self.__class__.get_genesis_block()]

    @staticmethod
    def get_genesis_block():
        hash = '37c83e9263e5f292ee53fdf55b47de26bc372086cf2f9bb8d7f1f6ab594c5202'
        return Block(0, '0', 1506721343, "All journeys begin with a single step", hash)

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
        timestamp = int(time.time())
        hash = Crypto.calculate_hash(index, previous_hash, timestamp, payload)
        return Block(index, previous_hash, timestamp, payload, hash)

    def get_latest_block(self):
        return self.blockchain[-1]
