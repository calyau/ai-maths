---
# === CORE IDENTIFICATION ===
concept: Linear Combination
slug: linear-combination

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vector-space
extends: []
related:
  - spanning-set
  - linear-independence
  - linear-dependence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linear combination of vectors?"
---

# Quick Definition

A linear combination of vectors $v_1, v_2, \ldots, v_n$ in a vector space $V$ over a field $F$ is any vector of the form $\alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n$ where $\alpha_i \in F$.

# Core Definition

Let $V$ be any vector space over a field $F$ and suppose that $v_1, v_2, \ldots, v_n$ are vectors in $V$ and $\alpha_1, \alpha_2, \ldots, \alpha_n$ are scalars in $F$. Any vector $w$ in $V$ of the form

$$w = \sum_{i=1}^{n} \alpha_i v_i = \alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n$$

is called a **linear combination** of the vectors $v_1, v_2, \ldots, v_n$ (Judson, p. 268).

# Prerequisites

- **Vector space** — Linear combinations are defined within a vector space using its addition and scalar multiplication

# Key Properties

1. The zero vector is always a linear combination of any set of vectors (set all scalars to zero)
2. Each $v_i$ is a linear combination of $\{v_1, \ldots, v_n\}$ (set $\alpha_i = 1$ and all others to zero)
3. The set of all linear combinations of a set of vectors forms a subspace (Proposition 20.8)

# Construction / Recognition

## To Construct:
1. Choose vectors $v_1, \ldots, v_n$ from the vector space
2. Choose scalars $\alpha_1, \ldots, \alpha_n$ from the field
3. Compute $\alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n$

# Context & Application

Linear combinations are the most fundamental operation in linear algebra. Every concept — spanning, independence, basis, dimension — is defined in terms of linear combinations. As noted in the reading questions (p. 270): "Linear algebra is all about linear combinations."

# Examples

**Example 1** (p. 268): In $\mathbb{R}^3$, the vector $(5, 7, 9)$ is a linear combination of $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$ via $5e_1 + 7e_2 + 9e_3$.

# Relationships

## Builds Upon
- **Vector space** — Linear combinations use the vector space operations

## Enables
- **Spanning set** — Defined as the set of all linear combinations
- **Linear independence** — Defined in terms of when a linear combination equals zero
- **Basis** — A basis allows unique representation of every vector as a linear combination

# Common Errors

- **Error**: Including products of vectors in a "linear" combination
  **Correction**: Only scalar multiples of vectors added together constitute a linear combination

# Common Confusions

- **Confusion**: Thinking a linear combination must use all nonzero coefficients
  **Clarification**: Coefficients may be zero; the zero vector is a trivial linear combination of any set

# Source Reference

Chapter 20: Vector Spaces, Section 20.2 "Subspaces," page 268.

# Verification Notes

- Definition source: Direct from p. 268
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
