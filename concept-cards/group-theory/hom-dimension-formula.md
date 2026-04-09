---
# === CORE IDENTIFICATION ===
concept: Hom Dimension Formula
slug: hom-dimension-formula

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
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-inner-product
  - fixed-point-subspace
extends: []
related:
  - orthogonality-relations
  - schur-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the dimension of Hom_{F[G]}(V,W) relate to the character inner product?"
---

# Quick Definition

For F[G]-modules V and W: dim_F Hom_{F[G]}(V, W) = (chi_V | chi_W).

# Core Definition

**Theorem 7.51.** For any F[G]-modules V and W, dim_F Hom_{F[G]}(V, W) = (chi_V | chi_W). The proof uses that Hom_{F[G]}(V,W) = Hom_F(V,W)^G and the fixed-point dimension formula (7.50). (Milne, Theorem 7.51, p. 117)

# Prerequisites

- **Character inner product** — the right-hand side
- **Fixed-point subspace** — the proof technique

# Key Properties

1. Relates algebraic (Hom space) to numerical (inner product) data
2. When V = W = S_i (simple): dim End_{F[G]}(S_i) = 1 (Schur's lemma over alg. closed field)
3. When V = S_i, W = S_j (i != j): Hom = 0
4. This immediately gives the orthogonality relations (7.52)

# Examples

**Example 1** (p. 117): For simple modules S_i, S_j: (chi_i|chi_j) = dim Hom(S_i, S_j) = delta_{ij}.

# Relationships

## Builds Upon
- **character-inner-product** — equated with Hom dimension
- **fixed-point-subspace** — proof technique

## Enables
- **orthogonality-relations** — immediate corollary

## Related
- **schur-lemma** — special case for simple modules

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.51, p. 117.

# Verification Notes

- Definition source: Direct from Theorem 7.51
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
