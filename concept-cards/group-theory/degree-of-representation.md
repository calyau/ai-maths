---
# === CORE IDENTIFICATION ===
concept: Degree of a Representation
slug: degree-of-representation

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 100
section: "Matrix representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dimension of a representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends: []
related:
  - matrix-representation
  - decomposition-of-f-g
  - dimension-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the degree of a representation?"
  - "What determines the degree of an irreducible representation?"
---

# Quick Definition

The degree of a representation G -> GL(V) is dim_F(V). For a matrix representation G -> GL_n(F), the degree is n. For an irreducible character chi, chi(e) equals the degree.

# Core Definition

The **degree** of a matrix representation G -> GL_n(F) is n. Equivalently, for a linear representation G -> GL(V), the degree is dim_F(V). For an irreducible representation with character chi, the degree is chi(e) = dim_F(V). (Milne, Chapter 7, pp. 100, 113-114)

# Prerequisites

- **Linear representation** — the degree is its dimension

# Key Properties

1. degree = dim_F(V) = chi_V(e)
2. For irreducible representations S_i with degrees f_i: sum f_i^2 = |G| (7.41c)
3. Each f_i divides |G| (a deeper result)
4. The multiplicity of S_i in the regular representation equals f_i (7.41b)

# Examples

**Example 1** (p. 114): For S_3: degrees are 1, 1, 2 with 1 + 1 + 4 = 6 = |S_3|.

**Example 2** (p. 118): For D_4: degrees are 1, 1, 1, 1, 2 with 1 + 1 + 1 + 1 + 4 = 8 = |D_4|.

# Relationships

## Builds Upon
- **linear-representation** — degree is the dimension

## Enables
- **dimension-formula** — sum f_i^2 = |G|

## Related
- **character-of-a-representation** — chi(e) = degree

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 100, 113-114.

# Verification Notes

- Definition source: Direct from pp. 100, 114
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
