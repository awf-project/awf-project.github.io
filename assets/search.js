async function search() {
  const query = new URLSearchParams(location.search).get("q")?.trim() || "";
  document.querySelector('input[name="q"]').value = query;
  if (!query) return;
  const status = document.getElementById("status");
  status.textContent = "Searching…";
  try {
    const response = await fetch("../index.json");
    if (!response.ok) throw new Error("Search index unavailable");
    const entries = await response.json();
    const terms = query.toLowerCase().split(/\s+/);
    const matches = [];
    for (const entry of entries) {
      const heading = (entry.tool + " " + entry.title).toLowerCase();
      const body = entry.body.toLowerCase();
      if (terms.every(term => heading.includes(term) || body.includes(term))) {
        const score = terms.filter(term => heading.includes(term)).length;
        matches.push({entry, score});
      }
    }
    matches.sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title));
    const results = document.getElementById("results");
    for (const {entry} of matches) {
      const item = document.createElement("li");
      const tool = document.createElement("small");
      tool.textContent = entry.tool;
      const link = document.createElement("a");
      link.href = entry.url;
      link.textContent = entry.title;
      item.append(tool, link);
      results.append(item);
    }
    status.textContent = matches.length
      ? matches.length + (matches.length === 1 ? " result" : " results")
      : "No results. Try another command or topic.";
  } catch {
    status.textContent = "The search index could not be loaded. Reload to try again.";
  }
}
search();
