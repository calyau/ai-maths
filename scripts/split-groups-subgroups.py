#!/usr/bin/env python3
"""Split Milne's 'Algebraic Groups, Lie Groups, and their Arithmetic Subgroups'
into part-level files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/groups-subgroups"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
# Split at Part level since the book has 6 major Parts plus front/back matter
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Table of Contents", 0, 2, 36),
    ("00b", "Preface", 0, 4, 120),
    ("00c", "Terminology", 0, 5, 154),
    ("00d", "Dramatis Personae", 0, 10, 290),
    ("01", "I. Basic Theory of Affine Groups", 1, 12, 330),
    ("02", "II. Lie Algebras and Algebraic Groups", 2, 238, 9083),
    ("03", "III. The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero", 3, 294, 11450),
    ("04", "IV. Lie Groups", 4, 326, 12606),
    ("05", "V. The Structure of Reductive Groups: The Split Case", 5, 332, 12794),
    ("06", "VI. The Structure of Reductive Groups: General Case", 6, 382, 14750),
    ("07", "VII. Arithmetic Subgroups", 7, 396, 15266),
    ("08", "Bibliography", 0, 412, 15912),
    ("09", "Index", 0, 418, 16010),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    # Remove Roman numeral prefix like "I. " or "VII. "
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
    print("Splitting book.md into parts...\n")
    main()
