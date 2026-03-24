# AWF Landing Page

Minimalist landing page for AWF (AI Workflow Framework), inspired by [zml.ai](https://zml.ai).

## 🚀 Deploy on GitHub Pages

### Option 1: GitHub Pages Repository

1. Create a repository `awf-project.github.io` or `awf-project.github.io/cli`
2. Clone it:
   ```bash
   git clone https://github.com/awf-project/awf-project.github.io.git
   cd awf-project.github.io
   ```

3. Copy the content:
   ```bash
   cp /root/.picoclaw/workspace/awf-landing-page/index.html .
   ```

4. Commit and push:
   ```bash
   git add index.html
   git commit -m "Initial landing page"
   git push origin main
   ```

### Option 2: Dedicated Repository

1. Create a new repository `awf-landing-page`
2. Clone it:
   ```bash
   git clone https://github.com/votre-org/awf-landing-page.git
   cd awf-landing-page
   ```

3. Copy the file:
   ```bash
   cp /root/.picoclaw/workspace/awf-landing-page/index.html .
   ```

4. Enable GitHub Pages in repository settings:
   - Settings → Pages → Source → Deploy from a branch → main → / (root)

## 📋 Structure

```
awf-landing-page/
├── index.html          # Main page
└── README.md           # Deployment instructions
```

## 🎨 Design System

- **Theme**: Dark mode (inspired by zml.ai)
- **Font**: Monospace (SF Mono, Monaco, Inconsolata)
- **Colors**:
  - Background: `#0a0a0a`
  - Foreground: `#e4e4e4`
  - Accent: `#22c55e` (green)
  - Muted: `#a0a0a0`

## 📊 Content

### Main Sections:
1. **Header**: Logo, tagline, CTA
2. **Stats**: GitHub stars, Discord members, plugins
3. **Why AWF**: Governance, extensibility, agnosticism, performance
4. **Architecture**: Go CLI, YAML, Plugin System
5. **Integrations**: OpenAI, Anthropic, Mistral, GitHub
6. **Community**: GitHub, Discord, Plugins

### Key Messages:
- "Orchestrate your LLMs in production"
- Zero vendor lock-in
- Plugin system v0.5.0
- Native audit and governance

## 🎯 Communication Objectives

### Positioning:
- **Not a competitor** to LLMs, but the **operating system** for orchestrating them
- Focus on **production-grade** features (audit, validation, reproducibility)
- **Open-source** and community-driven

### For LLM Providers:
- AWF positions their models at the center of enterprise workflows
- Official plugin = better integration
- Plugin ecosystem = more usage of their models

## 🔧 Customization

### Modify stats:
```html
<div class="stat-number">300+</div>
<div class="stat-label">GitHub Stars</div>
```

### Modify CTAs:
```html
<a href="https://github.com/awf-project/cli" class="btn btn-primary">
    GitHub - ⭐ Star on GitHub
</a>
```

### Add integrations:
```html
<div class="card">
    <h3>[Provider]</h3>
    <p>Short description</p>
    <pre><code>awf plugin install awf-project/awf-plugin-[provider]</code></pre>
</div>
```

## 📈 Success Metrics

- **Traffic**: 100+ visitors/week
- **Conversion**: 10% to GitHub
- **Engagement**: 5+ contributions/month
- **Partnerships**: 1+ official plugin per provider

## 🚀 Next Steps

1. [x] Create landing page
2. [ ] Deploy on GitHub Pages
3. [ ] Configure analytics (Plausible, simple)
4. [ ] Add contact form / newsletter
5. [ ] Create "Partnership" page for LLM providers
6. [ ] Add testimonials / use cases
7. [ ] Create interactive demos (CodeSandbox, etc.)

## 📞 Contact

- **Maintainer**: [Your name]
- **Email**: [your@email.com]
- **Discord**: #announcements
- **GitHub**: @awf-project

---

"Every bit helps, every bit matters."
- AWF
