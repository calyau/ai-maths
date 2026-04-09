---
# === CORE IDENTIFICATION ===
concept: Spanning Set
slug: spanning-set

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
  - "span"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-combination
  - vector-space
extends: []
related:
  - subspace
  - basis
  - linear-independence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for vectors to span a vector space?"
  - "What is the span of a set of vectors?"
---

# Quick Definition

The spanning set (or span) of vectors $v_1, v_2, \ldots, v_n$ is the set of all possible linear combinations of those vectors. If this set equals $W$, we say $W$ is spanned by $v_1, \ldots, v_n$.

# Core Definition

The **spanning set** of vectors $v_1, v_2, \ldots, v_n$ is the set of vectors obtained from all possible linear combinations of $v_1, v_2, \ldots, v_n$. If $W$ is the spanning set of $v_1, v_2, \ldots, v_n$, then we say that $W$ is **spanned** by $v_1, v_2, \ldots, v_n$ (Judson, p. 268).

# Prerequisites

- **Linear combination** — The span is defined as the set of all linear combinations
- **Vector space** — Spanning is defined within a vector space

# Key Properties

1. The span of any set of vectors is a subspace (Proposition 20.8)
2. The span of the empty set is $\{\mathbf{0}\}$
3. A vector space is spanned by $n$ vectors implies any set of more than $n$ vectors is linearly dependent (Proposition 20.11)
4. Adding a vector to a spanning set does not change the span if the vector is already in it

# Construction / Recognition

## To Construct:
1. Choose vectors $v_1, \ldots, v_n$ from a vector space $V$
2. Form all linear combinations $\alpha_1 v_1 + \cdots + \alpha_n v_n$ for $\alpha_i \in F$
3. The resulting set is the span

## To Recognize:
1. Verify every vector in $W$ can be written as $\alpha_1 v_1 + \cdots + \alpha_n v_n$ for some scalars

# Context & Application

Spanning sets describe the "reach" of a collection of vectors. Finding a minimal spanning set (a basis) is a central problem in linear algebra.

# Examples

**Example 1** (p. 269): The vectors $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$ span $\mathbb{R}^3$, since any $(x_1, x_2, x_3) = x_1 e_1 + x_2 e_2 + x_3 e_3$.

**Example 2** (p. 270): The sets $\{1, \sqrt{2}\}$ and $\{1 + \sqrt{2}, 1 - \sqrt{2}\}$ both span $\mathbb{Q}(\sqrt{2})$ over $\mathbb{Q}$.

# Relationships

## Builds Upon
- **Linear combination** — Span is the set of all linear combinations

## Enables
- **Basis** — A basis is a linearly independent spanning set
- **Dimension** — The minimum size of a spanning set

## Related
- **Subspace** — The span of any set is a subspace

# Common Errors

- **Error**: Assuming that a spanning set is unique
  **Correction**: Many different sets of vectors can span the same subspace

# Common Confusions

- **Confusion**: Conflating "spanning set" with "basis"
  **Clarification**: A spanning set may contain redundant vectors; a basis is a minimal spanning set that is also linearly independent

# Source Reference

Chapter 20: Vector Spaces, Section 20.2 "Subspaces," page 268. See Proposition 20.8 and 20.11.

# Verification Notes

- Definition source: Direct from p. 268
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
