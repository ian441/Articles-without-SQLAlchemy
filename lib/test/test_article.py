import unittest
from lib.models.article import Article

class TestArticle(unittest.TestCase):
    """Tests for Article class"""
    
    def setUp(self):
        """Create test article before each test"""
        self.article = Article("Test Title", 1, 1)
    
    def test_initialization(self):
        """Test article initialization"""
        self.assertEqual(self.article.title, "Test Title")
        self.assertEqual(self.article.author_id, 1)
        self.assertEqual(self.article.magazine_id, 1)
        self.assertIsNone(self.article.id)
        
        
        article_with_id = Article("Test", 1, 1, 5)
        self.assertEqual(article_with_id.id, 5)
    
    def test_property_setters(self):
        """Test property setters"""
        
        self.article.title = "New Title"
        self.assertEqual(self.article.title, "New Title")
        
        
        self.article.author_id = 2
        self.assertEqual(self.article.author_id, 2)
        
        
        self.article.magazine_id = 3
        self.assertEqual(self.article.magazine_id, 3)

if __name__ == '__main__':
    unittest.main()