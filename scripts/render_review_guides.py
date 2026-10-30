"""Render the editable Grover review guides to PDFs (maintainer tool only).

Install reportlab and pypdf in a separate tooling environment. The classroom
dependency pins are unchanged. Explicit pagebreak markers in the Markdown
sources keep the three-page setup and two-page instructor guides synchronized.
"""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import re
from urllib.parse import urlparse

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor("#12334A")
TEAL = colors.HexColor("#007E87")
INK = colors.HexColor("#23333F")
LIGHT = colors.HexColor("#F0F5F7")


def fonts() -> tuple[str, str, str]:
    folder = Path("/usr/share/fonts/truetype/dejavu")
    paths = [folder / name for name in (
        "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSansMono.ttf",
    )]
    if all(path.exists() for path in paths):
        for name, path in zip(("Guide", "GuideBold", "GuideMono"), paths):
            pdfmetrics.registerFont(TTFont(name, str(path)))
        pdfmetrics.registerFontFamily("Guide", normal="Guide", bold="GuideBold")
        return "Guide", "GuideBold", "GuideMono"
    return "Helvetica", "Helvetica-Bold", "Courier"


def inline(text: str, mono: str) -> str:
    """Escape prose and render the limited inline Markdown used by the guides."""
    pattern = re.compile(r"(\[[^\]]+\]\(https://[^)]+\)|`[^`]+`|\*\*[^*]+\*\*)")
    parts = []
    for token in pattern.split(text):
        if token.startswith("[") and "](https://" in token:
            label, url = token[1:].split("](", 1)
            parts.append(f'<link href="{escape(url[:-1], quote=True)}" color="#007E87">{escape(label)}</link>')
        elif token.startswith("`") and token.endswith("`"):
            parts.append(f'<font name="{mono}" size="8.3">{escape(token[1:-1])}</font>')
        elif token.startswith("**") and token.endswith("**"):
            parts.append(f"<b>{escape(token[2:-2])}</b>")
        else:
            parts.append(escape(token))
    return "".join(parts)


def build_story(markdown: str, regular: str, bold: str, mono: str):
    body = ParagraphStyle("Body", fontName=regular, fontSize=9.3, leading=13.1,
                          textColor=INK, spaceAfter=6, alignment=TA_LEFT)
    styles = {
        "title": ParagraphStyle("Title", parent=body, fontName=bold, fontSize=20,
                                leading=24, textColor=NAVY, spaceAfter=9),
        "h2": ParagraphStyle("Heading", parent=body, fontName=bold, fontSize=11.7,
                             leading=15, textColor=TEAL, spaceBefore=10, spaceAfter=5,
                             keepWithNext=True),
        "body": body,
        "bullet": ParagraphStyle("Bullet", parent=body, leftIndent=12,
                                 firstLineIndent=-8, spaceAfter=5),
        "callout": ParagraphStyle("Callout", parent=body, fontName=bold,
                                  backColor=LIGHT, borderColor=TEAL, borderWidth=0.6,
                                  borderPadding=7, spaceBefore=4, spaceAfter=10),
    }
    story = []
    paragraph = []
    code = []
    in_code = False
    new_page = True

    def flush():
        if paragraph:
            story.append(Paragraph(inline(" ".join(paragraph), mono), styles["body"]))
            paragraph.clear()

    for line in markdown.splitlines():
        if line.startswith("```"):
            flush()
            if in_code:
                block = Preformatted("\n".join(code), ParagraphStyle(
                    "Code", fontName=mono, fontSize=7.8, leading=10.5, textColor=INK,
                ))
                table = Table([[block]], colWidths=[510])
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]))
                story.extend([table, Spacer(1, 7)])
                code.clear()
            in_code = not in_code
        elif in_code:
            code.append(line)
        elif line == "<!-- pagebreak -->":
            flush()
            story.append(PageBreak())
            new_page = True
        elif line.startswith("# "):
            flush()
            story.append(Paragraph(inline(line[2:], mono), styles["title"]))
            new_page = False
        elif line.startswith("## "):
            flush()
            # Page-opening H2s render as visual titles without adding Markdown H1s.
            story.append(Paragraph(inline(line[3:], mono), styles["title" if new_page else "h2"]))
            new_page = False
        elif line.startswith("> "):
            flush()
            story.append(Paragraph(inline(line[2:], mono), styles["callout"]))
        elif line.startswith("- "):
            flush()
            story.append(Paragraph(inline(line[2:], mono), styles["bullet"], bulletText="-"))
        elif not line.strip():
            flush()
        else:
            paragraph.append(line.strip())
    flush()
    if in_code:
        raise ValueError("Unclosed code fence in guide source.")
    return story


