import time
import unittest

class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.now_timestamp = int(time.time())

    def test_crypto_calculate_hash(self):
        from crypto import Crypto

        hash = Crypto.calculate_hash(0, None, self.now_timestamp, 'payload', 0)

        # Return value is not empty
        self.assertGreater(len(hash), 0)

        # Return value has 64 characters
        self.assertEqual(len(hash), 64)

        # Return value always equals itself when method is called with same arguments
        self.assertEqual(hash, Crypto.calculate_hash(0, None, self.now_timestamp, 'payload', 0))

        # Any difference in method arguments will return a unique hash
        self.assertNotEqual(hash, Crypto.calculate_hash(1, None, self.now_timestamp, 'payload', 0))
        self.assertNotEqual(hash, Crypto.calculate_hash(0, 'some', self.now_timestamp, 'payload', 0))
        self.assertNotEqual(hash, Crypto.calculate_hash(0, None, self.now_timestamp + 1, 'payload', 0))
        self.assertNotEqual(hash, Crypto.calculate_hash(0, None, self.now_timestamp, 'different payload', 0))
        self.assertNotEqual(hash, Crypto.calculate_hash(0, None, self.now_timestamp, 'payload', 1))

        # Return value is a hex string convertible to a positive integer in base 10
        self.assertGreater(int(hash, 16), 0)

class BlockTest(unittest.TestCase):
    def setUp(self):
        self.now_timestamp = int(time.time())

    def test_block_calculate_hash(self):
        from block import Block

        block = Block(0, None, self.now_timestamp, 'payload', 0)

        # Block hash must be calculated before it is available
        self.assertIsNone(block.hash)

        # Calculate block hash
        block.calculate_hash()

        # Block hash is not empty
        self.assertGreater(len(block.hash), 0)

        block_two = Block(1, block.hash, self.now_timestamp, 'payload', 0)
        block_two.calculate_hash()

        # Block two hash is not equal to block one hash
        self.assertNotEqual(block_two.hash, block.hash)

class BlockchainTest(unittest.TestCase):
    def setUp(self):
        self.now_timestamp = int(time.time())
        self.time_fn = time.time
        time.time = lambda: self.now_timestamp

    def tearDown(self):
        time.time = self.time_fn

    def test_blockchain(self):
        from block import Block
        from blockchain import Blockchain

        # Initialize blockchain
        blockchain = Blockchain(difficulty=1e73)

        # Blockchain always starts with the genesis block
        self.assertEqual(len(blockchain.blockchain), 1)

        genesis_block = blockchain.get_genesis_block()

        # Genesis block is valid
        self.assertIsNotNone(genesis_block)
        self.assertIsInstance(genesis_block, Block)

        # Genesis block is first block
        self.assertEqual(genesis_block, blockchain.get_current_block())

        # Construct the next block after the genesis block
        next_block = Block(
            genesis_block.index + 1,
            genesis_block.hash,
            self.now_timestamp,
            'next block payload',
            0
        )

        # Calculate hash for next block
        next_block.calculate_hash()

        # Next block was designed to be valid
        self.assertTrue(Blockchain.valid_block(genesis_block, next_block))

        # Chain must move forward
        self.assertFalse(Blockchain.valid_block(next_block, genesis_block))

        # Construct an intentionally invalid block by bad index
        invalid_next_block = Block(0, genesis_block.hash, self.now_timestamp, 'next block payload', 0)

        # Next block's index must be greater than previous block's index
        self.assertFalse(Blockchain.valid_block(genesis_block, invalid_next_block))

        # Construct an intentionally invalid block by bad previous hash
        invalid_next_block = Block(
            genesis_block.index + 1,
            genesis_block.hash + '0',
            self.now_timestamp,
            'next block payload',
            0
        )

        # Next block's previous hash much match previous block's hash
        self.assertFalse(Blockchain.valid_block(genesis_block, invalid_next_block))

        # Generate next block and add to blockchain n times
        for i in range(0, 10):
            # Get current block
            current_block = blockchain.get_current_block()

            # Construct payload
            payload = 'block payload {0}'.format(i)

            # Generate next block using proof-of-work
            next_block = blockchain.generate_block(payload)

            # Next block should be valid
            self.assertTrue(Blockchain.valid_block(current_block, next_block))

            # Next block equals another block generated with same payload
            self.assertEqual(next_block, blockchain.generate_block(payload))

            # A different block would be generated with a different payload
            self.assertNotEqual(next_block, blockchain.generate_block('different block payload'))

            # Add the generated block to the chain
            blockchain.add_block(next_block)

            # Next block is now the current block
            self.assertIs(next_block, blockchain.get_current_block())

if __name__ == '__main__':
    unittest.main()
