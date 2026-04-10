---
# === CORE IDENTIFICATION ===
concept: Coalgebra
slug: coalgebra

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
pdf_page: 41
section: "Affine groups and Hopf algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - co-associative coalgebra
  - coassociative coalgebra with coidentity

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - comultiplication
  - counit
  - bialgebra
  - hopf-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coalgebra?"
  - "What must I know before understanding Hopf algebras?"
---

# Quick Definition

A coalgebra over k is a k-module C together with k-linear maps Delta: C -> C tensor C (comultiplication) and epsilon: C -> k (counit) satisfying coassociativity and the counit axiom. It is the dual notion to an associative algebra with identity.

# Core Definition

A **co-associative coalgebra** over k **with co-identity** (henceforth, a **coalgebra** over k) is a module C over k together with a pair of k-linear maps Delta: C -> C tensor C and epsilon: C -> k such that the following hold (Definition 5.1, p. 41):
- Coassociativity: (C tensor Delta) composed with Delta = (Delta tensor C) composed with Delta
- Counit axiom: (C tensor epsilon) composed with Delta = id_C = (epsilon tensor C) composed with Delta

These diagrams are obtained by reversing the arrows in the diagrams defining an associative algebra with identity (p. 41).

A **homomorphism** of coalgebras is a k-linear map f: C -> D such that (f tensor f) composed with Delta_C = Delta_D composed with f and epsilon_D composed with f = epsilon_C.

# Prerequisites

This is a foundational concept for the Hopf algebra theory. It requires familiarity with k-modules and tensor products.

# Key Properties

1. Every vector space admits the structure of a coalgebra: for a set S with basis C, define Delta(s) = s tensor s and epsilon(s) = 1 (5.2, p. 42)
2. A k-subspace D of C is a sub-coalgebra if Delta(D) is a subset of D tensor D (5.3, p. 42)
3. The tensor product of two coalgebras is again a coalgebra (5.4, p. 42)
4. The dual C^{vee} of a coalgebra is an associative algebra (Section 5c, p. 43)
5. Conversely, the dual of a finitely generated projective algebra is a coalgebra

# Construction / Recognition

## To Construct:
1. Start with a k-module C
2. Define Delta: C -> C tensor C (k-linear)
3. Define epsilon: C -> k (k-linear)
4. Verify coassociativity and the counit axiom

## To Recognize:
1. Check that Delta and epsilon satisfy the dual axioms to multiplication and unit
2. Verify the commutative diagrams (30), p. 42

# Context & Application

Coalgebras arise naturally as the dual of algebras. In the theory of algebraic groups, the coordinate ring O(G) is simultaneously an algebra (under pointwise multiplication) and a coalgebra (under the comultiplication Delta encoding the group law). The compatibility of these two structures gives a bialgebra, and with the antipode, a Hopf algebra.

# Examples

**Example 1** (5.2, p. 42): For a set S, the free k-module with basis S becomes a coalgebra with Delta(s) = s tensor s and epsilon(s) = 1.

**Example 2** (5.5, p. 43): For a set X, the free k-module C with basis X has coalgebra structure Delta(x) = x tensor x, epsilon(x) = 1. The dual algebra C^{vee} is the algebra of maps X -> k with pointwise multiplication.

# Relationships

## Enables
- **Bialgebra** — A bialgebra is simultaneously an algebra and a coalgebra
- **Hopf algebra** — A Hopf algebra is a bialgebra with inversion

## Related
- **Comultiplication** — The structure map Delta of a coalgebra
- **Counit** — The structure map epsilon of a coalgebra

# Common Confusions

- **Confusion**: Thinking that the dual of every algebra is a coalgebra
  **Clarification**: This requires the algebra to be finitely generated and projective as a k-module; the natural map V^{vee} tensor W^{vee} -> (V tensor W)^{vee} must be an isomorphism (5c, p. 43)

# Source Reference

Chapter I, Section 5b "Coalgebras", Definition 5.1, p. 41-42.

# Verification Notes

- Definition source: Direct from Definition 5.1, p. 41
- Confidence rationale: Explicit definition with axioms
- Uncertainties: None
- Cross-reference status: Verified
