# AWF Documentation

This repository powers [docs.awf-project.ai](https://docs.awf-project.ai/), the documentation for the AWF toolkit. Developers can use the portal to write an agent workflow, connect an agent to a codebase, query a Prolog knowledge base, or schedule a job. Each tool has its own guides and reference pages. A single [documentation search](https://docs.awf-project.ai/search/) covers all four.

## Explore the toolkit

| Tool | What it does | Start here |
| --- | --- | --- |
| [AWF CLI](https://docs.awf-project.ai/cli/) | Runs YAML workflows that combine AI agents and shell commands. | [Run your first workflow](https://docs.awf-project.ai/cli/getting-started/quick-start/) |
| [Tower](https://docs.awf-project.ai/tower/) | Indexes a codebase so agents can find symbols, follow references, and edit files through the Model Context Protocol (MCP). | [Connect an MCP client to your workspace](https://docs.awf-project.ai/tower/getting-started/installation/) |
| [ZPM](https://docs.awf-project.ai/zpm/) | Gives agents a persistent Prolog knowledge base where they can store facts, define rules, and query what follows from them. | [Set up the ZPM MCP server](https://docs.awf-project.ai/zpm/getting-started/getting-started-with-zpm-mcp-server/) |
| [ztick](https://docs.awf-project.ai/ztick/) | Lets an application schedule a job for a specific time and use rules to dispatch it to a command, webhook, or AWF workflow. | [Schedule your first job](https://docs.awf-project.ai/ztick/tutorials/getting-started/) |

## Run the portal locally

You can preview the entire portal without installing the four products. From the root of this checkout, use Make and Hugo to start the site. The production build uses Hugo 0.167.0.

```sh
make serve
```

Open [localhost:1313](http://localhost:1313/). Hugo rebuilds the preview as you edit. To generate the static site in `public/` and run the same checks as CI, run the following command with Python 3.9 or later installed.

```sh
make check
```

The checker validates internal links, heading anchors, redirects from older URLs, the sitemap, and the search index. To build the site alone, run `make build`.

## Contribute a guide or correction

1. Find the Markdown page under [content/](content/) in the relevant product directory. Imported pages keep the original repository path in their `source` field so you can compare a guide with its upstream version.
2. Write in English. Give a new page a descriptive `title` and a stable `slug`. Link to other guides by their content paths, such as `[Input validation](/cli/reference/validation.md)`. Hugo resolves these to published URLs and includes new guides in search.
3. If you move a page, add its former URL to `aliases` so existing bookmarks still work. Preview the change with `make serve`, then run `make check` before opening a pull request.

## How the site is published

Hugo turns the Markdown in [content/](content/) into static HTML using the templates in [layouts/](layouts/). It also builds a search index that the browser loads when a reader opens the search page. The [GitHub Pages workflow](.github/workflows/pages.yml) runs `make check` on pull requests and publishes the generated site after a successful build on `main`.

## License

The portal code and its original documentation use the [MIT License](LICENSE). Imported materials retain their upstream licenses, including the [EUPL-1.2](LICENSES/EUPL-1.2.txt). The bundled Geist typeface uses the [SIL Open Font License 1.1](static/assets/Geist-LICENSE.txt).
