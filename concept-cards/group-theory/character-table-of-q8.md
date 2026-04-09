---
# === CORE IDENTIFICATION ===
concept: Character Table of Q_8
slug: character-table-of-q8

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
pdf_page: 119
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
  - character-table-of-d4
  - character-table-does-not-determine-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character table of Q_8?"
  - "Why do D_4 and Q_8 have the same character table?"
---

# Quick Definition

The character table of Q_8 = {+/-1, +/-i, +/-j, +/-k} is identical to that of D_4, demonstrating that the character table does not determine the group.

# Core Definition

**Example 7.56.** Q_8 = <a, b | a^4 = 1, b^2 = a^2, b^{-1}ab = a^{-1}> where a = i, b = j. The conjugacy classes are {1}, {a^2 = -1}, {a, a^3 = +/-i}, {b, a^2 b = +/-j}, {ab, a^3 b = +/-k}. The character table is exactly the same as that of D_4. (Milne, Example 7.56, p. 119)

# Prerequisites

- **Character table** — this is a specific example

# Key Properties

1. Same character table as D_4 (identical 5x5 matrix)
2. Q_8 is not isomorphic to D_4 (e.g., Q_8 has a unique element of order 2, while D_4 has several)
3. The 2-dimensional representation uses the standard matrix representation of quaternions
4. This is the smallest example of non-isomorphic groups with the same character table

# Relationships

## Builds Upon
- **character-table** — an explicit example

## Related
- **character-table-of-d4** — identical character table
- **character-table-does-not-determine-group** — the canonical example

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.56, p. 119.

# Verification Notes

- Definition source: Direct from Example 7.56
- Confidence rationale: HIGH — explicit character table
- Uncertainties: None
