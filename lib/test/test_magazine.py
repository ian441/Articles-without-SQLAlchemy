import unittest
from lib.models.magazine import Magazine

class TestMagazine(unittest.TestCase):
    """Tests Magazine class initialization"""

    def test_magazine_initialization(self):
        """Tests magazine creation with and without ID"""
        
        mag1 = Magazine("Tech Weekly", "Technology")
        self.assertEqual(mag1.name, "Tech Weekly")
        self.assertEqual(mag1.category, "Technology")
        self.assertIsNone(mag1.id)

        
        mag2 = Magazine("Science Today", "Science", 2)
        self.assertEqual(mag2.name, "Science Today")
        self.assertEqual(mag2.category, "Science")
        self.assertEqual(mag2.id, 2)

if __name__ == '__main__':
    unittest.main()