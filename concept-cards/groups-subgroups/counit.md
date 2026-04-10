---
# === CORE IDENTIFICATION ===
concept: Counit
slug: counit

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
  - co-identity
  - coidentity
  - augmentation map
  - epsilon

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coalgebra
extends: []
related:
  - comultiplication
  - augmentation-ideal
  - hopf-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coalgebra?"
  - "How do I construct the Hopf algebra of an affine algebraic group?"
---

# Quick Definition

The counit epsilon: A -> k of a coalgebra (or Hopf algebra) encodes the identity element of the group. For an affine group G, epsilon(f) = f(1) (evaluation at the identity element).

# Core Definition

The **counit** (or **co-identity**) is the k-linear map epsilon: C -> k that, together with the comultiplication Delta, defines a coalgebra structure. It satisfies (C tensor epsilon) composed with Delta = id_C = (epsilon tensor C) composed with Delta (Definition 5.1, equation (30), p. 42).

For an affine group G, epsilon: O(G) -> k is the algebra homomorphism defined by epsilon(f) = f(1) (the constant function at the identity), equation (39), p. 48. In the functor-of-points language, epsilon corresponds to the identity element e in G(k).

# Prerequisites

- **Coalgebra** — epsilon is one of the two structure maps of a coalgebra

# Key Properties

1. epsilon is a k-algebra homomorphism (for bialgebras/Hopf algebras)
2. epsilon encodes the identity element of the group
3. Ker(epsilon) is the augmentation ideal
4. epsilon composed with S = epsilon (the antipode preserves the counit)

# Examples

**Example 1** (p. 48): For G_a, epsilon(f) = f(0) (constant term of the polynomial f).

**Example 2** (p. 48): For G_m, epsilon sends f(X, X^{-1}) to f(1, 1).

**Example 3** (p. 49): For GL_n, epsilon(x_{ii}) = 1, epsilon(x_{ij}) = 0 for i != j, epsilon(y) = 1 (evaluation at the identity matrix).

# Relationships

## Related
- **Comultiplication** — Together with epsilon, defines the coalgebra structure
- **Augmentation ideal** — Ker(epsilon) is the augmentation ideal
- **Hopf algebra** — epsilon is one of the three structure maps (Delta, epsilon, S)

# Source Reference

Chapter I, Definition 5.1 (p. 41), equation (39) (p. 48).

# Verification Notes

- Definition source: Direct from Definition 5.1 and equation (39)
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
