# test_quantumlink.py
"""
Tests for QuantumLink module.
"""

import unittest
from quantumlink import QuantumLink

class TestQuantumLink(unittest.TestCase):
    """Test cases for QuantumLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumLink()
        self.assertIsInstance(instance, QuantumLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
