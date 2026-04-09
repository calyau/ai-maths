#!/usr/bin/env python3
"""Split Martin-Lof's 'An Intuitionistic Theory of Types' into section files."""

import json
import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/intuitionistic-types"
BOOK_MD = SOURCES_DIR / "book.md"
METADATA_JSON = SOURCES_DIR / "metadata.json"

# Section mapping: (title, pdf_page, md_line_1indexed)
# Only top-level sections, not inline headings or subsections
SECTIONS = [
    ("1. Informal Explanations of the Basic Concepts", 0, 13),
    ("2. Formalization of an Intuitionistic Theory of Types", 9, 248),
    ("3. Reduction of Some Other Formal Theories to the Theory of Types", 24, 917),
    ("4. The Normalization Theorem and Its Consequences", 34, 1199),
    ("Bibliography", 45, 1383),
]


def slugify(title: str, max_len: int = 50) -> str:
    """Create a filename-safe slug from a title."""
    # Remove leading section numbers like "1. " or "2.4.2. "
    title = re.sub(r"^\d+(\.\d+)*\.?\s*", "", title)
    # Normalize unicode
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    # Lowercase, replace non-alnum with hyphens
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    # Truncate
    if len(slug) > max_len:
        slug = slug[:max_len].rstrip("-")
    return slug


def main():
    lines = BOOK_MD.read_text().splitlines(keepends=True)

    # Convert 1-indexed line numbers to 0-indexed
    split_points = [(title, pdf_page, ln - 1) for title, pdf_page, ln in SECTIONS]

    # Extract frontmatter: everything before section 1
    front_end = split_points[0][2]
    frontmatter = "".join(lines[:front_end])

    front_path = SOURCES_DIR / "00-frontmatter.md"
    front_header = (
        "---\n"
        "title: Frontmatter\n"
        "chapter_number: 0\n"
        "pdf_page: 0\n"
        "book_md_line: 1\n"
        "---\n\n"
    )
    front_path.write_text(front_header + frontmatter)
    print(f"  {front_path.name}: frontmatter (pdf page 0, {frontmatter.count(chr(10))} lines)")

    # Extract each section
    for i, (title, pdf_page, start_idx) in enumerate(split_points):
        if i + 1 < len(split_points):
            end_idx = split_points[i + 1][2]
        else:
            end_idx = len(lines)

        content = "".join(lines[start_idx:end_idx])
        chapter_num = i + 1
        slug = slugify(title)
        filename = f"{chapter_num:02d}-{slug}.md"

        header = (
            f"---\n"
            f"title: \"{title}\"\n"
            f"chapter_number: {chapter_num}\n"
            f"pdf_page: {pdf_page}\n"
            f"book_md_line: {start_idx + 1}\n"
            f"---\n\n"
        )

        out_path = SOURCES_DIR / filename
        out_path.write_text(header + content)
        line_count = content.count("\n")
        print(f"  {filename}: pdf page {pdf_page}, {line_count} lines")

    total = len(split_points) + 1  # sections + frontmatter
    print(f"\nTotal files created: {total} (1 frontmatter + {len(split_points)} sections)")


if __name__ == "__main__":
    print("Splitting book.md into sections...\n")
    main()
