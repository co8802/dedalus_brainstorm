from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from .tools.brainstorm import TOOL_DEFS, handle_call

app = FastAPI(title="Brainstorm Test API")

class CallReq(BaseModel):
    name: str
    arguments: Dict[str, Any] = {}

@app.get("/tools")
def tools():
    return {"tools": TOOL_DEFS}

@app.post("/call")
async def call(req: CallReq):
    return await handle_call(req.name, req.arguments)
