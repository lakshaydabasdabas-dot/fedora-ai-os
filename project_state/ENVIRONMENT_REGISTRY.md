# Fedora AI OS - ENVIRONMENT_REGISTRY.md

Last updated: 2026-06-12

## Purpose
The Environment Registry acts as a dedicated registry for Profession-Specific Agentic Environments (Environment Packs). It separates lifecycle management and discovery of environment-level capabilities from the Core Agent Registry.

## Registry Model
The Environment Registry tracks curated environment bundles consisting of:
- Skill bundles
- Prompt templates
- Specialized MCP tool configurations
- Memory schemas (Knowledge/Operational)

## Content
| Environment | Focus | Target Audience |
|-------------|-------|-----------------|
| Developer | Software Dev | Engineers |
| Research | Academic | Researchers |
| Content Creator | Media | Creators |
| Cybersecurity | SecOps | InfoSec |
| SysAdmin | DevOps | Admins |
| AI Engineer | ML Ops | AI Practitioners |

## Registry Workflow
- **Discovery:** Browse available packs via the Environment Marketplace.
- **Provisioning:** Registry downloads bundle signatures and assets.
- **Activation:** Runtime applies bundle policies/skills to Core Agents.
