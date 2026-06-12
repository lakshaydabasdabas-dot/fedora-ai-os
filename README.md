# Fedora AI OS – A Governed Cognitive Orchestration Layer for Fedora Linux

Fedora AI OS is a security-first, AI-native orchestration layer built on top of Fedora Linux, designed to transform the operating system into a governed cognitive workspace. It augments Fedora/GNOME with a federation of specialized, SELinux-confined AI agents that coordinate tasks, memory, desktop interaction, and system management through auditable interfaces.

This project is NOT a chatbot, a shell wrapper, a voice assistant, or a custom distribution. It IS a cognitive orchestration layer built with Fedora’s own security primitives.

## Core Principles:

*   **Governed Autonomy:** AI acts within enforced, auditable boundaries.
*   **Security First:** Isolation before intelligence, always.
*   **Observability:** Every action is traceable, replayable, and attributed.
*   **Recoverability:** All failures must be reversible or compensatable.
*   **Modularity:** Components can be replaced independently.
*   **Upstream Alignment:** Built with Fedora and GNOME ecosystems, not around them.
*   **OS-Native Execution:** Direct DBus/Unix sockets for low latency; MCP Gateway for external tools.

## Project Status Snapshot:

Fedora AI OS has moved from an architectural concept to active implementation and community engagement.

**Implemented Core Components (V1/V2):**
*   **Secure Runtime:** Rootless Podman containers with SELinux confinement, running the Goose executor.
*   **Workflow Engine:** LangGraph-based durable, checkpointed, and recoverable workflows powered by `v3_engine.py`.
*   **Memory System:** Multi-tiered memory (Personal, Operational, Graph, Audit) for structured fact storage.
*   **MCP Gateway:** A foundational, secure gateway for external tool calls.
*   **Resilience Mechanisms:** Standby Orchestrator for CEO agent failures and crash simulation/recovery testing.

**Key Documentation Reviewed:**
*   **Architecture Blueprints (v3.0 & v4.0):** Detailed guides on the 7-layer structure, agent roles, security, LLM routing, and roadmaps.
*   **Agentic Flow:** Describes the multi-agent system, marketplace, security pre-flight, and MCP execution.
*   **Implementation Details:** Documentation of recoverable workflows and core engine logic.
*   **Project History & Community:** Chronological progress from idea to Fedora SIG engagement.
*   **External Validation:** Analysis of Red Hat's `coreos/ai-helpers` repository confirming architectural alignment.

The project is currently focused on maturing its core components and integrating further intelligence, memory, and agent capabilities in subsequent development phases.

## Project Structure:

*   **`implementation_code/`**: All live code.
    *   `implementation_code/phase0/` — Workflow engine (v2/v3, complete and chaos-tested)
    *   `implementation_code/phase1/` — MCP Gateway, LangGraph bridge, and future components
*   **`project_state/`**: Source of truth — authoritative project documents (5 files).
*   **`roles/`**: Team assignments for all 4 contributors.
*   **`proposals/`**: Architecture blueprints and reference documents (not implementation state).
*   **`aios_done/`**: Historical/completed milestone documentation.

## Next Steps:

The current critical path is building the **MCP Gateway Core Proxy** — the central routing layer that every agent uses to talk to external tools. See `project_state/CRITICAL_PATH.md` for details and `project_state/NEXT_ACTIONS.md` for the full 20-task queue.

---
* *This README was generated based on our project discussions and reviewed documentation.*

