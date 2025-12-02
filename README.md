# Dedalus Brainstorm

Dedalus Brainstorm is a small FastAPI project that lets you collect and organize ideas by topic. 
It started as a simple experiment to show how two “brainstorming” tools could work together inside a lightweight API.

### Features
 Add new ideas under any topic
 List all ideas saved for a topic
 Easy to run locally with FastAPI and Uvicorn
 Simple in-memory storage that can later be extended to a database

### How it works
The app runs a FastAPI server with two routes:
1. `/tools` shows the available brainstorming tools
2. `/call` handles requests to add or list ideas

Behind the scenes, a `Memory` class stores ideas in a dictionary, grouped by topic.

### Run locally
```bash
source .venv/bin/activate
uvicorn src.app:app --reload --port 8001
