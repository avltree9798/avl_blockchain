import unittest
from avl_blockchain.block import Block
from avl_blockchain.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):

    def test_init(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)
        self.assertEqual(blockchain.chain[0].data, 'genesis block')

    def test_add_block(self):
        blockchain = Blockchain()
        new_block = Block(1, 'Test Block', None)
        blockchain.add_block(new_block)

        self.assertEqual(len(blockchain.chain), 2)
        self.assertEqual(blockchain.chain[1].data, 'Test Block')

    def test_get_latest_block(self):
        blockchain = Blockchain()
        new_block = Block(1, 'Test Block', None)
        blockchain.add_block(new_block)

        self.assertEqual(blockchain.get_latest_block().data, 'Test Block')

    def test_is_valid(self):
        blockchain = Blockchain()
        new_block = Block(1, 'Test Block', None)
        blockchain.add_block(new_block)

        self.assertTrue(blockchain.is_valid())

        # Tampering the chain to test if is_valid detects it
        blockchain.chain[1].data = 'Tampered Data'
        self.assertFalse(blockchain.is_valid())
