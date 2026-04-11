#!/usr/bin/env python3
"""Split Dummit & Foote's 'Abstract Algebra' (3rd ed.) into part-level files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/abs-alg"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Contents", 0, 7, 194),
    ("00b", "Preface to the Third Edition", 0, 12, 364),
    ("00c", "Preliminaries", 0, 14, 388),
    ("01", "Part I - Group Theory", 1, 26, 780),
    ("02", "Part II - Ring Theory", 2, 235, 6850),
    ("03", "Part III - Modules and Vector Spaces", 3, 349, 9735),
    ("04", "Part IV - Field Theory and Galois Theory", 4, 522, 14671),
    ("05", "Part V - Commutative Rings and Algebraic Geometry", 5, 668, 18986),
    ("06", "Part VI - Further Topics", 6, 852, 23779),
    ("07", "Appendix I - Cartesian Products and Zorn's Lemma", "A1", 905, 25559),
    ("08", "Appendix II - Category Theory", "A2", 911, 25722),
    ("09", "Index", 0, 919, 25921),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    # Remove "Part N - " or "Appendix N - " prefix
    title = re.sub(r"^(Part [IVX]+ - |Appendix [IVX]+ - )", "", title)
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
    print("Splitting book.md into parts...\n")
    main()
