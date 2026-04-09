---
# === CORE IDENTIFICATION ===
concept: Character Table of S_3
slug: character-table-of-s3

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
pdf_page: 117
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
  - character-table-of-c3
  - character-table-of-d4
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character table of S_3?"
  - "How do I construct the character table of a finite group?"
---

# Quick Definition

The character table of S_3 has 3 conjugacy classes and 3 irreducible characters of degrees 1, 1, 2.

# Core Definition

**Example 7.54.** The character table of S_3 is:

|       | (1) | (12) | (123) |
|-------|-----|------|-------|
| chi_0 | 1   | 1    | 1     |
| chi_1 | 1   | -1   | 1     |
| chi_2 | 2   | 0    | -1    |

chi_0 is the trivial character. chi_1 sends a permutation to its sign. chi_2 is the character of the 2-dimensional irreducible representation. (Milne, Example 7.54, p. 117)

# Prerequisites

- **Character table** — this is a specific example

# Key Properties

1. Three conjugacy classes: {(1)}, {(12),(13),(23)}, {(123),(132)}
2. Three irreducible representations of degrees 1, 1, 2
3. 1^2 + 1^2 + 2^2 = 6 = |S_3|
4. Orthogonality can be verified: (chi_0|chi_1) = (1/6)(1-1+1-1+1+1) = 0, etc.

# Construction / Recognition

1. S_3 has 3 conjugacy classes, so 3 irreducible characters
2. Degrees satisfy f_1^2 + f_2^2 + f_3^2 = 6, giving (1,1,2)
3. chi_0 = trivial, chi_1 = sign character
4. chi_2 is found from the 2-dimensional representation (e.g., permutation representation minus trivial)

# Relationships

## Builds Upon
- **character-table** — an explicit example

## Enables
- Illustration of orthogonality relations
- Template for constructing other character tables

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.54, p. 117.

# Verification Notes

- Definition source: Direct from Example 7.54
- Confidence rationale: HIGH — explicit character table
- Uncertainties: None
