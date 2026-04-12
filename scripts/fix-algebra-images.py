#!/usr/bin/env python3
"""Fix image references in book.md to point to ./images/ subdirectory."""

import re
from pathlib import Path

SOURCES_DIR = Path.home() / "Dropbox/Apps/sources-md/maths/algebra"
BOOK_MD = SOURCES_DIR / "book.md"

content = BOOK_MD.read_text()

pattern = r"!\[([^\]]*)\]\((_page_)"
replacement = r"![\1](./images/\2"

new_content, count = re.subn(pattern, replacement, content)

BOOK_MD.write_text(new_content)
print(f"Updated {count} image references in {BOOK_MD}")
