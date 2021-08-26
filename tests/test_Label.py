import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.label import label

class TestLabel(unittest.TestCase):
    def test_label(self):
        """
        Test that label is encoded
        """
        result = label('M'),label('B')
        self.assertEqual(result, (1,0))

if __name__ == '__main__':
    unittest.main()
