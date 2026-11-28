# AWF Documentation

This Hugo site hosts the English guides for AWF CLI, Tower, ZPM, and ztick at [docs.awf-project.ai](https://docs.awf-project.ai/). The production build uses Hugo 0.167.0. The link checker requires Python 3.9 or later and uses only the standard library.

## Local development

```sh
make serve  # Start the live preview at http://localhost:1313
make check  # Build the site and check internal links, anchors, redirects, and search
```

`make build` writes the static site to `public/`. Hugo generates the search index at build time. Only the search results page loads it.

### Tailnet preview

In **Nexus → Applications**, start the `documentation` project's `web` service in the `main` slot. Select **Advertise HTTPS** the first time. The [tailnet preview](https://documentation-awf.tailde86d7.ts.net/) is available while the instance is running. The fixed hostname is declared in [.nexus/services.json](.nexus/services.json). Nexus supplies the bind address, port, and HTTPS hostname to Hugo.

## Content and sources

Edit the Markdown pages in `content/`. The initial import included all 148 files from the four upstream `docs/` directories, including indexes and architecture decision record (ADR) templates. It also included project overviews, changelogs and, where available, contribution guides, community policies, plugin examples, and release articles.

| Product | Imported revision | Files from docs/ | Documents indexed at import |
| --- | --- | ---: | ---: |
| [AWF CLI](content/cli/) | [466c127](https://github.com/awf-project/cli/tree/466c127664c4e564805ba68e3032e5c57d8c9a93) | 62 | 75 |
| [Tower](content/tower/) | [be269c91](https://github.com/awf-project/tower/tree/be269c91e584dc974f1f2a4885dab595284f5fb5) | 31 | 33 |
| [ZPM](content/zpm/) | [f5187f5](https://github.com/awf-project/zpm/tree/f5187f5cf5a10c79f943068d82cc2f4d6a38e3da) | 28 | 30 |
| [ztick](content/ztick/) | [6f7b6a9](https://github.com/awf-project/ztick/tree/6f7b6a9c9f2eac9bdd99a50c788a3e9a238bec66) | 27 | 32 |

Each imported page records its upstream path in the `source` field. Use this field to locate the corresponding page when porting an upstream change. Give new pages a `title` and a stable `slug`. Link to content files using paths such as `/cli/reference/validation.md`. Hugo resolves these links at build time. When renaming a page, retain its slug or add its previous URL to `aliases`.

Product sections are published under `/cli/`, `/tower/`, `/zpm/`, and `/ztick/`. Moved pages retain their former `/docs/` URLs as Hugo aliases. GitHub Pages serves static redirects for those URLs. With JavaScript enabled, the redirects preserve the query string and fragment.

The portal uses the logo, Geist font, `station.webp` artwork, and colors from revision `f7b2374` of the `website` project. The stylesheet is in [assets/docs.css](assets/docs.css). Graphic assets and the Geist license are in [static/assets](static/assets/).

### Updates from product workflows

AWF's `plan` workflow delegates ADRs to `project-documentation`. Its `docs` workflow delegates guides to the same workflow. CLI, Tower, ZPM, and ztick each provide a local override in `.awf/workflows/project-documentation.yaml`. The writer reads the issue specification in the product checkout, updates English pages in this portal's `content/<product>/` directory, and runs `make check`. README and changelog updates stay in the product checkout.

By default, the writer looks for a checkout named `documentation` beside the main product repository, including when the product workflow runs in a linked worktree. Set `AWF_DOCUMENTATION_ROOT` to use another portal checkout. Review and commit portal changes in that repository. New pages authored in the portal appear in search and can omit the upstream `source` field.

## Publishing

The [Pages workflow](.github/workflows/pages.yml) runs `make check` on pull requests and on `main`. Once GitHub Pages is configured to deploy from GitHub Actions, a push to `main` publishes `public/`. The production domain is configured in [hugo.toml](hugo.toml) and [static/CNAME](static/CNAME).

The Tower repository also contains a `site/static/CNAME` for this domain. During cutover, check the current assignment in GitHub Pages, transfer the custom domain to the `documentation` repository if necessary, and verify DNS and HTTPS. The [site checker](scripts/check_site.py) covers the product entry points and deep links used by the main AWF website.
