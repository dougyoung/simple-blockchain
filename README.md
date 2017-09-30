# Simple Blockchain

A simple implementation of a proof-of-work blockchain in Python3 geared towards clarity of concept and simplicity in implementation.

The goal of this project is to serve as an educational tool and reference for learning.

## Getting started

### Dependencies

```
Python 3.6.x
```

### How to run

```bash
# python3 run.py [difficulty]
```

#### Difficulty

Difficulty defines the probability of finding a valid hash for a given block. The smaller the difficulty the more difficult it
is to find a nonce that yields a valid block. This number is static within the system to preserve the simplicity principle.

`difficulty` is an integer or float or a string that evaluates to an integer or float e.g. `1e71 * 5`.

Default is `1e71`. Increase this number if the proof-of-work portion of the program runs slow on your computer.

## Notes

This project represents a single node in a networkless proof-of-work based cryptocurrency system. As such it does not cover various concepts:

1. Peer networking and message passing
2. Best chain detection and replacement
3. More sophisticated consensus rules validation
4. Chain persistence

## More reading

1. [Blockchain](https://en.bitcoin.it/wiki/Block_chain)
2. [Proof-of-work](https://en.bitcoin.it/wiki/Proof_of_work)
3. [Difficulty](https://en.bitcoin.it/wiki/Difficulty)
