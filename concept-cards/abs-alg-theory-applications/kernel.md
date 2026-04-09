---
# === CORE IDENTIFICATION ===
concept: Kernel of a Linear Transformation
slug: kernel

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
  - "null space"
  - "ker(T)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-transformation
  - subspace
extends: []
related:
  - range-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the kernel of a linear transformation?"
  - "How is the kernel related to injectivity?"
---

# Quick Definition

The kernel of a linear transformation $T: V \to W$ is the set of all vectors in $V$ that map to the zero vector: $\ker(T) = \{v \in V : T(v) = \mathbf{0}\}$. It is always a subspace of $V$.

# Core Definition

The **kernel** of a linear transformation $T: V \to W$ is $\ker(T) = \{v \in V : T(v) = \mathbf{0}\}$. The kernel is sometimes called the **null space** of $T$ (Judson, p. 272).

# Prerequisites

- **Linear transformation** — The kernel is defined for linear transformations
- **Subspace** — The kernel is a subspace

# Key Properties

1. $\ker(T)$ is a subspace of $V$
2. $T$ is injective if and only if $\ker(T) = \{\mathbf{0}\}$
3. $\dim V = \dim \ker(T) + \dim R(V)$ (rank-nullity theorem)

# Examples

**Example 1** (p. 272): For any linear transformation $T$, $T(\mathbf{0}) = \mathbf{0}$, so $\mathbf{0} \in \ker(T)$.

# Relationships

## Builds Upon
- **Linear transformation** — The kernel is a property of linear transformations
- **Subspace** — The kernel is a subspace

## Related
- **Range space** — Together with kernel, determines the structure of $T$

# Source Reference

Chapter 20: Vector Spaces, Exercise 15, page 272.

# Verification Notes

- Definition source: Direct from Exercise 15, p. 272
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
