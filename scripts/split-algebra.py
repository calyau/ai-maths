#!/usr/bin/env python3
"""Split Artin's 'Algebra' (2nd ed.) into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/algebra"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Preface", 0, 6, 216),
    ("01", "Matrices", 1, 12, 328),
    ("02", "Groups", 2, 48, 1427),
    ("03", "Vector Spaces", 3, 89, 2728),
    ("04", "Linear Operators", 4, 113, 3460),
    ("05", "Applications of Linear Operators", 5, 143, 4378),
    ("06", "Symmetry", 6, 162, 5103),
    ("07", "More Group Theory", 7, 206, 6225),
    ("08", "Bilinear Forms", 8, 240, 7242),
    ("09", "Linear Groups", 9, 264, 8207),
    ("10", "Group Representations", 10, 301, 9033),
    ("11", "Rings", 11, 339, 10103),
    ("12", "Factoring", 12, 370, 11129),
    ("13", "Quadratic Number Fields", 13, 394, 11836),
    ("14", "Linear Algebra in a Ring", 14, 432, 12705),
    ("15", "Fields", 15, 453, 13587),
    ("16", "Galois Theory", 16, 488, 14503),
    ("17", "Index", 0, 540, 16026),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
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
