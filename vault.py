import sqlite3
import os

# Database configuration
DB_NAME = 'snippets.db'

def get_db_connection():
    """Establishes a connection to the SQLite database and returns the connection object."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database by creating the snippets table if it doesn't already exist."""
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS snippets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        conn.commit()
    print(f"Database initialized: {DB_NAME}")

def add_snippet(snippet_data: dict):
    """
    Adds a new learning snippet using a dictionary and named placeholders.
    This is highly secure and easy to read.
    """
    # 1. THE NAMED QUERY: Instead of ?, we use labels like :title.
    # This makes the SQL command self-documenting.
    query = '''
        INSERT INTO snippets (title, content, category) 
        VALUES (:title, :content, :category)
    '''
    
    with get_db_connection() as conn:
        # 2. THE MAPPING: We pass the dict directly. 
        # SQLite automatically maps 'title' in the dict to :title in the query.
        conn.execute(query, snippet_data)
        conn.commit()
    
    # Using .get() is a safe way to access dict keys without risking a crash
    print(f"Snippet added: {snippet_data.get('title')}")

def get_all_snippets() -> list[dict]:
    """Fetches all snippets and returns them as a list of dictionaries."""
    with get_db_connection() as conn:
        rows = conn.execute('SELECT id, title, content, category FROM snippets').fetchall()
        return [dict(row) for row in rows]

if __name__ == "__main__":
    init_db()

    # 3. DICTIONARY USAGE: This is how your data will look in Next.js or an API.
    print("\n--- Adding Sample Snippets via Dictionaries ---")
    
    # We can create a list of dictionaries to process
    samples = [
        {
            "title": "Named Style", 
            "content": "Uses :label in SQL for better clarity.", 
            "category": "Python"
        },
        {
            "title": "Dictionary Input", 
            "content": "Passing dicts to execute() is secure and clean.", 
            "category": "Data"
        }
    ]

    for item in samples:
        add_snippet(item)

    print("\n--- Current Vault Contents ---")
    for s in get_all_snippets():
        print(f"[{s['category']}] {s['id']}: {s['title']}")
