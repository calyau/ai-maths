#!/usr/bin/env python3
"""Split Armstrong's 'Groups and Symmetry' into chapter files."""

import re
import unicodedata
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/groups-symmetry"
BOOK_MD = SOURCES_DIR / "book.md"

# (file_prefix, title, chapter_number, pdf_page, md_line_1indexed)
CHAPTERS = [
    ("00", "Frontmatter", 0, 0, 1),
    ("00a", "Preface", 0, 3, 90),
    ("00b", "Contents", 0, 5, 112),
    ("01", "Symmetries of the Tetrahedron", 1, 8, 188),
    ("02", "Axioms", 2, 13, 241),
    ("03", "Numbers", 3, 18, 338),
    ("04", "Dihedral Groups", 4, 22, 443),
    ("05", "Subgroups and Generators", 5, 27, 583),
    ("06", "Permutations", 6, 33, 718),
    ("07", "Isomorphisms", 7, 39, 880),
    ("08", "Plato's Solids and Cayley's Theorem", 8, 44, 998),
    ("09", "Matrix Groups", 9, 51, 1089),
    ("10", "Products", 10, 59, 1285),
    ("11", "Lagrange's Theorem", 11, 64, 1418),
    ("12", "Partitions", 12, 68, 1513),
    ("13", "Cauchy's Theorem", 13, 75, 1648),
    ("14", "Conjugacy", 14, 80, 1780),
    ("15", "Quotient Groups", 15, 86, 1951),
    ("16", "Homomorphisms", 16, 93, 2157),
    ("17", "Actions, Orbits, and Stabilizers", 17, 98, 2276),
    ("18", "Counting Orbits", 18, 105, 2428),
    ("19", "Finite Rotation Groups", 19, 111, 2547),
    ("20", "The Sylow Theorems", 20, 120, 2685),
    ("21", "Finitely Generated Abelian Groups", 21, 126, 2836),
    ("22", "Row and Column Operations", 22, 132, 3012),
    ("23", "Automorphisms", 23, 138, 3223),
    ("24", "The Euclidean Group", 24, 143, 3345),
    ("25", "Lattices and Point Groups", 25, 152, 3582),
    ("26", "Wallpaper Patterns", 26, 162, 3757),
    ("27", "Free Groups and Presentations", 27, 173, 4049),
    ("28", "Trees and the Nielsen-Schreier Theorem", 28, 180, 4257),
    ("29", "Bibliography", 0, 188, 4390),
    ("30", "Index", 0, 190, 4415),
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
