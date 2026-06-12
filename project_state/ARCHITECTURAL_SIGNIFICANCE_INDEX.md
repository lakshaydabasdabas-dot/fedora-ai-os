# ARCHITECTURAL SIGNIFICANCE INDEX.md
Last Updated: 2026-06-12

## Tier 1 — Architectural Pivots
These are high-priority. They define Fedora AI OS.

### 1. Control Plane vs Data Plane Separation
- Importance Score: 10
- Reason: Fundamental architectural governance model (MCP Gateway as Control Plane).
- Impacted Components: MCP Gateway, Runtime Engine, Agent Registry.
- Date Introduced: 2026-06-08
- Current Status: ACTIVE (Design Phase)

### 2. Profession-Specific Agentic Environments
- Importance Score: 10
- Reason: Shifts OS from individual agents to comprehensive professional environment packs.
- Impacted Components: Agent Kernel, Registry, UI, Distribution.
- Date Introduced: 2026-06-11
- Current Status: ACTIVE (Definition Phase)

### 3. Recoverable Workflow Runtime
- Importance Score: 9
- Reason: OS-Native execution reliability via atomic/compensation/suspend-resume.
- Impacted Components: Workflow Engine (phase0), Podman runtime.
- Date Introduced: 2026-05-15
- Current Status: DONE (Phase 0)

### 4. Knowledge Infrastructure
- Importance Score: 9
- Reason: Fifth memory tier integration (docs2db) for RAG/embedding.
- Impacted Components: Memory Hierarchy, RAG Infrastructure.
- Date Introduced: 2026-06-12
- Current Status: INITIALIZING

## Tier 2 — Strategic Discoveries
Strategic external components that influence OS architecture.

### 1. MCP Gateway
- Importance Score: 8
- Reason: Core proxy for governed capabilities and trust.
- Impacted Components: Federation, Governance, Tools.
- Date Introduced: 2026-06-08
- Current Status: ACTIVE (Phase 1)

### 2. docs2db (Knowledge Infrastructure)
- Importance Score: 7
- Reason: External ingestion integration for the 5th memory tier.
- Impacted Components: Memory Hierarchy.
- Date Introduced: 2026-06-12
- Current Status: EVALUATING

## Tier 3 — Supporting Evidence
Repositories, experiments, papers.

### 1. Phase 0 Engine Experiments
- Importance Score: 5
- Reason: Validated the Recoverable Workflow Runtime architectural decision.
- Date Introduced: 2026-05-15
- Current Status: DONE

## Tier 4 — Historical Memory
Superseded ideas; context only.

### 1. Simple Role-based Agent Architecture
- Importance Score: 2
- Reason: Superseded by Profession-Specific Agentic Environments.
- Date Introduced: PRE-2026-06
- Current Status: SUPERSEDED
