# Engineering Marginalia

Evidence-led notes on software engineering practice.

Each article starts with a focused engineering question, reviews published research, industry surveys and engineering telemetry, then separates what the evidence shows from what teams can reasonably do in practice.

- **Language:** Traditional Chinese, with English technical terms kept in the original
- **Format:** a dependency-free static site, plus optional PDFs
- **Live site:** <https://obafgkm42.github.io/engineering-marginalia/>

## Articles

| Date | Article | Formats |
| --- | --- | --- |
| 2026.08 | AI 寫的程式碼，工程師到底怎麼驗收？ · *How developers actually verify AI-generated code* | [Web](posts/2026-08-ai-coding-quality-assurance/) · [PDF](posts/2026-08-ai-coding-quality-assurance/ai-coding-quality-assurance.pdf) |

## Repository structure

```text
.
├── index.html                 Article index; update it when publishing a post
├── assets/style.css           Shared screen and print styles
├── posts/
│   ├── _template/index.html   Reusable article template
│   └── YYYY-MM-topic/
│       ├── index.html
│       └── topic.pdf          Optional generated PDF
├── tools/build_pdf.py         Playwright-based PDF renderer
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
3. Add the new article to `index.html` and to the table above.
4. Complete the [pre-publication checklist](COMPLIANCE.md#pre-publication-checklist).
5. Optionally generate and inspect a PDF.
6. Commit and push; GitHub Pages redeploys automatically.

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

For Traditional Chinese text, install Noto CJK fonts if the host does not already provide compatible fonts. On Debian or Ubuntu:

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

## Design notes

- Colour, typography and spacing are CSS custom properties in `assets/style.css`.
- Light, dark and system themes use the same token names and should be updated together.
- Headings use `Noto Serif TC`, body text uses `Noto Sans TC`, and terms and figures use `IBM Plex Mono`, with local fallbacks.
- The reading measure is about 720 px; numeric columns use `tabular-nums`.

To rename the site, replace `Engineering Marginalia` in the root index, article pages, the article template and the `SITE_NAME` constant in `tools/build_pdf.py`.

## Licence

Original editorial content is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code, styles and templates are available under the MIT License. Third-party material is excluded unless an item is explicitly marked otherwise.

See [LICENSE](LICENSE) for the exact scope and attribution requirements.
