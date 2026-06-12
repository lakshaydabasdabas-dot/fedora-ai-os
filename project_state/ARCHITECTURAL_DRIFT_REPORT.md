# ARCHITECTURAL DRIFT REPORT.md
Last Updated: 2026-06-12

## Summary
The Fedora AI OS project has undergone significant architectural shifts in June 2026. While the core workflow runtime (Phase 0) remains robust, the agent organizational model and memory hierarchy have evolved, leading to some documentation drift.

## Architectural Drift & Overlapping Documentation

### 1. Agent Models (Drift)
- Concept: Older proposals refer to a stable set of 4-6 role-based core agents (CEO, Security, etc.) as the *primary agent architecture*.
- Current Reality: The architecture has shifted to **Profession-Specific Agentic Environments**. The core roles now act as an *agnostic kernel* upon which environment packs (Developer, Student, etc.) are applied.
- Recommendation: Archive or update documentation explicitly referencing old role-only models in favor of the new Kernel/Environment Pack model.

### 2. Marketplace & Registry (Overlap/Overlap)
- Concept: `AGENT_REGISTRY.md`, `ENVIRONMENT_REGISTRY.md`, and `MARKETPLACE.md` share significant functional scope.
- Overlap: The distinction between the *Agent Registry*, *Environment Registry*, and *Marketplace* discovery is currently fluid.
- Recommendation: Consolidate Registry documentation. Clearly define:
    - Agent Registry = Core roles/runtime management.
    - Environment Registry = Professional bundle packs (Lifecycle).
    - Marketplace = Discovery and distribution surface.

### 3. Documentation Reference
- The transition from old paths (e.g., `aios_doc/`) to `project_state/` is largely complete, however, scattered notes in early proposals may still contain deprecated references.
- `ARCHITECTURE_INDEX.md` is currently the best index, but should be updated to prioritize the tiered structure defined in `ARCHITECTURAL_SIGNIFICANCE_INDEX.md`.

## Stale Assumptions
- Any assumption that Fedora AI OS will operate as a marketplace for *individual agents* rather than *professional environments* is obsolete.
- Prior roadmap documents may suggest Phase 1 features (like core agents) will be "standalone" without environment context; this must be updated to ensure *every agent roll-out happens via environment pack activation*.
