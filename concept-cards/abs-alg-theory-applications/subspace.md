---
# === CORE IDENTIFICATION ===
concept: Subspace
slug: subspace

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
section: "20.2 Subspaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "vector subspace"
  - "linear subspace"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vector-space
extends:
  - vector-space
related:
  - spanning-set
  - linear-combination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subspace of a vector space?"
  - "How do I verify that a subset is a subspace?"
---

# Quick Definition

A subspace $W$ of a vector space $V$ over a field $F$ is a subset of $V$ that is itself a vector space under the same operations — equivalently, a subset closed under vector addition and scalar multiplication.

# Core Definition

Let $V$ be a vector space over a field $F$, and $W$ a subset of $V$. Then $W$ is a **subspace** of $V$ if it is closed under vector addition and scalar multiplication; that is, if $u, v \in W$ and $\alpha \in F$, then $u + v$ and $\alpha v$ are also in $W$ (Judson, p. 267).

# Prerequisites

- **Vector space** — Subspaces are substructures of vector spaces; one must understand the parent structure first

# Key Properties

1. Every subspace contains the zero vector $\mathbf{0}$
2. A subspace is itself a vector space under the inherited operations
3. The intersection of subspaces is a subspace
4. $\{\mathbf{0}\}$ is a subspace of every vector space (dimension zero)
5. $V$ itself is always a subspace of $V$
6. The span of any set of vectors is a subspace (Proposition 20.8)

# Construction / Recognition

## To Construct:
1. Start with a vector space $V$ over $F$
2. Select a subset $W \subseteq V$
3. Verify closure under addition and scalar multiplication

## To Recognize:
1. Check that $W$ is nonempty (or equivalently, $\mathbf{0} \in W$)
2. For any $u, v \in W$, verify $u + v \in W$
3. For any $\alpha \in F$ and $v \in W$, verify $\alpha v \in W$

# Context & Application

Subspaces provide a way to decompose vector spaces into simpler components. They arise naturally as solution sets of homogeneous linear equations, as kernels and images of linear transformations, and as spans of sets of vectors.

# Examples

**Example 1** (p. 267): $W = \{(x_1, 2x_1 + x_2, x_1 - x_2) : x_1, x_2 \in \mathbb{R}\}$ is a subspace of $\mathbb{R}^3$.

**Example 2** (p. 268): The set of polynomials in $F[x]$ with no odd-power terms is a subspace of $F[x]$.

**Example 3** (p. 271): The set $\{\mathbf{0}\}$ is a subspace of any vector space $V$, with dimension zero.

# Relationships

## Builds Upon
- **Vector space** — A subspace is a vector space within a vector space

## Enables
- **Basis** — A basis is found within and for a subspace
- **Direct sum** — Vector spaces can be decomposed into direct sums of subspaces
- **Kernel** — The kernel of a linear transformation is a subspace

## Related
- **Spanning set** — The span of a set of vectors forms a subspace
- **Linear combination** — Subspaces are closed under linear combinations

# Common Errors

- **Error**: Checking only closure under addition but not scalar multiplication
  **Correction**: Both closure conditions must hold; a subset closed under addition but not scalar multiplication is not a subspace

- **Error**: Forgetting to verify the zero vector is in the subset
  **Correction**: The zero vector must be in every subspace; if $\mathbf{0} \notin W$, then $W$ is not a subspace

# Common Confusions

- **Confusion**: Believing any subset of a vector space is a subspace
  **Clarification**: Only subsets that are closed under both operations qualify. For instance, $\{(x_1, x_2, x_3) : x_1 - 2x_2 + 2x_3 = 2\}$ is not a subspace because it does not contain $\mathbf{0}$.

# Source Reference

Chapter 20: Vector Spaces, Section 20.2 "Subspaces," pages 267–268. See Proposition 20.8 for span as subspace.

# Verification Notes

- Definition source: Direct from p. 267
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
