---
# === CORE IDENTIFICATION ===
concept: Character Table of C_3
slug: character-table-of-c3

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
  - representations-of-abelian-groups
extends: []
related:
  - character-table-of-s3
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character table of C_3?"
---

# Quick Definition

The character table of C_3 = {1, sigma, sigma^2} has three 1-dimensional representations with characters given by powers of zeta = e^{2pi i/3}.

# Core Definition

**Example 7.53.** The character table of C_3 (with zeta = e^{2pi i/3}) is:

|       | 1 | sigma | sigma^2 |
|-------|---|-------|---------|
| chi_0 | 1 | 1     | 1       |
| chi_1 | 1 | zeta  | zeta^2  |
| chi_2 | 1 | zeta^2| zeta    |

(Milne, Example 7.53, p. 117)

# Prerequisites

- **Character table** — this is a specific character table
- **Representations of abelian groups** — C_3 is abelian, so all irreducibles are 1-dimensional

# Key Properties

1. Three conjugacy classes (one for each element, since C_3 is abelian)
2. Three irreducible representations, all of degree 1
3. 1^2 + 1^2 + 1^2 = 3 = |C_3|
4. Each row is a group homomorphism C_3 -> C^x

# Relationships

## Builds Upon
- **character-table**, **representations-of-abelian-groups**

## Related
- **character-table-of-s3** — S_3 has C_3 as a normal subgroup

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.53, p. 117.

# Verification Notes

- Definition source: Direct from Example 7.53
- Confidence rationale: HIGH — explicit character table
- Uncertainties: None
