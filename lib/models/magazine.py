from lib.db.connection import get_connection
from contextlib import closing

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        """Save the magazine to the database"""
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute("""
                    UPDATE magazines SET name=?, category=? 
                    WHERE id=?
                """, (self.name, self.category, self.id))
            else:
                cursor.execute("""
                    INSERT INTO magazines (name, category) 
                    VALUES (?, ?)
                """, (self.name, self.category))
                self.id = cursor.lastrowid
            conn.commit()
        return self

    @classmethod
    def create(cls, name, category):
        """Create and save a new magazine"""
        return cls(name, category).save()

    @classmethod
    def _fetch_magazine(cls, query, params=()):
        """Helper to fetch a single magazine"""
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()
            return cls(row['name'], row['category'], row['id']) if row else None

    @classmethod
    def _fetch_magazines(cls, query, params=()):
        """Helper to fetch multiple magazines"""
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [cls(row['name'], row['category'], row['id']) 
                   for row in cursor.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        """Find magazine by ID"""
        return cls._fetch_magazine("SELECT * FROM magazines WHERE id=?", (id,))

    @classmethod
    def find_by_name(cls, name):
        """Find magazine by name"""
        return cls._fetch_magazine("SELECT * FROM magazines WHERE name=?", (name,))

    @classmethod
    def all(cls):
        """Get all magazines"""
        return cls._fetch_magazines("SELECT * FROM magazines")

    def delete(self):
        """Delete the magazine"""
        if not self.id:
            return False
            
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM magazines WHERE id=?", (self.id,))
            conn.commit()
        self.id = None
        return True

    def _fetch_related(self, query, params=()):
        """Helper for related records"""
        with closing(get_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def articles(self):
        """Get all articles in this magazine"""
        from lib.models.article import Article
        if not self.id:
            return []
        return [Article.find_by_id(row['id']) 
               for row in self._fetch_related(
                   "SELECT id FROM articles WHERE magazine_id=?", 
                   (self.id,))]

    def contributors(self):
        """Get all authors who wrote for this magazine"""
        from lib.models.author import Author
        if not self.id:
            return []
        return [Author.find_by_id(row['author_id']) 
               for row in self._fetch_related(
                   "SELECT DISTINCT author_id FROM articles WHERE magazine_id=?", 
                   (self.id,))]

    def article_titles(self):
        """Get all article titles in this magazine"""
        if not self.id:
            return []
        return [row['title'] for row in self._fetch_related(
            "SELECT title FROM articles WHERE magazine_id=?", 
            (self.id,))]

    def contributing_authors(self):
        """Get authors with >2 articles in this magazine"""
        from lib.models.author import Author
        if not self.id:
            return []
        return [Author.find_by_id(row['author_id']) 
               for row in self._fetch_related(
                   """SELECT author_id FROM articles 
                   WHERE magazine_id=? 
                   GROUP BY author_id HAVING COUNT(id) > 2""", 
                   (self.id,))]