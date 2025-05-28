from connection import get_db_cursor
from datetime import date, timedelta

def seed_database():
    with get_db_cursor() as cursor:
        # Clear existing data
        cursor.executescript("""
            DELETE FROM articles;
            DELETE FROM magazine_categories;
            DELETE FROM authors;
            DELETE FROM magazines;
        """)
        
        
        authors = [
            ('Salim Alvi', 'salim@gmail.com', 'Secret agent'),
            ('Steve Harvey', 'steve@gmail.com', 'Ice breaker'),
            ('Atwood Imani', 'atwood@gmail.com', 'Author of the book'),
            ('King Platinum', 'king@gmail.com', 'Early master')
        ]
        cursor.executemany(
            "INSERT INTO authors (name, email, bio) VALUES (?, ?, ?)",
            authors
        )
        
        
        magazines = [
            ('Fashion Weekly', '123-345', 'Fashion', 'quarterly'),
            ('Tech World', '456-789', 'Technology', 'monthly'),
            ('Health Digest', '789-012', 'Health', 'bi-monthly'),
            ('Travel Explorer', '234-567', 'Travel', 'monthly')
        ]
        cursor.executemany(
            """INSERT INTO magazines (title, issn, category, publication_frequency)
            VALUES (?, ?, ?, ?)""",
            magazines
        )
        
        
        categories = [
            (1, 'Fashion'),
            (1, 'Lifestyle'),
            (2, 'Technology'),
            (2, 'Innovation'),
            (3, 'Health'),
            (3, 'Wellness'),
            (4, 'Travel'),
            (4, 'Adventure')
        ]
        cursor.executemany(
            "INSERT INTO magazine_categories (magazine_id, category) VALUES (?, ?)",
            categories
        )
        
        
        articles = [
            ('The Magic Begins', 'Once upon a time...', 1, 1, 'the-magic-begins', 2500, 1, date.today() - timedelta(days=30)),
            ('Scary Night', 'It was a dark night...', 2, 2, 'scary-night', 1800, 1, date.today() - timedelta(days=15)),
            ('Dystopian Future', 'The world had changed...', 3, 3, 'dystopian-future', 3200, 0, None),
            ('The Lost City', 'An ancient city was discovered...', 4, 4, 'the-lost-city', 1500, 1, date.today() - timedelta(days=10))
        ]
        cursor.executemany(
            """INSERT INTO articles 
            (title, content, author_id, magazine_id, slug, word_count, is_published, published_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            articles
        )

if __name__ == '__main__':
    seed_database()
    print("Database seeded successfully!")