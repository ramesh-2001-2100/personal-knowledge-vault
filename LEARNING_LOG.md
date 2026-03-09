# Technical Summary: Building the Personal Knowledge Vault

**Chat Title:** *Vibe Coding a Secure Python & SQLite Knowledge Base*
**Date:** March 2026
**Project Status:** Backend v1.1 Complete (CLI Integrated)

---

## 1. Architectural Overview

The project follows a "Thin Slice" development pattern, establishing a functional connection between a Python logic layer and a local SQLite database.

* **Logic Layer:** `vault.py` handles database initialization, CRUD operations, and CLI interaction.
* **Data Layer:** `snippets.db` (SQLite) stores snippets with a schema consisting of `id`, `title`, `content`, and `category`.

---

## 2. Key Technical Concepts Learned

### Database Connections vs. Cursors

* **Connection (`conn`):** The "House" or the active pipe to the database file. Managed via a `with` context manager to ensure the pipe is closed safely.
* **Cursor (`cursor`):** The "Worker" or "Mailman" that executes specific SQL commands and keeps track of where we are in the results.

### Security: SQL Injection Protection

We implemented **Parameterized Queries** to prevent malicious code execution.

* **Positional Style:** Uses `?` as placeholders with a **Tuple**.
* **Named Style:** Uses `:label` as placeholders with a **Dictionary**.
* **Why:** Both styles separate the *Command* (SQL) from the *Data*, ensuring the database treats user input strictly as text.

### Data Structures: Tuples vs. Dictionaries

* **Tuples (Immutable):** Used originally for positional SQL parameters. Safe but rigid (order matters).
* **Dictionaries (Mutable):** Used for the final refactor. They allow for "Named" data access (e.g., `data['title']`), which is more readable and matches the JSON format used in **Next.js**.

---

## 3. Implementation Highlights

### The "Cake and Eat it Too" Pattern

We refactored the `add_snippet` function to achieve both maximum security and high readability using dict inputs:

```python
# Named Placeholder Pattern
query = "INSERT INTO snippets (title) VALUES (:title)"
# Passing a Dictionary directly
conn.execute(query, {"title": "My Snippet"})
```

### The `sqlite3.Row` Factory

By setting `conn.row_factory = sqlite3.Row`, we enabled the ability to treat database rows like Python dictionaries. This prevents "Index Magic" and makes the code self-documenting.

---

## 4. CLI Interaction (New)

We upgraded the script to support command-line arguments using `sys.argv`, allowing for seamless terminal interaction.

* **Capture Arguments:** `sys.argv` extracts words passed after `python vault.py`.
* **Flow Control:** If the first argument is `add`, the script expects Title, Content, and Category. Otherwise, it defaults to listing all contents.
* **Error Handling:** Added checks for missing arguments and empty vault states.

**Add Command:** `python vault.py add "Title" "Content" "Category"`
**List Command:** `python vault.py`

---

## 5. DevOps & SDLC Workflow

* **Environment:** Built in a Windows PowerShell environment, using local Python 3 and SQLite.
* **Verification:** Implemented a terminal-based testing loop to confirm DB persistence after script termination.

---

## 6. Future Roadmap

1. **Search Logic:** Implement `LIKE` operators with `%` wildcards for keyword discovery.
2. **Delete/Update Commands:** Expand the CLI to manage existing snippets.
3. **API Layer:** Wrap the logic in **FastAPI**.
4. **Agentic AI:** Integrate **LangGraph** to allow AI agents to query the vault.
