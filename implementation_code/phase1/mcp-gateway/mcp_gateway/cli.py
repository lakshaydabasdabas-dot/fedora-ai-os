import argparse
import uvicorn
import sys
from mcp_gateway.server import app

def serve():
    parser = argparse.ArgumentParser(description="MCP Gateway CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    serve_parser = subparsers.add_parser("serve", help="Start the MCP Gateway server")
    serve_parser.add_parser("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    
    # Simple parsing logic for `gateway serve --port 8000`
    args, unknown = parser.parse_known_args()
    
    if args.command == "serve":
        port = 8000
        if "--port" in unknown:
            port_idx = unknown.index("--port")
            if port_idx + 1 < len(unknown):
                port = int(unknown[port_idx + 1])
                
        print(f"Starting MCP Gateway on port {port}...")
        uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    serve()
