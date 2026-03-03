# Personal Knowledge Vault

A lightweight, local-first storage system for technical snippets and learning notes. This project is built with a focus on clean, secure database patterns and is designed to be easily extensible for AI-agent integration (e.g., LangGraph or CrewAI).

## 🚀 Features

- **SQLite Backend**: Zero-dependency local storage.
- **Dictionary-Based Operations**: Uses Python dictionaries and named SQL placeholders to prevent SQL injection and ensure code readability.
- **Context Management**: Robust database connection handling using Python context managers.
- **Categorized Snippets**: Organize learning by tags like `Kubernetes`, `Python`, or `AI`.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Database**: SQLite3 (Built-in)
- **Environment**: Windows PowerShell optimized

## 📂 Project Structure

- `vault.py`: Core logic for database initialization and CRUD operations.
- `snippets.db`: Local SQLite database (ignored by git).
- `implementation_plan.md`: Architectural roadmap for the project.

## 🚦 Getting Started

### 1. Initialize and Test
Run the vault script directly to set up the database and add sample data:

```powershell
python vault.py
```

### 2. Integration Example
You can import the vault logic into other Python scripts:

```python
from vault import add_snippet, get_all_snippets

# Add a new snippet
add_snippet({
    "title": "K8s Service",
    "content": "Type: LoadBalancer exposes the service externally.",
    "category": "Kubernetes"
})

# List all snippets
for s in get_all_snippets():
    print(f"[{s['category']}] {s['title']}")
```

## 📝 Future Roadmap

- [ ] Search functionality by title/category.
- [ ] CLI interface for quick snippet capture.
- [ ] Integration with LangGraph for agentic knowledge retrieval.
- [ ] Export snippets to Obsidian-ready Markdown files.
