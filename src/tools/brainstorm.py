# src/tools/brainstorm.py
from typing import Any, Dict, List
from src.memory import Memory


memory = Memory()

# What MCP clients see when they ask for your tools
TOOL_DEFS: List[Dict[str, Any]] = [
    {
        "name": "brainstorm.add",
        "description": "Add an idea under a topic",
        "inputSchema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "idea": {"type": "string"},
            },
            "required": ["topic", "idea"],
        },
    },
    {
        "name": "brainstorm.list",
        "description": "List ideas for a topic",
        "inputSchema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
            },
            "required": ["topic"],
        },
    },
]

async def handle_call(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if name == "brainstorm.add":
        topic = arguments.get("topic")
        idea = arguments.get("idea")
        if not topic or not idea:
            return {"error": "Both 'topic' and 'idea' are required."}
        memory.add_idea(topic, idea)
        return {"ok": True, "message": f"Added idea to '{topic}'."}

    if name == "brainstorm.list":
        topic = arguments.get("topic")
        if not topic:
            return {"error": "'topic' is required."}
        return {"ok": True, "ideas": memory.get_ideas(topic)}

    return {"error": f"Unknown tool '{name}'"}
