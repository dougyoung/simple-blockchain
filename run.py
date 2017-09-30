import random
import string
import time

from blockchain import Blockchain
from datetime import datetime

if __name__ == "__main__":
    blockchain = Blockchain()

    if len(blockchain.blockchain) != 1:
        message = "Found {0} blocks in chain, expected only genesis block".format(len(blockchain.blockchain))
        raise SystemError(message)

    while True:
        payload = ''.join(random.choices(string.ascii_letters, k=random.randrange(10, 30)))

        print("Committing {0} to the blockchain".format(payload))

        block = blockchain.generate_block(payload)

        print("Generated new block {0} {1} {2} {3} {4}".format(
            block.index,
            block.previous_hash,
            block.timestamp,
            block.payload,
            block.hash
        ))

        blockchain.add_block(block)

        print("UpdateTip: new best={0} height={1} date='{2}'".format(
            block.hash,
            block.index,
            datetime.utcfromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        ))
        
        time.sleep(10)
