# Technical Summary: Building the Personal Knowledge Vault

**Chat Title:** *Vibe Coding a Secure Python & SQLite Knowledge Base*
**Date:** March 2026
**Project Status:** Backend v1.0 Complete & Pushed to GitHub

---

## 1. Architectural Overview

The project follows a "Thin Slice" development pattern, establishing a functional connection between a Python logic layer and a local SQLite database.

* **Logic Layer:** `vault.py` handles database initialization and CRUD (Create, Read, Update, Delete) operations.
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

We refactored the `add_snippet` function to achieve both maximum security and high readability:

```python
# Named Placeholder Pattern
query = "INSERT INTO snippets (title) VALUES (:title)"
# Passing a Dictionary directly
conn.execute(query, {"title": "My Snippet"})

```

### The `sqlite3.Row` Factory

By setting `conn.row_factory = sqlite3.Row`, we enabled the ability to treat database rows like Python dictionaries. This prevents "Index Magic" (where you have to remember that `row[2]` is the category) and makes the code self-documenting.

---

## 4. DevOps & SDLC Workflow

* **Version Control:** Initialized `git` with a specific focus on the `.gitignore` file to protect the database (`*.db`) and environment files.
* **Branching:** Used `git init -b main` to align with modern GitHub standards.
* **Documentation:** Created an AI-augmented `README.md` to serve as a professional landing page for the repository.

---

## 5. Future Roadmap

1. **Search Logic:** Implement `LIKE` operators with `%` wildcards for keyword discovery.
2. **API Layer:** Wrap the logic in **FastAPI** to serve data to the web.
3. **Frontend:** Build a **Next.js 15** dashboard to visualize the snippets.
4. **Agentic AI:** Integrate **LangGraph** to allow AI agents to query the vault as a "tool."

