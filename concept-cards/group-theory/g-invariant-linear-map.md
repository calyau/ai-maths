---
# === CORE IDENTIFICATION ===
concept: G-invariant Linear Map
slug: g-invariant-linear-map

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
pdf_page: 102
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "G-equivariant map"
  - "intertwining operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends: []
related:
  - g-invariant-subspace
  - schur-lemma
  - hom-dimension-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a G-invariant linear map?"
  - "What is a G-equivariant map between representations?"
---

# Quick Definition

An F-linear map alpha: V -> V' between representation spaces is G-invariant (G-equivariant) if alpha(gv) = g(alpha(v)) for all g in G and v in V. Equivalently, it is an F[G]-module homomorphism.

# Core Definition

An F-linear map alpha: V -> V' of vector spaces on which G acts linearly is said to be **G-invariant** if alpha(gv) = g(alpha(v)) for all g in G, v in V. (Milne, Chapter 7, p. 102)

# Prerequisites

- **Linear representation** — G-invariant maps are between representation spaces

# Key Properties

1. G-invariant linear maps = F[G]-module homomorphisms
2. The kernel and image of a G-invariant map are G-invariant subspaces
3. Schur's lemma: a nonzero G-invariant map between irreducible representations is an isomorphism
4. Hom_{F[G]}(V,W)^G = Hom_{F[G]}(V,W) (Theorem 7.51)

# Examples

**Example 1** (p. 102): A projector pi: V -> V is G-invariant iff both its image and kernel are G-invariant subspaces.

# Relationships

## Builds Upon
- **linear-representation** — maps between representations

## Enables
- **schur-lemma** — about G-invariant endomorphisms of simple modules
- **hom-dimension-formula** — dim Hom_{F[G]}(V,W) = (chi_V|chi_W)

## Related
- **g-invariant-subspace** — kernels and images are G-invariant

# Source Reference

Chapter 7: Representations of Finite Groups, p. 102.

# Verification Notes

- Definition source: Direct from p. 102
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
