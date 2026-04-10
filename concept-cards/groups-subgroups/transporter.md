---
# === CORE IDENTIFICATION ===
concept: Transporter
slug: transporter

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 67
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "T_G(Y, Z)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - normalizer
  - centralizer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The transporter T_G(Y, Z) of subfunctors Y into Z (with respect to a group action G x X -> X) is the functor R -> {g in G(R) | gY subset Z}. When Y is representable and Z is closed, T_G(Y, Z) is represented by a quotient of O(G).

# Core Definition

Let G be an affine monoid acting on a functor X, and let Y and Z be subfunctors of X. The **transporter** T_G(Y, Z) of Y into Z is the functor R -> {g in G(R) | gY(R') subset Z(R') for all R-algebras R'} (Section 6n, p. 67).

**Theorem 6.36** (p. 67): If Z is closed in X and Y is representable, then T_G(Y, Z) is represented by a quotient of O(G).

The transporter is the key technical tool for proving that normalizers and centralizers are affine subgroups.

# Prerequisites

- **Affine algebraic group** — The transporter is defined for group actions

# Key Properties

1. T_G(Y, Z) is represented by a quotient of O(G) under the given hypotheses
2. Used to construct normalizers: N_G(H) = T_G(H, H) intersected with T_G(H, H)^{-1}
3. Used to construct centralizers: C_G(H) = T_{G x G}(H, H) for diagonal embedding

# Relationships

## Enables
- **Normalizer** — N_G(H) uses the transporter
- **Centralizer** — C_G(H) uses the transporter

# Source Reference

Chapter I, Section 6n (p. 67), Theorem 6.36.

# Verification Notes

- Definition source: Direct from Section 6n
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
