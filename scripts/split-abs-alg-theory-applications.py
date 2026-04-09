#!/usr/bin/env python3
"""Split Judson's 'Abstract Algebra: Theory and Applications' into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/abs-alg-theory-applications"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Acknowledgements", 0, 5, 43),
    ("00b", "Preface", 0, 6, 62),
    ("00c", "Contents", 0, 9, 82),
    ("01", "Preliminaries", 1, 14, 269),
    ("02", "The Integers", 2, 30, 903),
    ("03", "Groups", 3, 41, 1315),
    ("04", "Cyclic Groups", 4, 59, 1869),
    ("05", "Permutation Groups", 5, 72, 2425),
    ("06", "Cosets and Lagrange's Theorem", 6, 87, 2953),
    ("07", "Introduction to Cryptography", 7, 94, 3210),
    ("08", "Algebraic Coding Theory", 8, 104, 3514),
    ("09", "Isomorphisms", 9, 127, 4282),
    ("10", "Normal Subgroups and Factor Groups", 10, 138, 4702),
    ("11", "Homomorphisms", 11, 146, 4988),
    ("12", "Matrix Groups and Symmetry", 12, 154, 5271),
    ("13", "The Structure of Groups", 13, 171, 5788),
    ("14", "Group Actions", 14, 181, 6162),
    ("15", "The Sylow Theorems", 15, 195, 6638),
    ("16", "Rings", 16, 204, 6890),
    ("17", "Polynomials", 17, 223, 7608),
    ("18", "Integral Domains", 18, 239, 8291),
    ("19", "Lattices and Boolean Algebras", 19, 252, 8723),
    ("20", "Vector Spaces", 20, 266, 9197),
    ("21", "Fields", 21, 274, 9476),
    ("22", "Finite Fields", 22, 292, 10097),
    ("23", "Galois Theory", 23, 307, 10568),
    ("24", "GNU Free Documentation License", 0, 325, 11150),
    ("25", "Hints and Answers to Selected Exercises", 0, 332, 11278),
    ("26", "Notation", 0, 346, 11852),
    ("27", "Index", 0, 349, 11970),
    ("28", "Colophon", 0, 355, 12396),
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
