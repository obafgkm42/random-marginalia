#!/usr/bin/env python3
"""
把一篇文章的 HTML 轉成 A4 PDF。

用法:
    python3 tools/build_pdf.py posts/2026-08-ai-coding-quality-assurance/index.html
    python3 tools/build_pdf.py posts/<slug>/index.html --out custom-name.pdf

排版規則來自 assets/style.css 的 @media print 區塊——瀏覽器 Ctrl+P 會得到
一樣的結果，這支腳本額外做的只有頁首頁尾與頁碼。

需求:
    pip install playwright && playwright install chromium

中文字型: 優先使用系統上的 Noto Sans/Serif TC 或 Noto CJK。若都沒有，
先安裝 (Debian/Ubuntu): sudo apt install fonts-noto-cjk
"""

import argparse
import pathlib
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("需要 playwright：pip install playwright && playwright install chromium")

SITE_NAME = "Engineering Marginalia"

FOOTER = (
    '<div style="width:100%;font-family:\'IBM Plex Mono\',monospace;font-size:7.5pt;'
    'color:#8A99A3;padding:0 16mm;display:flex;justify-content:space-between;">'
    f"<span>{SITE_NAME}</span>"
    '<span><span class="pageNumber"></span>&nbsp;/&nbsp;<span class="totalPages"></span></span>'
    "</div>"
)


def build(html_path: pathlib.Path, out_path: pathlib.Path) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox", "--font-render-hinting=none"])
        page = browser.new_page()
        # networkidle：等 Google Fonts 載完；離線時會 timeout 後照樣以系統字型輸出
        try:
            page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=20000)
        except Exception:
            page.goto(html_path.resolve().as_uri(), wait_until="load")
        page.emulate_media(media="print")
        page.pdf(
            path=str(out_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=FOOTER,
            margin={"top": "18mm", "bottom": "20mm", "left": "16mm", "right": "16mm"},
        )
        browser.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="把文章 HTML 轉成 A4 PDF")
    ap.add_argument("html", help="文章的 index.html 路徑")
    ap.add_argument("--out", help="輸出檔名，預設為 <資料夾名>.pdf 放在同一層")
    args = ap.parse_args()

    html_path = pathlib.Path(args.html)
    if not html_path.is_file():
        sys.exit(f"找不到檔案：{html_path}")

    out_path = (
        pathlib.Path(args.out)
        if args.out
        else html_path.parent / f"{html_path.parent.name.split('-', 2)[-1]}.pdf"
    )

    build(html_path, out_path)
    size_kb = out_path.stat().st_size / 1024
    print(f"✓ {out_path}  ({size_kb:,.0f} KB)")


if __name__ == "__main__":
    main()
