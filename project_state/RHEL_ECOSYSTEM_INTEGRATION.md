# RHEL_ECOSYSTEM_INTEGRATION.md
Last Updated: 2026-06-12

## 1. Executive Summary
Fedora AI OS adopts the RHEL Lightspeed philosophy: decentralization via specialized MCP servers and robust governance, rather than a monolithic agent. Fedora AI OS acts as an Operating Platform (Orchestration/Trust) and explicitly rejects the "Agent Factory" paradigm.

## 2. Repositories Investigated
linux-mcp-server, docs2db*, insights-mcp, goose-proxy, AgentGateway, sysadmin-agents, coreos/ai-helpers.

## 3. Architectural Lessons
RHEL Lightspeed validates that effective AI-in-OS succeeds through specialized services, knowledge systems, and governance layers.

## 4. What Fedora AI OS Adopts
- Knowledge Infrastructure (docs2db architecture).
- Specialist MCP Server patterns (linux-mcp-server diagnostics, service, log management).
- Insights-MCP RBAC/Service Account security adaptions.

## 5. What Fedora AI OS Learns From
- Goose-Proxy identity boundaries and mTLS concept as a reference for secure transport.
- Sysadmin-agents for operational diagnostic heuristics and runbook workflow inspiration.

## 6. What Fedora AI OS Rejects
- Autonomous script execution (without strict Trust/Governance).
- LLM-based security authority (security must remain OS-native/SELinux/RBAC-bound).
- AgentGateway as a current Gateway replacement (keep as potential future Data Plane candidate).

## 7. Impact on Current Architecture
- Shifts Knowledge Infrastructure from an "add-on" to a "First-Class Subsystem."
- Solidifies the MCP Gateway's role as the permanent Control Plane.

## 8. Impact on Future Architecture
- Future data plane flexibility (e.g., AgentGateway) is preserved, but governance ownership remains immutable within Fedora AI OS.

## 9. Open Questions
- Optimal caching strategy for docs2db retrieval flow.
- Federation point between local Fedora AI OS Trust levels and external remote MCP capabilities.
