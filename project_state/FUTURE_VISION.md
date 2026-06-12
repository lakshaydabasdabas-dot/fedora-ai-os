# Fedora AI OS - FUTURE_VISION.md

Last updated: 2026-06-11

## Core Philosophy
Fedora AI OS is a security-first, AI-native orchestration layer built above Fedora Linux. 

## Architectural Concept: Profession-Specific Agentic Environments
Moving forward, our architecture moves beyond simple role-based agents. We are adopting **Profession-Specific Agentic Environments**.

Users do not install individual agents; they install comprehensive environments that include agent configurations, specialized skills, MCP tool mappings, memory templates, workflows, UI presets, and security policies.

### Environment-Specific Customization
An environment provides:
- Agent roles, prompts & configurations
- MCP tool bundles
- Workflow templates
- Context packs & memory schemas
- UI presets & security policies

### Core Roles (Environment Agnostic)
To prevent agent sprawl, we maintain a small, stable set of core agent roles:
- CEO Agent
- Runtime Agent
- Security Agent
- Memory Agent
- Desktop Agent
- Workflow Agent
- Research Agent
- Planning Agent
- Execution Agent

Environments supply the *data* and *configuration* that customize these agents for specific professional needs.

### Environment Registry & Marketplace
A centralized Registry will allow users to discover, install, and manage these specialized environments. The Marketplace will enable community-driven creation and distribution of environment packs.

### Multi-Environment Support
The architecture natively supports the concurrent installation of multiple environments (e.g., "Developer + Student" or "Finance + Sales"), merging capabilities and policies into a unified, secure cognitive workspace.
