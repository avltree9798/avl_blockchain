from avl_blockchain.block import Block
from avl_blockchain.blockchain import Blockchain

blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.add_block(Block(1, "Transaction Data 1", ""))
blockchain.add_block(Block(2, "Transaction Data 2", ""))
blockchain.add_block(Block(3, "Transaction Data 3", ""))

# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash if block.previous_hash else '0')
    print("\n")
print(blockchain.is_valid())
