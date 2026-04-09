#!/usr/bin/env python3
"""Split Kirillov's 'Introduction to Lie Groups and Lie Algebras' into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/intro-lie-groups"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
# chapter_number is int for chapters, string for appendices, 0 for non-chapter sections
CHAPTERS = [
    # Frontmatter: lines 1-8 (title + author)
    ("00", "Frontmatter", 0, 0, 1),
    # Contents: lines 9-112
    ("00b", "Contents", 0, 2, 9),
    # Chapters
    ("01", "Introduction", 1, 6, 113),
    ("02", "Lie Groups: Basic Definitions", 2, 8, 142),
    ("03", "Lie Groups and Lie Algebras", 3, 20, 505),
    ("04", "Representations of Lie Groups and Lie Algebras", 4, 38, 1149),
    ("05", "Representations of sl(2,C) and Spherical Laplace Operator", 5, 58, 1814),
    ("06", "Structure Theory of Lie Algebras", 6, 66, 2126),
    ("07", "Complex Semisimple Lie Algebras", 7, 82, 2684),
    ("08", "Root Systems", 8, 90, 2994),
    ("09", "Representations of Semisimple Lie Algebras", 9, 110, 3718),
    ("10", "Appendix A - Manifolds and Immersions", "A", 118, 3959),
    ("11", "Appendix B - Jordan Decomposition", "B", 120, 3963),
    ("12", "Appendix C - Root Systems and Simple Lie Algebras", "C", 122, 4020),
    ("13", "List of Notation", 0, 130, 4316),
    ("14", "Index", 0, 132, 4350),
    ("15", "Bibliography", 0, 134, 4421),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    # Remove "Appendix X - " prefix
    title = re.sub(r"^Appendix [A-Z] - ", "", title)
    # Normalize unicode
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    # Lowercase, replace non-alnum with hyphens
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(slug) > max_len:
        slug = slug[:max_len].rstrip("-")
    return slug


def main():
    lines = BOOK_MD.read_text().splitlines(keepends=True)
    total_lines = len(lines)

    print(f"Total lines in book.md: {total_lines}\n")

    for i, (prefix, title, chapter_num, pdf_page, md_line) in enumerate(CHAPTERS):
        start_idx = md_line - 1  # convert to 0-indexed

        if i + 1 < len(CHAPTERS):
            end_idx = CHAPTERS[i + 1][4] - 1  # next chapter's start (0-indexed)
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
