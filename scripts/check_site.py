"""Check the generated site, internal links and published product entry points."""
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

PUBLIC = Path(__file__).resolve().parents[1] / "public"
BASE = "https://docs.awf-project.ai/"
LEGACY = re.compile(r"^/(cli|tower|zpm|ztick)/docs(?:/|$)")
# The main AWF website also links to the historical forms of these routes.
ENTRY_POINTS = (
    "/cli/", "/tower/", "/zpm/", "/ztick/",
    "/cli/reference/input-validation/",
    "/tower/getting-started/installation/",
    "/zpm/reference/mcp-tools-reference/",
    "/zpm/reference/prolog-engine-reference/",
    "/ztick/reference/configuration-reference/",
    "/ztick/reference/http-api-reference/",
)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = set()
        self.has_source = False
        self.canonical = None
        self.redirect = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = attrs.get("content", "").removeprefix("0; url=")
        if tag == "a" and "original-document" in attrs.get("class", "").split():
            self.has_source = True
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src", "action"):
            if attrs.get(key):
                self.links.add(attrs[key])


def main():
    pages = {}
    for file in PUBLIC.rglob("*.html"):
        url = "/" + file.relative_to(PUBLIC).as_posix().removesuffix("index.html")
        pages[url] = Page()
        pages[url].feed(file.read_text())

    errors = defaultdict(set)
    for source, page in pages.items():
        if LEGACY.match(source) or page.redirect is not None:
            if not page.redirect or page.redirect != page.canonical:
                errors["Invalid redirect"].add(source)
            elif page.redirect != urljoin(BASE, urlsplit(page.redirect).path):
                errors["Redirect outside production site"].add(source)
        for link in page.links:
            url = urlsplit(urljoin(urljoin(BASE, source), link))
            if url.netloc != urlsplit(BASE).netloc:
                continue
            path = unquote(url.path)
            if path in pages:
                if LEGACY.match(path) or pages[path].redirect is not None:
                    errors[source].add(link)
                if url.fragment and unquote(url.fragment) not in pages[path].ids:
                    errors[source].add(link)
            elif not (PUBLIC / path.lstrip("/")).is_file():
                errors[source].add(link)

    for url in ENTRY_POINTS:
        if url not in pages:
            errors["Website entry points"].add(url)
        product, tail = url[1:].split("/", 1)
        legacy = f"/{product}/docs/{tail}"
        if legacy not in pages or pages[legacy].redirect != urljoin(BASE, url):
            errors["Missing legacy redirect"].add(legacy)
    sitemap = ET.parse(PUBLIC / "sitemap.xml")
    for loc in sitemap.iterfind(".//{*}loc"):
        path = urlsplit(loc.text).path
        if loc.text != urljoin(BASE, path) or path not in pages or pages[path].redirect:
            errors["Invalid sitemap entry"].add(loc.text)
    index = json.loads((PUBLIC / "index.json").read_text())
    indexed_urls = {entry["url"] for entry in index}
    for source, page in pages.items():
        if page.has_source and source not in indexed_urls:
            errors["Missing from search"].add(source)
    for entry in index:
        if (entry["url"] not in pages or pages[entry["url"]].redirect
                or not entry["title"] or not entry["body"].strip()):
            errors["Invalid search entry"].add(entry["url"])

    if errors:
        for source, links in sorted(errors.items()):
            print(source, *sorted(links), sep="\n  ")
        raise SystemExit(1)
    print(f"{len(pages)} HTML pages, {len(index)} searchable documents, "
          f"{len(ENTRY_POINTS)} website entry points verified.")


if __name__ == "__main__":
    main()
