# KNOWLEDGE_INFRASTRUCTURE.md
Last Updated: 2026-06-12

## 1. Purpose
Knowledge Infrastructure provides a dedicated retrieval layer for system-wide documents, research findings, and audit logs.

## 2. Relationship To Memory
- Personal Memory (Mem0): Ephemeral, user-specific (Who).
- Operational Memory (Redis): Volatile, workflow-specific (State).
- Knowledge Infrastructure (docs2db): Immutable/Persisted, global system knowledge (What/How).

## 3. docs2db Architecture
- Ingestion pipeline (docs2db platform)
- API endpoint (docs2db-api)
- MCP Gateway connection (docs2db-mcp-server)

## 4. Retrieval Flow
Request → MCP Gateway (Governance/Trust) → docs2db-mcp-server → docs2db-api → RAG Engine → Response.

## 5. MCP Integration
Standardized via `knowledge:*` tool namespace exposed through the MCP Gateway.

## 6. Future Extensions
Integration with system-level diagnostic heuristics and runbooks from the RHEL ecosystem.
