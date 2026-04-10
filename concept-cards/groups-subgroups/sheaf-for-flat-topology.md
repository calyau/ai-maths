---
# === CORE IDENTIFICATION ===
concept: Sheaf for the Flat Topology
slug: sheaf-for-flat-topology

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
pdf_page: 90
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fpqc sheaf

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-group
extends: []
related:
  - quotient-group-algebraic
  - surjective-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A functor F: Alg_k -> Set is a sheaf for the flat topology if it satisfies: (F1) F commutes with finite products, and (F2) for every faithfully flat R -> R', the sequence F(R) -> F(R') => F(R' tensor_R R') is exact. Every representable functor is a sheaf.

# Core Definition

A functor F: Alg_k -> Set satisfying conditions (F1) and (F2) is said to be a **sheaf for the flat topology** (fpqc topology) (Section 7k, p. 91):
- (F1) For every finite family of k-algebras (R_i), the canonical map F(product R_i) -> product F(R_i) is bijective
- (F2) For every faithfully flat R -> R', the sequence F(R) -> F(R') => F(R' tensor_R R') is exact

**Proposition 7.68**: Every representable functor is a sheaf.

**Proposition 7.73**: For a surjective homomorphism G -> Q with kernel N, Q represents the sheaf associated with the functor R -> G(R)/N(R).

# Prerequisites

- **Affine group** — Affine groups are sheaves

# Key Properties

1. Every representable functor is a sheaf (Proposition 7.68)
2. The associated sheaf aF exists for any functor F (Proposition 7.70)
3. Quotients G/N represent sheafifications of R -> G(R)/N(R)
4. Sheafification preserves finite inverse limits

# Relationships

## Related
- **Quotient group (algebraic)** — Quotients are sheafifications
- **Surjective homomorphism** — The sheaf perspective simplifies surjectivity

# Source Reference

Chapter I, Section 7k (p. 91-92), Propositions 7.68-7.73.

# Verification Notes

- Definition source: Direct from Section 7k
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
