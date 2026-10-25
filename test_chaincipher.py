# test_chaincipher.py
"""
Tests for ChainCipher module.
"""

import unittest
from chaincipher import ChainCipher

class TestChainCipher(unittest.TestCase):
    """Test cases for ChainCipher class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainCipher()
        self.assertIsInstance(instance, ChainCipher)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainCipher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
