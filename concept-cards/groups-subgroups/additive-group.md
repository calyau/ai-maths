---
# === CORE IDENTIFICATION ===
concept: Additive Group
slug: additive-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 22
section: "Definition of an affine (algebraic) group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G_a"
  - "\\mathbb{G}_a"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - multiplicative-group
  - coordinate-ring
contrasts_with:
  - multiplicative-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The additive group G_a is the algebraic group defined by the functor R -> (R, +). It is represented by the polynomial ring k[X] with comultiplication Delta(X) = X tensor 1 + 1 tensor X.

# Core Definition

The **additive group** G_a is the affine algebraic group (k[X], Delta) where Delta is the k-algebra homomorphism k[X] -> k[X] tensor k[X] sending X to X tensor 1 + 1 tensor X (Example 2.10, p. 22). For f_1, f_2 in h^A(R), (f_1 * f_2)(X) = f_1(X) + f_2(X), so the group operation on h^A(R) is isomorphic to R is addition.

The Hopf algebra structure is (5.20, p. 48):
- Delta(f)(X_1, X_2) = f(X_1 + X_2)
- epsilon(f) = f(0) (constant term)
- (Sf)(X) = f(-X)

# Prerequisites

- **Affine algebraic group** — G_a is an example of an affine algebraic group

# Key Properties

1. O(G_a) = k[X], a polynomial ring in one variable
2. G_a(R) = (R, +) for all k-algebras R
3. G_a is commutative and connected
4. G_a is unipotent (embeds in the upper triangular matrices via a -> (1, a; 0, 1))
5. dim(G_a) = 1

# Examples

**Example 1** (p. 29): G_a(R) = R as an additive group. The embedding G_a -> SL_2 sends a to the matrix (1 a; 0 1) (3.15, p. 34).

# Relationships

## Enables
- **Unipotent group** — G_a is the simplest unipotent group

## Contrasts With
- **Multiplicative group** — G_m uses multiplication instead of addition; O(G_m) = k[X, X^{-1}] vs O(G_a) = k[X]

# Source Reference

Chapter I, Example 2.10 (p. 22), 3.1 (p. 29), and 5.20 (p. 48).

# Verification Notes

- Definition source: Direct from Example 2.10
- Confidence rationale: Explicit, worked example
- Uncertainties: None
- Cross-reference status: Verified
