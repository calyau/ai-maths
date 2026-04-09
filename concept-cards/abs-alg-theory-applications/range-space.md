---
# === CORE IDENTIFICATION ===
concept: Range Space
slug: range-space

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
  - "image"
  - "R(V)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-transformation
  - subspace
extends: []
related:
  - kernel
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the range space of a linear transformation?"
---

# Quick Definition

The range (or image) of a linear transformation $T: V \to W$ is the set $R(V) = \{w \in W : T(v) = w \text{ for some } v \in V\}$. It is a subspace of $W$.

# Core Definition

The **range** or **range space** of $T$ is $R(V) = \{w \in W : T(v) = w \text{ for some } v \in V\}$ (Judson, p. 272). It is a subspace of $W$.

# Prerequisites

- **Linear transformation** — The range is a property of linear transformations
- **Subspace** — The range is always a subspace

# Key Properties

1. $R(V)$ is a subspace of $W$
2. $\dim V = \dim \ker(T) + \dim R(V)$ (rank-nullity)
3. $T$ is surjective if and only if $R(V) = W$
4. If $\dim V = \dim W$, then $T$ is injective iff surjective

# Examples

**Example 1**: If $\{v_1, \ldots, v_n\}$ is a basis for $V$, then $R(V) = \text{span}\{T(v_1), \ldots, T(v_n)\}$.

# Relationships

## Builds Upon
- **Linear transformation** — The range is the image of $T$

## Related
- **Kernel** — Together with the range, determines $T$

# Source Reference

Chapter 20: Vector Spaces, Exercise 15, page 272.

# Verification Notes

- Definition source: From Exercise 15, p. 272
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
