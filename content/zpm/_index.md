---
title: "ZPM"
weight: 3
description: "Give agents a shared memory of facts and rules they can query through MCP."
source: "docs/README.md"
aliases: ["/zpm/docs/"]
---

Welcome to zpm documentation. Choose your path:

## For New Users

- **[Getting Started with MCP Server](/zpm/getting-started/mcp-server.md)** — Set up and run the zpm MCP server in 5 minutes
- **[Project Initialization](/zpm/user-guide/project-init.md)** — Initialize a `.zpm/` project directory
- **[Local Site Development](https://github.com/awf-project/zpm/blob/7002b3b6527376e514ab4ba6846ecaeb538a7ee7/docs/getting-started/site-development.md)** — Preview the zpm documentation site locally

## For Users

- **[Memory Segments](/zpm/user-guide/memory-segments.md)** — Manage isolated knowledge domains with named memory segments
- **[Schema Discovery](/zpm/user-guide/schema-discovery.md)** — Explore predicates in the knowledge base
- **[Find Predicate References](/zpm/user-guide/predicate-references.md)** — Locate all usage sites of a predicate before refactoring
- **[Rename Predicates Safely](/zpm/user-guide/rename-predicate.md)** — Atomically rename functors with automatic TMS preservation
- **[Knowledge Base Overview](/zpm/user-guide/knowledge-base-overview.md)** — Get a comprehensive snapshot with predicates, samples, assumptions, and persistence health
- **[Fact Update and Upsert](/zpm/user-guide/fact-update-upsert.md)** — Replace facts atomically or insert if missing
- **[Quality Checks](/zpm/user-guide/quality-checks.md)** — Verify consistency and explain reasoning chains
- **[Fact Deletion](/zpm/user-guide/fact-deletion.md)** — Remove individual facts or clear entire categories
- **[Truth Maintenance System](/zpm/user-guide/truth-maintenance.md)** — Manage assumptions and automatically propagate belief changes
- **[Knowledge Base Persistence](/zpm/user-guide/persistence.md)** — Save and restore knowledge base state with snapshots and automatic recovery
- **[Upgrading zpm](/zpm/user-guide/upgrading.md)** — Keep zpm up to date with SHA256 verification
- **[Contributing to Documentation](https://github.com/awf-project/zpm/blob/7002b3b6527376e514ab4ba6846ecaeb538a7ee7/docs/user-guide/contributing-docs.md)** — Guidelines for writing site documentation

## For Developers

- **[CLI Reference](/zpm/reference/cli.md)** — Command-line interface, subcommands, and flags
- **[Prolog Engine Reference](/zpm/reference/prolog-engine.md)** — Engine API, query syntax, and sandboxing constraints
- **[MCP Tools Reference](/zpm/reference/mcp-tools.md)** — Available tools and their JSON-RPC methods
- **[Site Configuration Reference](/zpm/reference/site-config.md)** — Hugo site configuration, deployment, and customization
- **[Project Brief](/zpm/project-brief.md)** — Vision, requirements, and success criteria
- **[Architecture Decision Records](/zpm/adr/_index.md)** — Design decisions and rationale

## Documentation Site

This documentation is also available online at **https://docs.awf-project.ai/zpm/**. The original ZPM documentation site is built with Hugo and the Thulite/Doks theme, and deploys automatically via GitHub Actions on push to `main`.

To preview locally: `cd site && npm ci && npm run dev`

## About zpm

zpm is a Prolog inference engine for the Model Context Protocol, implemented in Zig. It aims to enable deterministic logical reasoning in AI workflows.
