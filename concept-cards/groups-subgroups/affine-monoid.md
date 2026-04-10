---
# === CORE IDENTIFICATION ===
concept: Affine Monoid
slug: affine-monoid

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 26
section: "Definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - algebraic monoid

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coordinate-ring
  - comultiplication
extends: []
related:
  - affine-group
  - bialgebra
  - monoid-object
contrasts_with:
  - affine-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An affine monoid is a k-algebra A with maps Delta: A -> A tensor A and epsilon: A -> k making h^A(R) a monoid (with identity epsilon) for each R. Equivalently, it corresponds to a commutative bialgebra. When A is finitely presented, it is an algebraic monoid.

# Core Definition

An **affine monoid** is a k-algebra A together with homomorphisms Delta: A -> A tensor A and epsilon: A -> k such that Delta makes h^A(R) into a monoid with identity element (A -> k -> R) for each k-algebra R (p. 26). When A is finitely presented, the affine monoid is said to be **algebraic**.

For any affine monoid M, the functor R -> M(R)^x (invertible elements) is an affine group M^x; when M is algebraic, so is M^x (Proposition 2.18, p. 26).

Commutative bialgebras correspond to affine monoids (Theorem 5.15a).

# Prerequisites

- **Coordinate ring** — A is the coordinate ring
- **Comultiplication** — Delta encodes the monoid operation

# Key Properties

1. A monoid is a "group without inverses"
2. M^x (invertible elements) is always an affine group
3. Corresponds to commutative bialgebras (without antipode)
4. End_V (endomorphism monoid) is a key example (Example 2.17)

# Examples

**Example 1** (p. 26): End_V: R -> (End_{R-lin}(R tensor V), composition). When V is free with basis e_1,...,e_n, this is R -> (M_n(R), multiplication), represented by k[X_11,...,X_nn].

**Example 2** (p. 26): GL_V = (End_V)^x is the group of invertible elements.

# Relationships

## Related
- **Affine group** — An affine group is an affine monoid with inversion
- **Bialgebra** — Commutative bialgebras correspond to affine monoids

## Contrasts With
- **Affine group** — Groups have inverses; monoids may not

# Source Reference

Chapter I, Section 2d (p. 26), Proposition 2.18, Theorem 5.15a.

# Verification Notes

- Definition source: Direct from p. 26
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
