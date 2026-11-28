---
title: "AWF CLI"
weight: 1
description: "Compose AI agents and shell commands into versioned workflows."
source: "docs/README.md"
aliases: ["/cli/docs/"]
---

Welcome to the AWF (AI Workflow Framework CLI) documentation.

> **📖 Online documentation:** These docs are also available at **[docs.awf-project.ai/cli](/cli/)** with full-text search and dark mode support.

> **⚠️ Security Warning:** AWF executes shell commands and interacts with AI agents. Agents can "hallucinate" and produce destructive commands. Never run untrusted workflows and always review them using `--dry-run` or `--interactive` mode. See [Security Policy](/cli/security.md) for more.

## Quick Navigation

| Section | Description |
|---------|-------------|
| [Getting Started](/cli/getting-started/_index.md) | Installation and first steps |
| [User Guide](/cli/user-guide/_index.md) | Commands, workflow syntax, templates |
| [Reference](/cli/reference/_index.md) | Exit codes, error codes, interpolation, validation, timeouts, loops |
| [Development](/cli/development/_index.md) | Architecture, contributing, testing |

## Getting Started

New to AWF? Start here:

1. [Installation](/cli/getting-started/installation.md) - Install AWF on your system
2. [Quick Start](/cli/getting-started/quickstart.md) - Create and run your first workflow
3. [Build Your First Plugin](/cli/getting-started/first-plugin.md) - Scaffold, test, install, and run your first AWF plugin

## User Guide

Learn how to use AWF effectively:

