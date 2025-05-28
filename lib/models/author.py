from lib.db.connection import get_connection
from lib.models.article import Article

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        """Save the author to the database"""
        with get_connection() as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute("UPDATE authors SET name=? WHERE id=?", (self.name, self.id))
            else:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
                self.id = cursor.lastrowid
            conn.commit()

    @classmethod
    def _fetch_author(cls, query, params=()):
        """Helper method to fetch a single author"""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            row = cursor.fetchone()
            return cls(row['name'], row['id']) if row else None

    @classmethod
    def _fetch_authors(cls, query, params=()):
        """Helper method to fetch multiple authors"""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [cls(row['name'], row['id']) for row in cursor.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        """Find an author by ID"""
        return cls._fetch_author("SELECT * FROM authors WHERE id=?", (id,))

    @classmethod
    def find_by_name(cls, name):
        """Find an author by name"""
        return cls._fetch_author("SELECT * FROM authors WHERE name=?", (name,))

    @classmethod
    def all(cls):
        """Get all authors"""
        return cls._fetch_authors("SELECT * FROM authors")

    @classmethod
    def count(cls):
        """Count all authors"""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM authors")
            return cursor.fetchone()[0]

    def _fetch_related(self, query, params=()):
        """Helper method for related records"""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def articles(self):
        """Get all articles by this author"""
        return self._fetch_related("SELECT * FROM articles WHERE author_id=?", (self.id,))

    def magazines(self):
        """Get all magazines this author wrote for"""
        return self._fetch_related("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id=?
        """, (self.id,))

    def add_article(self, magazine_id, title):
        """Create a new article for this author"""
        return Article(title, self.id, magazine_id).save()

    def topic_areas(self):
        """Get unique magazine categories for this author"""
        categories = self._fetch_related("""
            SELECT DISTINCT category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id=?
        """, (self.id,))
        return [row['category'] for row in categories]