import sqlite3

def setup_db():
    with open('lib/db/schema.sql') as f:
        schema_sql = f.read()

    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database schema created!")

if __name__ == "__main__":
    setup_db()