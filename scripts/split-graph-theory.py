#!/usr/bin/env python3
"""Split Diestel's 'Graph Theory' (3rd ed., 2005) into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/graph-theory"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
# Chapter boundaries determined by cross-referencing TOC page numbers
# with actual heading/content lines in book.md.
# Some chapters lack explicit "Chapter N" headings — they begin with
# introductory paragraphs before section N.1.
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Preface", 0, 1, 17),
    ("00b", "About the Second Edition", 0, 4, 62),
    ("00c", "About the Third Edition", 0, 5, 86),
    ("00d", "Contents", 0, 7, 111),
    ("01", "The Basics", 1, 11, 241),
    ("02", "Matching, Covering and Packing", 2, 43, 1203),
    ("03", "Connectivity", 3, 65, 1760),
    ("04", "Planar Graphs", 4, 94, 2452),
    ("05", "Colouring", 5, 122, 3222),
    ("06", "Flows", 6, 150, 3972),
    ("07", "Extremal Graph Theory", 7, 173, 4773),
    ("08", "Infinite Graphs", 8, 206, 5559),
    ("09", "Ramsey Theory for Graphs", 9, 261, 6798),
    ("10", "Hamilton Cycles", 10, 285, 7389),
    ("11", "Random Graphs", 11, 304, 7824),
    ("12", "Minors, Trees and WQO", 12, 325, 8433),
    ("13", "Appendix A - Infinite Sets", "A", 367, 9403),
    ("14", "Appendix B - Surfaces", "B", 374, 9477),
    ("15", "Hints for All the Exercises", 0, 379, 9646),
    ("16", "Index", 0, 403, 10105),
    ("17", "Symbol Index", 0, 419, 11001),
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
