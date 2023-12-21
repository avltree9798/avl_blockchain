# AVL Blockchain

## Description
AVL Blockchain is a Python-based blockchain implementation. This project is designed to demonstrate the fundamental principles of blockchain technology in a simple and educational manner.

## Features
- Implementation of a basic blockchain.
- Simple and clear Python codebase.

## Installation
To install AVL Blockchain, you will need Python installed on your system. Then, you can clone this repository and install the required dependencies:

```bash
git clone https://github.com/avltree9798/avl_blockchain.git
cd avl_blockchain
pip install poetry
poetry install
```

## Usage
Here's a quick example of how to create a blockchain and add a block:
```python
from avl_blockchain.block import Block
from avl_blockchain.blockchain import Blockchain

# Create a new blockchain
blockchain = Blockchain()

# Add a new block
blockchain.add_block(Block(1, 'Test Block', None))

# Verify the blockchain
print(blockchain.is_valid())
```
