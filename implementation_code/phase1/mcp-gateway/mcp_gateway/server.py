from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="MCP Gateway Server")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    # This is a stub for Month 1: Core Proxy Routing
    # We will implement JSON-RPC 2.0 parsing here
    return JSONResponse(
        status_code=501, 
        content={"error": "Not Implemented", "detail": "MCP proxy endpoint is under construction"}
    )
