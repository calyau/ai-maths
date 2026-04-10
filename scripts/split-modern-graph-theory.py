#!/usr/bin/env python3
"""Split Bollobas's 'Modern Graph Theory' into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/modern-graph-theory"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Apologia", 0, 2, 7),
    ("00b", "Preface", 0, 4, 24),
    ("00c", "Contents", 0, 6, 51),
    ("01", "I. Fundamentals", 1, 9, 145),
    ("02", "II. Electrical Networks", 2, 46, 840),
    ("03", "III. Flows, Connectivity and Matching", 3, 74, 1387),
    ("04", "IV. Extremal Problems", 4, 110, 2134),
    ("05", "V. Colouring", 5, 152, 3223),
    ("06", "VI. Ramsey Theory", 6, 187, 3956),
    ("07", "VII. Random Graphs", 7, 221, 4756),
    ("08", "VIII. Graphs, Groups and Matrices", 8, 259, 5788),
    ("09", "IX. Random Walks on Graphs", 9, 300, 6742),
    ("10", "X. The Tutte Polynomial", 10, 340, 7859),
    ("11", "Symbol Index", 0, 384, 8921),
    ("12", "Name Index", 0, 386, 8982),
    ("13", "Subject Index", 0, 390, 9118),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    # Remove Roman numeral prefix like "I. " or "VIII. "
    title = re.sub(r"^[IVXLC]+\.\s*", "", title)
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(slug) > max_len:
        slug = slug[:max_len].rstrip("-")
    return slug


def main():
    lines = BOOK_MD.read_text().splitlines(keepends=True)
    total_lines = len(lines)

    print(f"Total lines in book.md: {total_lines}\n")

    for i, (prefix, title, chapter_num, pdf_page, md_line) in enumerate(CHAPTERS):
        start_idx = md_line - 1

        if i + 1 < len(CHAPTERS):
            end_idx = CHAPTERS[i + 1][4] - 1
        else:
            end_idx = total_lines

        content = "".join(lines[start_idx:end_idx])
        slug = slugify(title)
        filename = f"{prefix}-{slug}.md"

        header = (
            f"---\n"
            f"title: \"{title}\"\n"
            f"chapter_number: {chapter_num}\n"
            f"pdf_page: {pdf_page}\n"
            f"book_md_line: {md_line}\n"
            f"---\n\n"
        )

        out_path = SOURCES_DIR / filename
        out_path.write_text(header + content)
        line_count = content.count("\n")
        print(f"  {filename}: pdf page {pdf_page}, {line_count} lines")

    print(f"\nTotal files created: {len(CHAPTERS)}")


if __name__ == "__main__":
    print("Splitting book.md into chapters...\n")
    main()
