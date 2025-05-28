import sqlite3
from contextlib import contextmanager

DATABASE = 'articles.db'

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('DATABASE')
    conn.row_factory = sqlite3.Row # This enables column access by name
    try:
        yield conn
    finally:
        conn.close()
        
@contextmanager
def get_db_cursor():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except:
            conn.rollback()
            raise