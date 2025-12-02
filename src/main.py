# src/main.py
import asyncio

from mcp.server import Server
from mcp.types import (
    CallToolRequest,          # <-- no *Schema
    ListToolsRequest,         # <-- no *Schema
    InitializedNotification,  # <-- no *Schema
)

# HTTP transport that exists in your installed openmcp
from openmcp.server.transports.streamable_http import StreamableHTTPTransport

# your tools
from .tools.brainstorm import TOOL_DEFS, handle_call



def create_server() -> Server:
    server = Server(
        name="org/brainstorm",
        version="0.2.0",
        capabilities={"tools": {}},
    )

    @server.set_notification_handler(InitializedNotification)
    async def on_init(_params=None) -> None:
        print("[brainstorm] MCP client initialized")

    @server.set_request_handler(ListToolsRequest)
    async def list_tools(_req):
        return {"tools": TOOL_DEFS}

    @server.set_request_handler(CallToolRequest)
    async def call_tool(req):
        # mcp v1.22 uses .params with `name` and optional `arguments`
        name = req.params.name
        args = req.params.arguments or {}
        return await handle_call(name, args)

    return server


async def start_http(port: int = 8080):
    server = create_server()
    transport = StreamableHTTPTransport(port=port)
    await server.connect(transport)
    print(f"[brainstorm] listening on http://localhost:{port}/mcp")


if __name__ == "__main__":
    asyncio.run(start_http())
