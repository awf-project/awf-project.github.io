---
title: "ztick"
weight: 4
description: "Schedule work and dispatch jobs to connected runners when they are due."
source: "docs/README.md"
aliases: ["/ztick/docs/"]
---

This directory contains documentation for ztick, organized by the **Diátaxis** framework:

## [Tutorials](/ztick/tutorials/_index.md) — Learning-Oriented

Step-by-step guides for users new to ztick.

- **[Getting Started](/ztick/tutorials/getting-started.md)** — Build, run, and verify your first ztick instance

## [User Guide](/ztick/user-guide/_index.md) — Task-Oriented

Practical how-to guides for common operations.

- **[Creating Jobs](/ztick/user-guide/creating-jobs.md)** — Define jobs with execution times and query by prefix
- **[Writing Rules](/ztick/user-guide/writing-rules.md)** — Pattern-match jobs to actions
- **[Configuring Authentication](/ztick/user-guide/authentication.md)** — Set up token-based client authentication with namespace isolation
- **[Configuration](/ztick/user-guide/configuration.md)** — Set up logging, listen addresses, persistence, TLS encryption, and authentication
- **[Inspecting Logfiles](/ztick/user-guide/inspecting-logfiles.md)** — Dump, export, and live-tail the binary persistence logfile
- **[Monitoring Health](/ztick/user-guide/monitoring-health.md)** — Check server status and inspect execution pipeline

## [Reference](/ztick/reference/_index.md) — Information-Oriented

Complete technical specification and API documentation.

- **[Configuration Schema](/ztick/reference/configuration.md)** — All TOML options and defaults
- **[HTTP API](/ztick/reference/http-api.md)** — RESTful API endpoints, authentication, and examples
- **[Protocol](/ztick/reference/protocol.md)** — Native TCP protocol reference
- **[Data Types](/ztick/reference/types.md)** — Job, Rule, Runner, Execution structures
- **[Persistence Format](/ztick/reference/persistence.md)** — Binary logfile encoding

## [Development](/ztick/development/_index.md) — Understanding-Oriented

Architecture, design decisions, and contribution guidelines.

- **[Hexagonal Architecture](/ztick/development/architecture.md)** — Layer separation and dependency flow
- **[Building the Project](/ztick/development/building.md)** — Compile from source, run tests
- **[Contributing](/ztick/development/contributing.md)** — Code style, testing, submission process

## [Architecture Decision Records (ADRs)](/ztick/adr/_index.md)

Rationale behind major technical choices.

---

**How to use this documentation:**

- **New to ztick?** Start with [Getting Started](/ztick/tutorials/getting-started.md)
- **Want to complete a task?** Check the [User Guide](/ztick/user-guide/_index.md)
- **Need technical details?** See [Reference](/ztick/reference/_index.md)
- **Curious about design?** Read [Development](/ztick/development/_index.md) and [ADRs](/ztick/adr/_index.md)
