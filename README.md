# Engineering Marginalia

Notes in the margins of other people's research.

Each article takes published studies, industry surveys and engineering telemetry on a single software-engineering question, and works out what the evidence actually supports in practice. **Articles are written in Traditional Chinese with English technical terms kept in the original.** This README, the tooling and the templates are in English.

**Live site:** https://obafgkm42.github.io/engineering-marginalia/

A plain static site — no build step, no dependencies, no framework. One shared stylesheet, one folder per article.

---

## Articles

| Date | Title | |
| --- | --- | --- |
| 2026.08 | AI 寫的程式碼，工程師到底怎麼驗收？ · *How developers actually verify AI-generated code* | [Read](posts/2026-08-ai-coding-quality-assurance/) · [PDF](posts/2026-08-ai-coding-quality-assurance/ai-coding-quality-assurance.pdf) |

---

## Running it

Local preview:

```bash
python3 -m http.server 8000   # http://localhost:8000
```

Deploying to GitHub Pages: **Settings** → **Pages** → Source *Deploy from a branch* → branch `main`, folder `/ (root)`.

> Keep the empty `.nojekyll` file. Without it GitHub Pages runs Jekyll, and Jekyll ignores directories starting with an underscore — `posts/_template/` would silently disappear from the deployed site.

---

## Layout

```
.
├── index.html                  Article index — hand-maintained, edit when adding a post
├── assets/
│   └── style.css               The entire design system + print styles. The only stylesheet.
├── posts/
│   ├── _template/
│   │   └── index.html          Article template with an example of every component
│   └── 2026-08-ai-coding-quality-assurance/
│       ├── index.html
│       └── ai-coding-quality-assurance.pdf
├── tools/
│   └── build_pdf.py            Renders an article to an A4 PDF
├── .nojekyll
├── LICENSE
└── README.md
```

Naming convention: article directories are `YYYY-MM-english-slug`; the PDF drops the date prefix (`build_pdf.py` derives this automatically).

---

## Adding an article

```bash
cp -r posts/_template posts/2026-09-your-topic
```

1. Edit `posts/2026-09-your-topic/index.html` — `<title>`, the meta tags, and the `.mast` header (kicker, title, standfirst, the three meta fields). Write the body using the components in the template; delete whatever you don't use. **Always keep the 資料來源 (sources) section.**
2. Add an `<li>` at the **top** of `<ul class="postlist">` in `index.html`, copying the format of the existing entry.
3. Optional: `uv run tools/build_pdf.py posts/2026-09-your-topic/index.html`
4. Add a row to the Articles table above.
5. Commit and push — Pages redeploys automatically.

### Components

Every component below has a worked example in the template.

| Markup | Purpose |
| --- | --- |
| `<span class="en">term</span>` | An English technical term inside Chinese prose, set in mono. **The house typographic convention** — it lets terms be scanned out of a wall of Chinese text. |
| `.readouts` / `.ro` | Statistic cards. Add `.up` to turn the figure red (a metric getting worse), `.down` for amber. |
| `.note` / `.note.warn` / `.note.crit` | Callout box, three severities. |
| `.tw` wrapping a `<table>` | Table. The `.tw` wrapper provides horizontal scroll so wide tables never break the page on mobile. |
| `.ladder` / `.rung` | A stepped sequence — pipeline stages, CI gates. Only for things that genuinely have an order. |
| `.check` | Checklist with checkboxes. |
| `.src` + `.tag` | Source list. |

`.sec-num` numbering is for sections that are genuinely sequential or that readers will cite. If the content isn't a sequence, don't number it.

---

## PDFs

Requires [uv](https://docs.astral.sh/uv/). Chromium has to be fetched once:

```bash
uv run --with playwright==1.62.0 playwright install chromium
```

Then, per article:

```bash
uv run tools/build_pdf.py posts/<slug>/index.html
```

`tools/build_pdf.py` declares its dependency as [PEP 723](https://peps.python.org/pep-0723/) inline metadata and is locked in `tools/build_pdf.py.lock`, so uv builds the environment on demand — there is no venv, no `requirements.txt`, and nothing to install into your system Python. `.python-version` pins the interpreter for this repo.

The print layout lives in the `@media print` block of `assets/style.css`, so <kbd>Ctrl</kbd>+<kbd>P</kbd> in a browser produces the same pages. The script only adds the running footer and page numbers.

Chinese typefaces: the script uses whatever Noto Sans/Serif TC or Noto CJK is installed on the system. On Debian/Ubuntu: `sudo apt install fonts-noto-cjk`.

---

## Design system

- Everything runs through CSS custom properties. To reskin the site, edit the `:root` block and the two dark-mode blocks at the top of `assets/style.css` — nothing else.
- Three theme states are supported: explicit light, explicit dark, and follow-the-system. All three read from the same tokens, so keep them in sync when editing.
- Type: `Noto Serif TC` for headings, `Noto Sans TC` for body, `IBM Plex Mono` for terms, figures and labels. Loaded from Google Fonts as progressive enhancement, falling back to PingFang TC / Microsoft JhengHei when unavailable.
- Measure is ~720px; numeric columns use `tabular-nums`.

To rename the site, replace `Engineering Marginalia` in `index.html`, `posts/*/index.html`, `posts/_template/index.html` and the `SITE_NAME` constant in `tools/build_pdf.py`.

---

## Licence

- **Article content** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code, styles and templates** — MIT

See [LICENSE](LICENSE) for the full terms, including the third-party exception below.

---

## Editorial standards

These articles quote third-party research heavily. The following rules were followed when writing them and should be kept for anything added later.

**Where the line sits on quotation**

- Statistics are facts and aren't copyrightable. **Citing a figure, attributing it, and linking the original** is the safe pattern.
- Do **not** reproduce charts, screenshots or long passages from source reports. Vendor research (Veracode, LinearB, Faros, GitClear and similar) is typically all-rights-reserved and not licensed for redistribution.
- Some sources are more permissive and can be leaned on harder: Google/DORA publishes under CC BY 4.0 (attribution is enough); the Stack Overflow survey dataset is ODbL, which carries a share-alike obligation worth reading before reuse.

**What every article must carry**

- A sources section listing every citation with a link.
- Where vendor telemetry is cited, a note on the vendor's commercial interest and a reminder that **correlation is not causation**.
- The date range of the underlying data. Figures in this field go stale within about six months.

**Other**

- Tool and product names are used nominatively. That's fine, but nothing may imply endorsement — the footer disclaimer covers this and should stay.
- The AI-assistance disclosure in the footer stays. It isn't a legal requirement; it's what makes the numbers defensible when someone challenges them.
- If an article touches on your employer's work, check the internal publication policy before pushing.

> This section is a summary of practice, not legal advice.
