# Fedora AI OS - ENVIRONMENT_LIFECYCLE.md
Last updated: 2026-06-12

## Environment Lifecycle States
- **Draft:** Local development/initial definition.
- **Published:** Distributed to Environment Marketplace.
- **Installed:** Downloaded locally; assets cached.
- **Activated:** Runtime has applied policies/skills to core agent.
- **Suspended:** Paused state, resources released, state checkpointed.
- **Upgraded:** Transition to new version; compatibility migration run.
- **Deprecated:** No longer updated; marked for removal.
- **Removed:** Fully purged from local registry.

## Principles
1. **Multi-versioning:** Multiple versions of an environment can coexist in the local registry.
2. **Persistence:** Environment memory (Knowledge/Operational) is associated with the active session; suspension checkpoints the state.
3. **Dependencies:** Environments can depend on other specialized environment packs via strict version constraint.
4. **Immutability:** Once an environment pack is installed, its core assets (prompts/skills) are immutable.
