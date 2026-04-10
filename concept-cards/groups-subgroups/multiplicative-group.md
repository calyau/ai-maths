---
# === CORE IDENTIFICATION ===
concept: Multiplicative Group
slug: multiplicative-group

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
pdf_page: 29
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G_m"
  - "\\mathbb{G}_m"
  - GL_1

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - additive-group
  - general-linear-group
  - torus
  - group-of-nth-roots-of-unity
contrasts_with:
  - additive-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The multiplicative group G_m is the algebraic group defined by the functor R -> R^x (units of R). It is represented by k[X, X^{-1}] with comultiplication Delta(X) = X tensor X.

# Core Definition

The **multiplicative group** G_m is the functor R -> R^x (the group of units). It is an affine algebraic group with coordinate ring O(G_m) = k[X, X^{-1}] isomorphic to k[X, Y]/(XY - 1) (3.2, p. 29).

The Hopf algebra structure is (5.21, p. 48):
- Delta(X) = X tensor X
- epsilon sends f(X, X^{-1}) to f(1, 1)
- S(X) = X^{-1}

G_m = GL_1, and the embedding G_m -> GL_n sends a to the scalar matrix diag(a,...,a) (p. 16).

# Prerequisites

- **Affine algebraic group** — G_m is an example of an affine algebraic group

# Key Properties

1. O(G_m) = k[X, X^{-1}], the ring of Laurent polynomials
2. G_m(R) = R^x for all k-algebras R
3. G_m is commutative and connected
4. G_m is a one-dimensional torus
5. dim(G_m) = 1

# Examples

**Example 1** (p. 29): G_m(R) = {(a, b) in R^2 | ab = 1} isomorphic to Hom_{k-alg}(k[X,Y]/(XY-1), R).

**Example 2** (p. 16): The extension 1 -> G_m -> GL_n -> PGL_n -> 1 exhibits GL_n as a reductive group.

# Relationships

## Enables
- **Torus** — G_m is the simplest torus; a torus is a product of copies of G_m (over k^{al})
- **Group of nth roots of unity** — mu_n is the kernel of the nth power map G_m -> G_m

## Related
- **General linear group** — G_m = GL_1, and embeds as scalar matrices in GL_n

## Contrasts With
- **Additive group** — Different group operation (multiplication vs addition) and different coordinate ring structure

# Source Reference

Chapter I, 3.2 (p. 29) and 5.21 (p. 48).

# Verification Notes

- Definition source: Direct from 3.2
- Confidence rationale: Explicit definition with Hopf algebra structure
- Uncertainties: None
- Cross-reference status: Verified
