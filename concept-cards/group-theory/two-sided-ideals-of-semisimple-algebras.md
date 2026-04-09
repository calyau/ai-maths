---
# === CORE IDENTIFICATION ===
concept: Two-sided Ideals of Semisimple Algebras
slug: two-sided-ideals-of-semisimple-algebras

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 107
section: "Semisimple modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-f-algebra
  - isotypic-component
extends: []
related:
  - simple-f-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the two-sided ideals of a semisimple algebra?"
  - "How do two-sided ideals relate to isotypic components?"
---

# Quick Definition

In a semisimple F-algebra A, the minimal two-sided ideals are exactly the isotypic components of _A A. Every two-sided ideal is a direct sum of minimal two-sided ideals.

# Core Definition

**Proposition 7.17.** Let A be a semisimple F-algebra. The isotypic components of the A-module _A A are the minimal two-sided ideals of A. Every two-sided ideal of A is a direct sum of minimal two-sided ideals. The proof: two-sided ideals are left submodules stable under right multiplication (= under all endomorphisms of _A A, by 7.16), and by 7.15, these are exactly the sums of isotypic components. (Milne, Proposition 7.17, p. 107)

# Prerequisites

- **Semisimple F-algebra** — the algebra whose ideals are classified
- **Isotypic component** — the building blocks

# Key Properties

1. Minimal two-sided ideals = isotypic components of _A A
2. Every two-sided ideal = direct sum of minimal two-sided ideals
3. For A = A_1 x ... x A_t (simple factors): the A_i are the minimal two-sided ideals

# Relationships

## Builds Upon
- **semisimple-f-algebra** — the algebra
- **isotypic-component** — equals minimal two-sided ideals

## Related
- **simple-f-algebra** — the minimal two-sided ideals are simple algebras

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.17, p. 107.

# Verification Notes

- Definition source: Direct from Proposition 7.17
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
