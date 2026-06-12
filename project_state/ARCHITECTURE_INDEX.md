# Fedora AI OS — Architecture & Memory Strategy
Last Updated: 2026-06-12

## 1. Core Architectural Pillars
These remain the foundation and are non-negotiable:
- CEO Agent, Workflow Engine, LangGraph orchestration
- MCP Gateway (as the core proxy and orchestrator, featuring V1 Policy Engine and V2+ Trust Agent)
- Multi-tier Policy & Trust System (V1: Policy Engine, V2+: Trust Agent)
- Recoverable Workflow Runtime (Atomic/Compensation/Suspend-Resume)
- Fedora-native security (SELinux/Podman/systemd)
- Environment Packs, Agent Registry, and Profile Switching

## 2. New Layer: Knowledge Infrastructure
Knowledge Infrastructure is now officially integrated into the architecture as the fifth memory tier, positioned below the MCP Gateway.

**Memory Tier Hierarchy:**
1. Personal (Mem0)
2. Operational (Redis)
3. Graph (FalkorDB/Neo4j)
Knowledge Infrastructure (First-class subsystem, dedicated retrieval layer)
5. Audit (SQLite)

## 3. Revised MCP Gateway & Federation Strategy
The MCP Gateway acts as the control plane for governance (Trust, Capabilities, Approvals). Federation and infrastructure-level concerns (Auth, Retries, Circuit Breakers, Routing) will evaluate AgentGateway as a potential underlying component for these duties, but the Fedora AI OS control plane retains ownership of policy enforcement.

## 4. Specialist Agent Classification
Agents are split into two categories to prevent scope creep:
- **Core Agents (Owned):** CEO, Workflow, Runtime, Memory, Security, Desktop. (Always maintained by Fedora AI OS)
- **Environment Agents (Orchestrated):** Agents installed via packs (Claude Code, Goose, Perplexity, Writing/Research agents, etc.). Fedora AI OS orchestrates these via LangGraph; we do not build them.

## 5. Architectural Flow
```text
CEO Agent
    ↓
Workflow Engine
    ↓
MCP Gateway (Control Plane)
    ↓
Knowledge Infrastructure (docs2db)
    ↓
Specialist MCP Servers / Environment Agents
```
