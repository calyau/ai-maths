---
# === CORE IDENTIFICATION ===
concept: Dimension of an Algebraic Group
slug: dimension-of-algebraic-group

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 59
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - dim G

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - coordinate-ring
extends: []
related:
  - exact-sequence-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The dimension of an algebraic group G is the Krull dimension of O(G). When O(G) is an integral domain, this equals the transcendence degree of the fraction field over k.

# Core Definition

The **dimension** of an algebraic group G is defined to be the Krull dimension of O(G) (Summary 6.11, p. 59). When O(G) is an integral domain (which holds when G is smooth and connected), this equals the transcendence degree of O(G) over k.

**Dimension formula** (Proposition 7.60, p. 88): For an exact sequence 1 -> N -> G -> Q -> 1, dim G = dim N + dim Q.

# Prerequisites

- **Affine algebraic group** — Dimension is a property of algebraic groups
- **Coordinate ring** — dim G = Krull dimension of O(G)

# Key Properties

1. dim G = Krull dimension of O(G)
2. For smooth connected G: dim G = transcendence degree of Frac(O(G)) over k
3. dim(G x H) = dim G + dim H
4. dim G = dim N + dim Q for exact sequences
5. dim H <= dim G for any subgroup H; strict inequality when G is smooth and connected and H != G (Proposition 6.24)

# Examples

**Example 1**: dim(G_a) = 1, dim(G_m) = 1, dim(GL_n) = n^2, dim(SL_n) = n^2 - 1.

**Example 2**: dim(A^n) = n (transcendence degree of k(X_1,...,X_n) over k).

# Relationships

## Related
- **Exact sequence (algebraic groups)** — dim G = dim N + dim Q

# Source Reference

Chapter I, 6.10 (p. 58), Summary 6.11 (p. 59), Proposition 7.60 (p. 88).

# Verification Notes

- Definition source: Direct from 6.10 and Summary 6.11
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
