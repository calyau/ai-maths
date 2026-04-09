---
# === CORE IDENTIFICATION ===
concept: Character Table of D_4
slug: character-table-of-d4

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 118
section: "The character table of a group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-table
extends: []
related:
  - character-table-of-q8
  - character-table-does-not-determine-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character table of D_4?"
  - "How do I construct the character table of a finite group?"
---

# Quick Definition

The character table of D_4 has 5 conjugacy classes and 5 irreducible characters of degrees 1, 1, 1, 1, 2. It is identical to the character table of Q_8.

# Core Definition

**Example 7.55.** D_4 = <a, b | a^4 = b^2 = 1, bab^{-1} = a^{-1}>. The conjugacy classes are {1}, {a^2}, {a, a^3}, {b, a^2 b}, {ab, a^3 b}. The four 1-dimensional characters assign +/-1 to a and b. The 2-dimensional representation sends a to diag(i, -i) and b to the matrix ((0,1),(1,0)). The character table is:

|       | 1 | a^2 | a  | b  | ab |
|-------|---|-----|----|----|----|
| chi_0 | 1 | 1   | 1  | 1  | 1  |
| chi_1 | 1 | 1   | 1  | -1 | -1 |
| chi_2 | 1 | 1   | -1 | 1  | -1 |
| chi_3 | 1 | 1   | -1 | -1 | 1  |
| chi_4 | 2 | -2  | 0  | 0  | 0  |

(Milne, Example 7.55, p. 118)

# Prerequisites

- **Character table** — this is a specific example

# Key Properties

1. Five conjugacy classes, five irreducible representations
2. Degrees: 1, 1, 1, 1, 2 with 4 + 4 = 8 = |D_4|
3. Same character table as Q_8 (Example 7.56)
4. The four 1-dimensional characters come from the relation a^2 = 1 in the abelianization

# Relationships

## Builds Upon
- **character-table** — an explicit example

## Related
- **character-table-of-q8** — identical character table
- **character-table-does-not-determine-group** — D_4 and Q_8 are the key example

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.55, p. 118.

# Verification Notes

- Definition source: Direct from Example 7.55
- Confidence rationale: HIGH — explicit character table
- Uncertainties: None
