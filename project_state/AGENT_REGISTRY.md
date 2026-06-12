# Fedora AI OS - AGENT_REGISTRY.md

Last updated: 2026-06-11

## Registry Model

The Agent Registry tracks two distinct types of entities:

### 1. Core Agent Registry
Tracks foundational framework roles.

### 2. Environment Registry
Tracks professional environment bundles.

| Environment | Supported Agents | Focus |
|-------------|------------------|-------|
| Developer | Coding, Debug, Doc, Test | Software Dev |
| Student | Planning, Notes, Assignment | Study/Learning |
| Research | Lit Review, Citation | Academic |
| Content Creator| Scripting, SEO | Media |
| Cybersecurity | Threat, Vulnerability | SecOps |
| SysAdmin | Monitoring, Deployment | DevOps |
| AI Engineer | RAG, Prompting, Evaluation | ML Ops |

## Installation Model
- Install: Registry fetches environment bundle (skills, prompts, tool bundles).
- Activation: Agent Kernel applies bundles to Core Roles.
- Merging: Multiple activated environments result in flattened capability/policy sets.
