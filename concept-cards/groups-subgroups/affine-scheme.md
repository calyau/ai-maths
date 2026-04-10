---
# === CORE IDENTIFICATION ===
concept: Affine Scheme
slug: affine-scheme

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
pdf_page: 53
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - affine k-scheme

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - coordinate-ring
  - affine-group-scheme
  - zariski-topology
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine group scheme?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

An affine scheme is a locally ringed space isomorphic to Spec(A) = (spec A, O_A) for some commutative ring A. The functor Spec is a contravariant equivalence from commutative rings to affine schemes.

# Core Definition

For a commutative ring A, the **prime spectrum** spec(A) is the set of prime ideals in A, equipped with the **Zariski topology** whose closed sets are V(a) = {p | p contains a} for ideals a in A. The **structure sheaf** O_A is defined by O_A(D(f)) = A_f for principal open sets D(f) = {p | f not in p} (Section 6a, p. 53-54).

An **affine scheme** (V, O_V) is a ringed space isomorphic to Spec(A) for some commutative ring A. A morphism of affine schemes is a morphism of locally ringed spaces (p. 54).

**Proposition 6.1** (p. 54): The functor Spec is a contravariant equivalence from commutative rings to affine schemes, with quasi-inverse (V, O) -> O(V).

An **affine k-scheme** is an affine scheme V with a morphism V -> Spec(k), equivalently a pair (V, O_V) where O(V) is a k-algebra.

# Prerequisites

This is a foundational concept from algebraic geometry. It requires familiarity with commutative algebra (prime ideals, localization).

# Key Properties

1. Spec is a contravariant equivalence: commutative rings <-> affine schemes
2. Principal open sets D(f) form a base for the topology
3. The stalk at p is the local ring A_p
4. For a field k, an affine algebraic scheme is Spm(A) for a finitely generated k-algebra A

# Examples

**Example 1** (p. 57): For an algebraically closed field k, the closed subsets of k^n correspond to ideals in k[X_1,...,X_n], and the affine scheme structure on V(a) has coordinate ring k[V] = k[X_1,...,X_n]/a.

**Example 2** (p. 57): Spm(k[X,Y]/(Y^2)) is the x-axis "with multiplicity 2" -- same topological space as Spm(k[X,Y]/(Y)) but a thickened structure.

# Relationships

## Enables
- **Affine group scheme** — Group objects in the category of affine schemes
- **Coordinate ring** — O(V) is the coordinate ring of the affine scheme V

# Source Reference

Chapter I, Section 6a "Affine schemes", p. 53-54, Proposition 6.1.

# Verification Notes

- Definition source: Direct from Section 6a
- Confidence rationale: Standard algebraic geometry, explicitly presented
- Uncertainties: None
- Cross-reference status: Verified
