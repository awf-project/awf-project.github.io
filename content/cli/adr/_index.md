---
title: "Architecture decisions"
source: "docs/ADR/README.md"
description: "Understand the architecture decisions behind AWF, including execution, persistence, provider integrations, and the tradeoffs that shaped the CLI."
weight: 5
aliases: ["/cli/docs/adr/"]
---

This directory contains the Architecture Decision Records (ADRs) for this project.

## Format

Each ADR follows this structure:

```markdown
# NNNN: Title

**Status**: Proposed | Accepted | Superseded | Deprecated
**Date**: YYYY-MM-DD

## Context       — What is the issue motivating this decision?
## Candidates    — Options considered with trade-offs
## Decision      — What we chose and why
## Consequences  — What becomes easier/harder
## Constitution Compliance — Mapping to project principles
```

## Numbering Convention

ADRs are numbered sequentially: `001`, `002`, etc.
Numbers are never reused. If a decision is reversed, the original ADR is marked "Superseded" and a new ADR is created with a reference.

## Index

| ADR | Title | Status |
|-----|-------|--------|
| [001](/cli/adr/001-hexagonal-architecture.md) | Hexagonal Architecture | Accepted |
| [002](/cli/adr/002-error-taxonomy-exit-codes.md) | Error Taxonomy with Exit Codes | Accepted |
| [003](/cli/adr/003-yaml-state-machine-workflows.md) | YAML State Machine for Workflow Definition | Accepted |
| [004](/cli/adr/004-domain-operation-registry.md) | Domain Operation Registry with Infrastructure Coexistence | Accepted |
| [005](/cli/adr/005-atomic-file-writes.md) | Atomic File Writes for State Persistence | Accepted |
| [006](/cli/adr/006-xdg-path-resolution.md) | XDG-Compliant Path Resolution | Accepted |
| [007](/cli/adr/007-agent-prompt-xor-constraint.md) | Agent Prompt XOR Constraint | Accepted |
| [008](/cli/adr/008-openai-compatible-provider-http-adapter.md) | OpenAI-Compatible Provider: HTTP Adapter Integration | Accepted |
| [009](/cli/adr/009-breaking-removal-custom-provider-v0.4.0.md) | Breaking: Removal of Custom Provider in v0.4.0 | Accepted |
| [010](/cli/adr/010-paired-jsonl-audit-trail-with-atomic-append.md) | Paired JSONL Audit Trail with Atomic Append | Accepted |
| [011](/cli/adr/011-application-layer-secret-masking-for-audit-events.md) | Application-Layer Secret Masking for Audit Events | Accepted |
| [012](/cli/adr/012-runtime-shell-detection.md) | Runtime Shell Detection with $SHELL Environment Variable | Accepted |
| [013](/cli/adr/013-context-aware-input-ports.md) | Context-Aware Input Ports | Accepted |
| [014](/cli/adr/014-shebang-execution-for-script-files.md) | Shebang Execution for Script Files | Accepted |
| [015](/cli/adr/015-grpc-go-plugin-transport-for-external-plugins.md) | gRPC via go-plugin as External Plugin Transport | Accepted |
| [016](/cli/adr/016-http-interface-adapter-huma-sse-streaming.md) | HTTP Interface Adapter with Huma v2 and SSE Streaming | Accepted |
| [017](/cli/adr/017-mcp-proxy-stdio-subprocess-for-tool-interception.md) | MCP Proxy via stdio Subprocess for Tool Interception | Accepted |
| [018](/cli/adr/018-acp-transparent-agent-server-protocol.md) | ACP Transparent Agent Server via JSON-RPC 2.0 stdio Subprocess | Accepted |
| [019](/cli/adr/019-mcp-server-sdk-adapter.md) | MCP Server Migration to Official go-sdk | Accepted |
| [020](/cli/adr/020-acp-server-migration-to-coder-sdk.md) | ACP Server Migration to Official coder/acp-go-sdk | Accepted |

## Creating a New ADR

1. Find the next number: `ls docs/ADR/ | grep -oP '^\d+' | sort -n | tail -1` + 1
2. Copy the template: `cp docs/ADR/.template.md docs/ADR/NNNN-short-name.md`
3. Fill in all sections
4. Update this index
5. Submit for review

## Pre-Merge Checklist

Before merging any new or modified ADR:

- [ ] **Cross-references**: All `[ADR-NNNN]` links resolve to existing files
- [ ] **Supersession**: If changing a prior decision, both ADRs have `Supersedes`/`Superseded by` metadata
- [ ] **Constitution**: Compliance section maps to current constitution version
- [ ] **Candidates**: At least 2 alternatives documented with trade-offs
