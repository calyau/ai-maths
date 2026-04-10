---
# === CORE IDENTIFICATION ===
concept: Comultiplication
slug: comultiplication

# === CLASSIFICATION ===
category: hopf-algebras
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
  - coproduct
  - Delta

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coordinate-ring
extends: []
related:
  - coalgebra
  - hopf-algebra
  - counit
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct the Hopf algebra of an affine algebraic group?"
  - "What is a coalgebra?"
---

# Quick Definition

The comultiplication Delta: A -> A tensor A is a k-algebra homomorphism on the coordinate ring of an affine group that encodes the group multiplication. For f in O(G), (Delta f)_R(a, b) = f_R(ab) for all a, b in G(R).

# Core Definition

For an affine group G = (A, Delta), the **comultiplication** (or coproduct) is the k-algebra homomorphism Delta: A -> A tensor A that induces the group multiplication. Specifically, for any k-algebra R, the map (f_1, f_2) -> (f_1, f_2) composed with Delta defines a binary operation on h^A(R) = Hom_{k-alg}(A, R) (Definition 2.9, p. 22).

Explicitly, if f is in O(G), then Delta(f) is the unique element of O(G) tensor O(G) such that (Delta f)_R(a, b) = f_R(ab) for all R and all a, b in G(R) (equation (38), p. 48).

# Prerequisites

- **Coordinate ring** — Delta is a map on the coordinate ring O(G)

# Key Properties

1. Delta is a k-algebra homomorphism (not just k-linear)
2. Delta is coassociative: (Delta tensor id) composed with Delta = (id tensor Delta) composed with Delta
3. Delta, together with the counit epsilon and antipode S, gives O(G) the structure of a Hopf algebra
4. Delta encodes the group law: Delta(f) tells you how f evaluates on products

# Examples

**Example 1** (p. 48): For G_a with O(G_a) = k[X], Delta(X) = X tensor 1 + 1 tensor X, corresponding to f(a+b) being expressed using f(a) and f(b).

**Example 2** (p. 48): For G_m with O(G_m) = k[X, X^{-1}], Delta(X) = X tensor X, corresponding to f(ab) = f(a)f(b).

**Example 3** (p. 49): For GL_n, Delta(x_{ik}) = sum_j x_{ij} tensor x_{jk}, reflecting matrix multiplication (c_{ik} = sum_j a_{ij}b_{jk}).

# Relationships

## Builds Upon
- **Coordinate ring** — Delta is defined on O(G)

## Enables
- **Coalgebra** — The pair (O(G), Delta) with counit forms a coalgebra
- **Hopf algebra** — Delta is the key structure map

## Related
- **Counit** — The identity element map epsilon: O(G) -> k

# Source Reference

Chapter I, Section 2c (Definition 2.9, p. 22) and Section 5g (explicit description, p. 48).

# Verification Notes

- Definition source: Direct from Definition 2.9 and equation (38)
- Confidence rationale: Explicit definition with worked examples
- Uncertainties: None
- Cross-reference status: Verified
