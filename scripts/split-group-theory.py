#!/usr/bin/env python3
"""Split Milne's 'Group Theory' into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/group-theory"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Contents", 0, 2, 55),
    ("00b", "Notation and Acknowledgements", 0, 4, 126),
    ("01", "Basic Definitions and Results", 1, 6, 171),
    ("02", "Free Groups and Presentations; Coxeter Groups", 2, 30, 1110),
    ("03", "Automorphisms and Extensions", 3, 42, 1480),
    ("04", "Groups Acting on Sets", 4, 56, 1969),
    ("05", "The Sylow Theorems; Applications", 5, 76, 2704),
    ("06", "Subnormal Series; Solvable and Nilpotent Groups", 6, 86, 2985),
    ("07", "Representations of Finite Groups", 7, 100, 3467),
    ("08", "Appendix A - Additional Exercises", "A", 120, 4176),
    ("09", "Appendix B - Solutions to the Exercises", "B", 124, 4279),
    ("10", "Appendix C - Two-Hour Examination", "C", 132, 4443),
    ("11", "Bibliography", 0, 134, 4515),
    ("12", "Index", 0, 136, 4541),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    title = re.sub(r"^Appendix [A-Z] - ", "", title)
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
