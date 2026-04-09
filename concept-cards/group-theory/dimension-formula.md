---
# === CORE IDENTIFICATION ===
concept: Dimension Formula for Representations
slug: dimension-formula

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
pdf_page: 113
section: "The representations of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "sum of squares formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - decomposition-of-f-g
  - degree-of-representation
extends: []
related:
  - number-of-irreducible-representations
  - character-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the relation between degrees of irreducible representations and the group order?"
  - "What does sum f_i^2 = |G| mean?"
---

# Quick Definition

If f_1, ..., f_t are the degrees of the irreducible representations of G over an algebraically closed field of characteristic zero, then sum_{i=1}^t f_i^2 = |G|.

# Core Definition

**Theorem 7.41(c).** Let S_1, ..., S_t be representatives for the isomorphism classes of simple F[G]-modules, and let f_i = dim_F S_i. Then sum_{1 <= i <= t} f_i^2 = |G|. This is simply the statement sum dim_F M_{f_i}(F) = dim_F F[G]. (Milne, Theorem 7.41c, p. 114)

# Prerequisites

- **Decomposition of F[G]** — F[G] = M_{f_1}(F) x ... x M_{f_t}(F)
- **Degree of representation** — the f_i

# Key Properties

1. sum f_i^2 = |G| (a dimension count)
2. This constrains the possible degrees: e.g., for |G| = 6, t = 3, the only solution is (1,1,2)
3. Each f_i >= 1 (representations are nonzero)
4. f_i = 1 iff S_i is 1-dimensional (there are [G:G'] such)

# Examples

**Example 1**: S_3: 1^2 + 1^2 + 2^2 = 6. **Example 2**: D_4: 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 8. **Example 3**: A_4: 1^2 + 1^2 + 1^2 + 3^2 = 12.

# Relationships

## Builds Upon
- **decomposition-of-f-g** — the algebraic source of the formula

## Enables
- Constraining possible character tables
- **character-table** — first step in construction

## Related
- **number-of-irreducible-representations** — t = number of conjugacy classes

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.41(c), p. 114.

# Verification Notes

- Definition source: Direct from Theorem 7.41(c)
- Confidence rationale: HIGH — explicit formula
- Uncertainties: None
