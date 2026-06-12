# ENVIRONMENT_PROFILE_ARCHITECTURE_UPDATE

## 1. Executive Summary
This document defines a major architectural shift for Fedora AI OS: moving from a model where the OS builds all its specialist agents, to a model of **Active Orchestration**. Fedora AI OS now focuses on provisioning, securing, managing, and governing modular "Environment Packs" that leverage existing specialist market agents.

## 2. Architectural Changes
- **Shift to Orchestration:** Fedora AI OS provides the runtime, security, memory, and governance to manage third-party specialist agents.
- **Environment Packs:** The primary distribution and configuration unit replaces individual agent installs.
- **Dormant Profile System:** Multiple environments can be installed, but only active ones consume resources.

## 3. First Boot Experience
1. **Model Assignment:** User selects specific models for core system agents (CEO, Memory, Planning, etc.).
2. **Environment Selection:** User chooses one or more "Environment Packs" (e.g., Developer + Content Creator) based on their professional needs.

## 4. Model Selection Architecture
Core Fedora AI OS service roles are assigned dedicated models during setup:
- CEO Agent
- Memory Agent
- Planning Agent
- Runtime Agent
- Security Agent

## 5. Environment Registry Design
The Environment Registry curates bundles of:
- Required/Optional Agents
- Skills, MCP Configurations & Tool Bundles
- Workflow Templates & Memory Schemas
- Permissions & Policy Bundles

## 6. Agent Registry Design
Fedora AI OS maintains a verified, curated Agent Registry, enabling secure, governed access to specialist agents (e.g., Claude Code, Goose, specialized research agents).

## 7. Profile Switching Architecture
- Environments persist as dormant/active status within a user profile.
- Switching profiles toggles agent process lifecycle (Enable/Disable), minimizing resource footprint to only active specialist capabilities.

## 8. Marketplace Evolution
The Marketplace transitions from a single-agent listing to an **Environment-first marketplace**, where users discover and install curated professional workflows.

## 9. Resource Management Strategy
- **Core OS Agents:** Always active, low-footprint (CEO, Runtime, Workflow, Memory, Security, Desktop).
- **Specialist Agents:** Only active when their associated Environment Pack is enabled.

## 10. CEO Agent Changes
- **Provisioning Authority:** Responsible for automating the installation and configuration of Environment Packs and their constituent agent dependencies.
- **Governance:** CEO Agent enforces the "no arbitrary software" rule, installing only verified environment packs from the curated registry.

## 11. Files Updated/Created
- Updated: CURRENT_STATE.md, ROADMAP.md, FUTURE_VISION.md, ARCHITECTURE.md, MARKETPLACE.md, CEO_AGENT.md, PROJECT_STATE.md (meta).
- Created: ENVIRONMENT_REGISTRY.md.

## 12. Roadmap Impact
- Long-term vision adjusted to prioritize the Environment Registry and Environment Pack lifecycle before broader marketplace federation.
- Core critical path (MCP Gateway, Runtime) remains strictly prioritized.