def render(source: Path, output: Path, *, tests: int | None, download_url: str | None,
           expected_pages: int) -> None:
    regular, bold, mono = fonts()
    markdown = source.read_text(encoding="utf-8")
    download_note = (
        f"Versioned preview download: [standalone ZIP]({download_url})."
        if download_url else
        "PUBLIC DOWNLOAD NOT YET AVAILABLE. Obtain the standalone ZIP from the instructor."
    )
    test_summary = f"{tests} passing offline tests" if tests else "all offline tests passing"
    markdown = markdown.replace("{{DOWNLOAD_NOTE}}", download_note).replace("{{TEST_SUMMARY}}", test_summary)
    if "{{" in markdown or "}}" in markdown:
        raise ValueError(f"Unresolved template value in {source.name}")
    output.parent.mkdir(parents=True, exist_ok=True)

    def furniture(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(TEAL)
        canvas.setLineWidth(1.2)
        canvas.line(45, 758, 567, 758)
        canvas.setFont(bold, 8.3)
        canvas.setFillColor(NAVY)
        canvas.drawString(45, 768, "UTC PHYS 3810  /  FALL 2026")
        canvas.setFont(regular, 7.7)
        canvas.setFillColor(colors.HexColor("#5E6E78"))
        canvas.drawString(45, 25, "REVIEW DRAFT v0.1  |  October 29, 2026")
        canvas.drawRightString(567, 25, f"{doc.page} / {expected_pages}")
        canvas.restoreState()

    document = SimpleDocTemplate(
        str(output), pagesize=letter, rightMargin=45, leftMargin=45,
        topMargin=47, bottomMargin=45, title=source.stem.replace("_", " "),
        author="PHYS 3810 teaching materials", subject="Grover preview review draft v0.1",
    )
    document.build(build_story(markdown, regular, bold, mono),
                   onFirstPage=furniture, onLaterPages=furniture)
    reader = PdfReader(output)
    if len(reader.pages) != expected_pages:
        raise RuntimeError(f"{output.name}: expected {expected_pages} pages; got {len(reader.pages)}")
    for page in reader.pages:
        text = page.extract_text() or ""
        if not text.strip() or "{{" in text:
            raise RuntimeError(f"Empty page or unresolved template in {output.name}")
        for annotation in page.get("/Annots", []):
            rectangle = annotation.get_object().get("/Rect")
            if rectangle and not (0 <= rectangle[0] < rectangle[2] <= 612
                                  and 0 <= rectangle[1] < rectangle[3] <= 792):
                raise RuntimeError(f"Out-of-page link in {output.name}: {rectangle}")
    print(f"Created {output} ({len(reader.pages)} pages)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tests", type=int, help="Executed Grover-preview unit-test count.")
    parser.add_argument("--download-url", help="Actual published HTTPS ZIP URL; omit for an unpublished draft.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "output" / "pdf")
    args = parser.parse_args()
    if args.tests is not None and args.tests < 1:
        parser.error("--tests must be positive")
    if args.download_url:
        url = urlparse(args.download_url)
        if url.scheme != "https" or not url.netloc:
            parser.error("--download-url must be an HTTPS URL")
    for source_name, output_name, pages in (
        ("SETUP_REVIEW_DRAFT.md", "PHYS3810_Setup_Review_Draft_2026-10-29.pdf", 3),
        ("INSTRUCTOR_REVIEW_DRAFT.md", "PHYS3810_Grover_Instructor_Review_Draft_2026-10-29.pdf", 2),
    ):
        render(ROOT / "teaching" / "phys3810-fa2026" / "preview" / source_name,
               args.output_dir / output_name, tests=args.tests,
               download_url=args.download_url, expected_pages=pages)


if __name__ == "__main__":
    main()
