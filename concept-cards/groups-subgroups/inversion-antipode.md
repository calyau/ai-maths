---
# === CORE IDENTIFICATION ===
concept: Inversion (Antipode)
slug: inversion-antipode

# === CLASSIFICATION ===
category: hopf-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 44
section: "Affine groups and Hopf algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - antipode
  - antipodal map
  - coinverse

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bialgebra
extends: []
related:
  - hopf-algebra
  - comultiplication
  - counit
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Hopf algebra?"
  - "How do I construct the Hopf algebra of an affine algebraic group?"
---

# Quick Definition

An inversion (or antipode) for a bialgebra A is a k-linear map S: A -> A satisfying m(S tensor id)(Delta(a)) = e(epsilon(a)) = m(id tensor S)(Delta(a)) for all a in A. It encodes the group inversion g -> g^{-1}.

# Core Definition

An **inversion** (or **antipodal map**, usually shortened to **antipode**) for a bialgebra A is a k-linear map S: A -> A such that (Definition 5.9, p. 44):
- m composed with (S tensor id) composed with Delta = e composed with epsilon = m composed with (id tensor S) composed with Delta

Additionally, S satisfies S(ab) = S(ba) for all a, b in A and S(1) = 1. In fact, condition (a) alone implies condition (b) (Aside 5.10).

For commutative bialgebras, the inversion is unique if it exists (Corollary 5.17, p. 46) and is automatically a k-algebra homomorphism. Moreover, any homomorphism of commutative Hopf algebras preserves inversions (Proposition 5.16).

Explicitly, for an affine group G, (Sf)_R(a) = f_R(a^{-1}) for all R and a in G(R) (equation (40), p. 48).

# Prerequisites

- **Bialgebra** — The inversion is defined on a bialgebra

# Key Properties

1. S composed with S = id (for commutative Hopf algebras, Exercise 5-5a)
2. Delta composed with S = t composed with (S tensor S) composed with Delta (Exercise 5-5b)
3. epsilon composed with S = epsilon (Exercise 5-5c)
4. S is unique when it exists (for commutative bialgebras)
5. S is a k-algebra homomorphism (for commutative bialgebras)

# Examples

**Example 1** (p. 48): For G_a, S(f)(X) = f(-X). In particular, S(X) = -X.

**Example 2** (p. 48): For G_m, S(X) = X^{-1}.

**Example 3** (p. 49): For GL_n, S(x_{ij}) = y * a_{ji} (cofactor formula from Cramer's rule).

# Relationships

## Enables
- **Hopf algebra** — A bialgebra with an inversion is a Hopf algebra

## Related
- **Comultiplication** — S interacts with Delta via the Hopf algebra axiom
- **Counit** — S interacts with epsilon: epsilon composed with S = epsilon

# Source Reference

Chapter I, Section 5, Definition 5.9 (p. 44), equation (34), and explicit formulas (40) (p. 48).

# Verification Notes

- Definition source: Direct from Definition 5.9
- Confidence rationale: Explicit definition with axioms and examples
- Uncertainties: None
- Cross-reference status: Verified
