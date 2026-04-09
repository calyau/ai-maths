---
# === CORE IDENTIFICATION ===
concept: Direct Sum of Vector Spaces
slug: direct-sum-vector-space

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
section: "20.5 Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "internal direct sum"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subspace
  - dimension
extends: []
related:
  - vector-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a direct sum of vector spaces?"
---

# Quick Definition

A vector space $W$ is the direct sum of subspaces $U$ and $V$, written $W = U \oplus V$, if $U + V = W$ and $U \cap V = \{\mathbf{0}\}$. Every element of $W$ can then be written uniquely as $w = u + v$.

# Core Definition

If $U + V = W$ and $U \cap V = \{\mathbf{0}\}$, then $W$ is said to be the **direct sum** and we write $W = U \oplus V$ (Judson, Exercise 17, p. 272). Every element $w \in W$ can be written uniquely as $w = u + v$ where $u \in U$ and $v \in V$.

# Prerequisites

- **Subspace** — Direct sums decompose a space into subspaces
- **Dimension** — $\dim(U \oplus V) = \dim U + \dim V$

# Key Properties

1. Every element has a unique decomposition $w = u + v$
2. $\dim W = \dim U + \dim V$
3. Every subspace $U$ of a finite-dimensional $W$ has a complement $V$ with $W = U \oplus V$
4. The dimension formula: $\dim(U + V) = \dim U + \dim V - \dim(U \cap V)$

# Examples

**Example 1**: $\mathbb{R}^3 = \text{span}\{e_1, e_2\} \oplus \text{span}\{e_3\}$ where $e_i$ are standard basis vectors.

# Relationships

## Builds Upon
- **Subspace** — Direct sums decompose into subspaces

# Source Reference

Chapter 20: Vector Spaces, Exercise 17, page 272.

# Verification Notes

- Definition source: From Exercise 17, p. 272
- Confidence: HIGH — explicit definition in exercise
- Cross-reference status: Verified
- Uncertainties: None
