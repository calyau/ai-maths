---
# === CORE IDENTIFICATION ===
concept: Linear Independence of Irreducible Characters
slug: linear-independence-of-characters

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
pdf_page: 115
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - irreducible-character
  - decomposition-of-f-g
extends: []
related:
  - characters-determine-representations
  - characters-basis-for-class-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are irreducible characters linearly independent?"
---

# Quick Definition

The irreducible characters chi_1, ..., chi_t are linearly independent over F: if sum c_i chi_i(g) = 0 for all g, then all c_i = 0.

# Core Definition

**Proposition 7.43.** The functions chi_1, ..., chi_t are linearly independent over F. The proof uses the central idempotents e_j of F[G] = M_{f_1}(F) x ... x M_{f_t}(F): chi_i(e_j) = f_j if i = j and 0 otherwise, so sum c_i chi_i(e_j) = c_j f_j, giving c_j = 0. (Milne, Proposition 7.43, p. 115)

# Prerequisites

- **Irreducible character** — the functions in question
- **Decomposition of F[G]** — provides the central idempotents

# Key Properties

1. Linear independence over F (not just over Z)
2. Since there are t irreducible characters and t conjugacy classes, they form a basis for class functions (7.47)
3. The proof uses the central idempotents e_j in F[G]

# Relationships

## Builds Upon
- **irreducible-character** — the linearly independent functions
- **decomposition-of-f-g** — provides the central idempotents

## Enables
- **characters-basis-for-class-functions** — since dim(class functions) = t = number of irreducible characters
- **characters-determine-representations** — linear independence implies unique decomposition

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.43, p. 115.

# Verification Notes

- Definition source: Direct from Proposition 7.43
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
