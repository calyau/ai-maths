---
# === CORE IDENTIFICATION ===
concept: Basis
slug: basis

# === CLASSIFICATION ===
category: linear-algebra
subcategory: vector-spaces
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Vector Spaces"
chapter_number: 20
pdf_page: 266
section: "20.3 Linear Independence"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-independence
  - spanning-set
extends: []
related:
  - dimension
  - linear-combination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a basis for a vector space?"
  - "Is a basis unique?"
  - "How are bases related to dimension?"
---

# Quick Definition

A basis for a vector space $V$ is a set of vectors that is both linearly independent and spans $V$. Every vector in $V$ can be written uniquely as a linear combination of basis vectors.

# Core Definition

A set $\{e_1, e_2, \ldots, e_n\}$ of vectors in a vector space $V$ is called a **basis** for $V$ if $\{e_1, e_2, \ldots, e_n\}$ is a linearly independent set that spans $V$ (Judson, p. 269).

# Prerequisites

- **Linear independence** — Basis vectors must be linearly independent
- **Spanning set** — Basis vectors must span the entire space

# Key Properties

1. Any two bases of a finite-dimensional vector space have the same number of elements (Proposition 20.14)
2. In a vector space of dimension $n$, any $n$ linearly independent vectors form a basis (Theorem 20.15)
3. In a vector space of dimension $n$, any $n$ vectors that span $V$ form a basis (Theorem 20.15)
4. A linearly independent set of $k < n$ vectors can always be extended to a basis (Theorem 20.15)
5. Every vector in $V$ has a unique representation as a linear combination of basis vectors (Proposition 20.9)

# Construction / Recognition

## To Construct:
1. Find a set of vectors that spans $V$
2. Remove any vector that is a linear combination of the others
3. The resulting linearly independent spanning set is a basis

## To Recognize:
1. Verify the set spans $V$ (every vector is a linear combination)
2. Verify the set is linearly independent (the only trivial combination yielding $\mathbf{0}$ uses all zero scalars)

# Context & Application

Bases provide coordinate systems for vector spaces. They are essential for computation and for defining the dimension of a space. In the context of field extensions, a basis for $E$ over $F$ determines the degree $[E:F]$.

# Examples

**Example 1** (p. 269): $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$ form a basis for $\mathbb{R}^3$. So does $\{(3,2,1), (3,2,0), (1,1,1)\}$.

**Example 2** (p. 270): Both $\{1, \sqrt{2}\}$ and $\{1 + \sqrt{2}, 1 - \sqrt{2}\}$ are bases for $\mathbb{Q}(\sqrt{2})$ over $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Linear independence** — A necessary condition for a basis
- **Spanning set** — A necessary condition for a basis

## Enables
- **Dimension** — Defined as the number of elements in any basis
- **Degree of field extension** — The dimension of $E$ over $F$ viewed as a vector space

## Related
- **Linear combination** — Every vector has a unique linear combination representation in terms of a basis

# Common Errors

- **Error**: Assuming there is only one basis for a given vector space
  **Correction**: A vector space has infinitely many bases (in general), but all have the same size

# Common Confusions

- **Confusion**: Believing that one basis is "the" correct one
  **Clarification**: All bases are equally valid; the standard basis is merely conventional. The choice of basis is a matter of convenience.

# Source Reference

Chapter 20: Vector Spaces, Section 20.3, pages 269–270. See Proposition 20.14 and Theorem 20.15.

# Verification Notes

- Definition source: Direct from p. 269
- Confidence: HIGH — explicit definition with multiple examples
- Cross-reference status: Verified
- Uncertainties: None
