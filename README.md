# Random Marginalia

Evidence-led notes on whatever is worth examining.

Each article starts with a focused question, reviews relevant published sources and available data, then separates what the evidence shows from what can reasonably be concluded.

- **Format:** a dependency-free static site, plus optional PDFs
- **Live site:** <https://obafgkm42.github.io/random-marginalia/>

## Articles

| Date | Article | Formats |
| --- | --- | --- |
| 2026.08 | 從田裡到行情：2026 年氣候怎樣影響六種主要作物與農產品 ETF · *How 2026 climate is affecting six major crops and agricultural ETFs* | [Web](posts/2026-08-climate-crops-etfs/) |
| 2026.08 | 云南为什么会长出这些诡异又美丽的植物与菌子？ · *Why Yunnan grows such strange and beautiful plants and fungi* | [Web](posts/2026-08-yunnan-strange-plants/) |
| 2026.08 | AI 寫的程式碼，工程師到底怎麼驗收？ · *How developers actually verify AI-generated code* | [Web](posts/2026-08-ai-coding-quality-assurance/) · [PDF](posts/2026-08-ai-coding-quality-assurance/ai-coding-quality-assurance.pdf) |

## Repository structure

```text
.
├── index.html                 Article index; update it when publishing a post
├── assets/style.css           Shared screen and print styles
├── posts/
│   ├── _template/index.html   Reusable article template
│   ├── _template/review-log.md  Review log template
│   └── YYYY-MM-topic/
│       ├── index.html
│       ├── review-log.md      Review record; committed with the article
│       └── topic.pdf          Optional generated PDF
├── tools/build_pdf.py         Playwright-based PDF renderer
├── docs/review-spec.md        Pre-publication agent review process
├── docs/style-rules.md        Numbered style and evidence rules
├── docs/review-agents.md      Reviewer and arbiter prompts
├── COMPLIANCE.md              Editorial and rights-review checklist
├── LICENSE                    CC BY 4.0 and MIT scopes
└── README.md
```

Article directories use `YYYY-MM-english-slug`. `build_pdf.py` removes the date prefix when naming the PDF.

## Preview locally

No build is needed for the website:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

The site is deployed from `main` with GitHub Pages. Keep `.nojekyll`: without it, Pages may process the site with Jekyll and omit `posts/_template/`.

## Publish an article

1. Copy the template:

   ```bash
   cp -r posts/_template posts/2026-09-your-topic
   ```

2. Update the page title, description, masthead, article body and source list.
3. Run at least one [agent review round](docs/review-spec.md) and revise; record it in `review-log.md` beside the article.
4. Add the new article to `index.html` and to the table above.
5. Complete the [pre-publication checklist](COMPLIANCE.md#pre-publication-checklist).
6. Optionally generate and inspect a PDF.
7. Open a pull request; on merge, GitHub Pages redeploys automatically.

### Article components

The template contains a working example of every component.

| Markup | Purpose |
| --- | --- |
| `<span class="en">term</span>` | English technical term inside Chinese prose |
| `.readouts` / `.ro` | Statistic cards; `.up` and `.down` add status colours |
| `.note`, `.note.warn`, `.note.crit` | Callouts with three severity levels |
| `.tw` around a `<table>` | Horizontally scrollable table on narrow screens |
| `.ladder` / `.rung` | Ordered stages or gates |
| `.check` | Checklist |
| `.src` + `.tag` | Annotated source list |

Use `.sec-num` only when section order matters or readers need stable section references.

## Generate a PDF

PDF generation requires [uv](https://docs.astral.sh/uv/) and a one-time Chromium download:

```bash
uv run --with playwright==1.62.0 playwright install chromium
uv run tools/build_pdf.py posts/<slug>/index.html
```

The script declares its Playwright dependency with [PEP 723](https://peps.python.org/pep-0723/) metadata and uses `tools/build_pdf.py.lock`; it does not require a project virtual environment. The print layout is shared with the browser through `assets/style.css`.

For Chinese text, install Noto CJK fonts if the host does not already provide compatible fonts. On Debian or Ubuntu:

```bash
sudo apt install fonts-noto-cjk
```

## Editorial and compliance policy

Every article must:

- distinguish reported findings from the author's interpretation;
- link each material claim to a source and record the source's date and limitations;
- use short, clearly marked quotations only when the original wording matters;
- avoid reproducing third-party charts, screenshots, tables or substantial text without a compatible licence or permission;
- mark any included third-party material and its licence next to the item;
- avoid confidential, personal or employer-owned information; and
- disclose AI authorship without overstating the level of human review.

See [COMPLIANCE.md](COMPLIANCE.md) for the source log, third-party rights, privacy, correction and release procedures. It is a practical publishing checklist, not legal advice.

Articles are AI-drafted, so the check that matters is whether a draft survives being argued with. Before publication each one goes through independent style and substance review under [docs/review-spec.md](docs/review-spec.md), against the numbered rules in [docs/style-rules.md](docs/style-rules.md), with an arbiter holding a hard three-round budget so review terminates. The record of each article's review is kept in `review-log.md` in its directory.

## Design notes

- Colour, typography and spacing are CSS custom properties in `assets/style.css`.
- Light, dark and system themes use the same token names and should be updated together.
- Chinese headings and body text use the SC or TC Noto CJK variant selected by each page's `lang` attribute; terms and figures use `IBM Plex Mono`, with local fallbacks.
- The reading measure is about 720 px; numeric columns use `tabular-nums`.

To rename the site, replace `Random Marginalia` in the root index, article pages, the article template and the `SITE_NAME` constant in `tools/build_pdf.py`.

## Licence

Original editorial content is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code, styles and templates are available under the MIT License. Third-party material is excluded unless an item is explicitly marked otherwise.

See [LICENSE](LICENSE) for the exact scope and attribution requirements.
