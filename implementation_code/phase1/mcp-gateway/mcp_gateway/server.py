from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="MCP Gateway Server")

# Load config on startup
from mcp_gateway.config import load_config
try:
    backends = load_config("config.yaml")
    print(f"Loaded {len(backends)} backends from config.")
except Exception as e:
    print(f"Warning during startup: {e}")

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
