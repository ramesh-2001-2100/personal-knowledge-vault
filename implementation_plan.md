# Personal Knowledge Vault Implementation Plan

A Python-based storage system for "Learning Snippets" using a local SQLite database.

## Proposed Changes

### Logic Tier

#### [NEW] [vault.py](file:///c:/Users/lrame/code/personal_knowledge_vault/vault.py)
This file will contain the core logic for managing snippets.

- **Storage**: Use `sqlite3` to connect to `snippets.db`.
- **Initialization**: Create a `snippets` table if it doesn't exist (columns: `id`, `title`, `content`, `category`).
- **`add_snippet(title: str, content: str, category: str) -> None`**: 
    - Inserts a new row into the `snippets` table.
- **`get_all_snippets() -> list[dict]`**:
    - Executes a `SELECT *` query.
    - Maps rows to a list of dictionaries for easier handling in Python.

## Verification Plan

### Manual Verification
- I will include a self-test block to:
    1. Initialize the DB.
    2. Add sample snippets.
    3. Retrieve and print all snippets.
- Terminal Command:
    ```powershell
    python vault.py
    ```
