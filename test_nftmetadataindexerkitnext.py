# test_nftmetadataindexerkitnext.py
"""
Tests for NftMetadataIndexerKitNext module.
"""

import unittest
from nftmetadataindexerkitnext import NftMetadataIndexerKitNext

class TestNftMetadataIndexerKitNext(unittest.TestCase):
    """Test cases for NftMetadataIndexerKitNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerKitNext()
        self.assertIsInstance(instance, NftMetadataIndexerKitNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerKitNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