- [Commands](/cli/user-guide/commands.md) - All CLI commands and flags
- [Interactive Input Collection](/cli/user-guide/interactive-inputs.md) - Automatic prompting for missing workflow inputs
- [Agent Steps](/cli/user-guide/agent-steps.md) - Invoke AI agents via CLI (Claude, Codex, Gemini, GitHub Copilot, Mistral Vibe, OpenCode) or HTTP APIs (OpenAI, Ollama, vLLM, Groq)
  - [Agent Skills](/cli/user-guide/agent-steps.md#agent-skills) - Inject deterministic domain knowledge into agent steps via `skills:` declarations with multi-directory discovery
  - [Agent Roles](/cli/user-guide/agent-steps.md#agent-roles) - Inject reusable personas into agent steps via `role:` field referencing AGENTS.md files with system prompt composition
  - [Output Formatting](/cli/user-guide/agent-steps.md#output-formatting) - Automatic code fence stripping and JSON validation (`output_format: json|text`)
  - [Streaming Output Display & Tool Markers](/cli/user-guide/agent-steps.md#streaming-output-display--tool-markers) - Human-readable filtered output and tool-use markers for `--output streaming` and `--output buffered` modes
  - [External Prompt Files](/cli/user-guide/agent-steps.md#external-prompt-files) - Load prompts from Markdown files with template interpolation
  - [Model Validation](/cli/user-guide/agent-steps.md#model-validation) - Provider-specific model name validation (Claude, Gemini, Codex)
  - [MCP Proxy](/cli/user-guide/agent-steps.md#mcp-proxy---tool-interception-and-control) - Tool call interception and observability via Model Context Protocol; expose plugin operations as MCP tools
- [Conversation Mode](/cli/user-guide/conversation-steps.md) - Multi-turn conversations with native session resume for CLI providers and context window management
- [Configuration](/cli/user-guide/configuration.md) - Project configuration file
- [Workflow Syntax](/cli/user-guide/workflow-syntax.md) - YAML workflow definition reference
  - [Inline Error Shorthand](/cli/user-guide/workflow-syntax.md#inline-error-shorthand) - Specify error messages directly on steps without separate terminal states
  - [External Script Files](/cli/user-guide/workflow-syntax.md#external-script-files) - Load shell commands from external `.sh` files with template interpolation and shebang-based interpreter dispatch
  - [Shebang Support](/cli/user-guide/workflow-syntax.md#shebang-support) - Execute scripts via their declared interpreter (Python, Perl, bash, etc.)
  - [GitHub Operations](/cli/user-guide/workflow-syntax.md#github-operations) - Built-in GitHub plugin with declarative operations
  - [HTTP Operations](/cli/user-guide/workflow-syntax.md#http-operations) - Built-in HTTP operation for REST API calls
  - [Notification Operations](/cli/user-guide/workflow-syntax.md#notification-operations) - Built-in notification plugin with desktop and webhook backends
- [Retry Configuration](/cli/user-guide/retry.md) - Automatic retry with backoff strategies, delay capping, and exit code filtering
- [Templates](/cli/user-guide/templates.md) - Reusable workflow templates
- [Plugins](/cli/user-guide/plugins.md) - Install plugins, scaffold new plugin repositories, and author custom operations, validators, and step types
- [Plugin Events](/cli/user-guide/plugin-events.md) - Real-time event reactivity between plugins and core
- [Workflow Packs](/cli/user-guide/workflow-packs.md) - Install, execute (`awf run pack/workflow`), and manage reusable workflow packs with 3-tier path resolution
- [HTTP API](/cli/user-guide/api.md) - REST API server with OpenAPI 3.1 spec, async workflow execution, real-time SSE streaming, and remote integration
- [Terminal UI (TUI)](/cli/user-guide/tui.md) - Interactive dashboard for workflow browsing, monitoring, history, and agent conversations
- [ACP Editor Integration](/cli/user-guide/acp-server.md) - Connect AWF to ACP-compatible editors (Zed, acp.nvim) as a transparent AI agent; workflow discovery, multi-turn conversations, and approval gates in the editor
- [Upgrading AWF](/cli/user-guide/upgrade.md) - Self-update command with version checking, checksum verification, and atomic binary replacement
- [Audit Trail](/cli/user-guide/audit-trail.md) - Structured execution audit log with JSONL output
- [Distributed Tracing](/cli/user-guide/tracing.md) - Configure OpenTelemetry tracing to export workflow spans to Jaeger, Grafana Tempo, or compatible backends
- [Examples](/cli/user-guide/examples.md) - Real-world workflow examples

## Reference

Technical reference documentation:

- [Exit Codes](/cli/reference/exit-codes.md) - Error codes and their meanings
- [Error Codes](/cli/reference/error-codes.md) - Structured error taxonomy and lookup guide
- [Variable Interpolation](/cli/reference/interpolation.md) - Template variables and syntax
- [Input Validation](/cli/reference/validation.md) - Validation rules for workflow inputs
- [Timeouts](/cli/reference/timeouts.md) - Optional execution deadlines, inheritance, and cancellation semantics
- [Loop Reference](/cli/reference/loop.md) - Loop control flow and transitions
- [Audit Trail Schema](/cli/reference/audit-trail-schema.md) - Workflow start/completion audit log JSONL format
- [Transcript Schema](/cli/reference/transcript-schema.md) - Canonical agent exchange transcript (full execution lifecycle in JSONL)
- [Package Documentation](/cli/reference/package-documentation.md) - Discovering code documentation with `go doc`

## Development

For contributors and developers:

- [Architecture](/cli/development/architecture.md) - Hexagonal architecture overview
- [Creating an Agent Provider](/cli/development/creating-agent-provider.md) - Provider implementation guide, including CLI hooks and MCP proxy integration patterns
- [Plugin Event Architecture](/cli/development/plugin-event-architecture.md) - EventBus, gRPC event adapter, and wiring design
- [Project Structure](/cli/development/project-structure.md) - Codebase organization
- [Code Quality](/cli/development/code-quality.md) - Linters, formatters, and quality tooling
- [Testing](/cli/development/testing.md) - Testing conventions and commands

## Building the original CLI documentation locally

To build and serve the documentation site locally:

```bash
make docs        # Build the site with minification
make docs-serve  # Serve at http://localhost:1313 with live reload
make docs-clean  # Clean build artifacts
```

The documentation site is built with [Hugo](https://gohugo.io) and the [Doks](https://getdoks.org) theme. Documentation source files in this directory are mounted directly into the site via Hugo module configuration — changes are reflected immediately on rebuild without requiring file copies.

**Requirements:** Hugo 0.147+ with extended edition (includes CSS/JS transpiling)

## Additional Resources

- [CHANGELOG](/cli/changelog.md) - Version history
- [CONTRIBUTING](/cli/contributing.md) - How to contribute
- [LICENSE](https://github.com/awf-project/cli/blob/main/LICENSE) - EUPL-1.2 License
