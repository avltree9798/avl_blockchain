from avl_blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self):
        return Block(0, 'genesis block', None)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block: Block):
        block.previous = self.get_latest_block()
        block.hash = block.get_hash()
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i-1]
            current_block = self.chain[i]
            if current_block.hash != current_block.get_hash():
                return False
            if current_block.previous.hash != previous_block.hash:
                return False
        return True
