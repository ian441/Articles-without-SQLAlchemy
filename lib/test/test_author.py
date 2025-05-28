import unittest
from lib.models.author import Author

class TestAuthor(unittest.TestCase):
    """Tests for Author class"""

    def test_author_initialization(self):
        """Test author initialization with and without ID"""
        
        no_id = Author("John Doe")
        self.assertEqual(no_id.name, "John Doe")
        self.assertIsNone(no_id.id)

        
        with_id = Author("Jane Smith", 3)
        self.assertEqual(with_id.name, "Jane Smith")
        self.assertEqual(with_id.id, 3)

if __name__ == '__main__':
    unittest.main()