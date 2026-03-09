import sqlite3
import sys  # Required to read terminal arguments
import os

# Database configuration
DB_NAME = 'snippets.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    # Allows accessing columns by name (e.g., row['title'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema."""
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

def add_snippet(snippet_data: dict):
    """Adds a new learning snippet using a dictionary with named placeholders."""
    query = '''
        INSERT INTO snippets (title, content, category) 
        VALUES (:title, :content, :category)
    '''
    with get_db_connection() as conn:
        conn.execute(query, snippet_data)
        conn.commit()
    print(f"✅ Snippet added: {snippet_data.get('title')}")

def get_all_snippets() -> list[dict]:
    """Fetches all snippets from the database."""
    with get_db_connection() as conn:
        rows = conn.execute('SELECT id, title, content, category FROM snippets').fetchall()
        return [dict(row) for row in rows]

# --- CLI INTERFACE ---
if __name__ == "__main__":
    init_db()

    # sys.argv captures arguments passed from the terminal
    args = sys.argv

    # Check for 'add' command
    if len(args) > 1 and args[1] == "add":
        # Expecting: vault.py add "Title" "Content" "Category"
        if len(args) > 4:
            new_snippet = {
                "title": args[2],
                "content": args[3],
                "category": args[4]
            }
            add_snippet(new_snippet)
        else:
            print("❌ Error: Missing information.")
            print("Usage: python vault.py add \"Title\" \"Content\" \"Category\"")
    
    else:
        # Default behavior: List all snippets
        snippets = get_all_snippets()
        if not snippets:
            print("\n📭 The vault is currently empty. Add your first snippet!")
            print("Usage: python vault.py add \"Title\" \"Content\" \"Category\"")
        else:
            print(f"\n--- Current Vault Contents ({len(snippets)} snippets) ---")
            for s in snippets:
                print(f"[{s['category']}] {s['id']}: {s['title']}")
                print(f"   {s['content']}\n")
