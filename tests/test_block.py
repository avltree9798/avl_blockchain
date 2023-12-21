from avl_blockchain.block import Block
import unittest


class TestBlock(unittest.TestCase):

    def test_block_creation(self):
        """Test if a block is created with the correct attributes."""

        data = "Block Data"
        previous_block = Block(0, "Genesis Block", None)

        block = Block(1, data, previous_block)

        # Check if the block's index is correct
        self.assertEqual(block.index, 1)

        # Check if the block's data is correct
        self.assertEqual(block.data, data)

        # Check if the block's previous is correct
        self.assertIs(block.previous, previous_block)

        # Check if the block's hash is a valid SHA256 hash
        self.assertTrue(len(block.hash), 64)
        self.assertIsInstance(block.hash, str)

    def test_hash_integrity(self):
        """Test if the block's hash changes with different data."""

        previous_block = Block(0, "Genesis Block", None)
        block1 = Block(1, "Block Data 1", previous_block)
        block2 = Block(1, "Block Data 2", previous_block)

        # Check if different data results in different hashes
        self.assertNotEqual(block1.hash, block2.hash)

    def test_str_representation(self):
        """Test the string representation of the block."""

        previous_block = Block(0, "Genesis Block", None)
        block = Block(1, "Block Data", previous_block)

        expected_str = f'{block.index}{block.timestamp}{block.data}{previous_block.hash}'
        self.assertEqual(str(block), expected_str)
