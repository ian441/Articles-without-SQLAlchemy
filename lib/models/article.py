from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        """Save the article to the database"""
        with get_connection() as conn:
            cursor = conn.cursor()
            
            if self.id:
                cursor.execute("""
                    UPDATE articles SET title=?, author_id=?, magazine_id=? 
                    WHERE id=?
                """, (self.title, self.author_id, self.magazine_id, self.id))
            else:
                cursor.execute("""
                    INSERT INTO articles (title, author_id, magazine_id) 
                    VALUES (?, ?, ?)
                """, (self.title, self.author_id, self.magazine_id))
                self.id = cursor.lastrowid
                
            conn.commit()
        return self

    @classmethod
    def _fetch_articles(cls, query, params=()):
        """Helper method to fetch articles"""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [cls(row['title'], row['author_id'], row['magazine_id'], row['id']) 
                    for row in cursor.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        """Find an article by its ID"""
        articles = cls._fetch_articles("SELECT * FROM articles WHERE id=?", (id,))
        return articles[0] if articles else None

    @classmethod
    def find_by_title(cls, title):
        """Find articles by title"""
        return cls._fetch_articles("SELECT * FROM articles WHERE title=?", (title,))
    
    @classmethod
    def all(cls):
        """Get all articles from the database"""
        return cls._fetch_articles("SELECT * FROM articles")

    def author(self):
        """Get the author of this article"""
        from lib.models.author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        """Get the magazine this article was published in"""
        from lib.models.magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)