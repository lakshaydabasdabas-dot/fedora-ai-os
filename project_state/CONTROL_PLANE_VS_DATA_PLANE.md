# Fedora AI OS - CONTROL_PLANE_VS_DATA_PLANE.md

Last updated: 2026-06-12

## Architectural Distinction

### Control Plane (Fedora AI OS Owned)
The logic layer that dictates *what* is allowed and *who* is responsible.
- Trust Levels (TRUST 0-3)
- Capability Token Issuance
- Governance & Audit Policy
- Approval Workflows
- Registry (Agent/Environment)
- MCP Gateway Orchestration

### Data Plane (Infrastructure)
The operational layer that facilitates *how* the communication occurs.
- Routing / Load Balancing
- Protocol Negotiation (MCP)
- Federation / Retries
- Authentication / Encryption
- Observability (Tracing)

## Future Scalability Note
The CEO Agent currently handles provisioning and environment coordination. As environment complexity grows, a dedicated **Environment Manager** component will be needed to decouple high-level coordination from core engine orchestration. This is currently deferred to Phase 2.
