---
# === CORE IDENTIFICATION ===
concept: Dual Space
slug: dual-space

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "V*"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vector-space
  - linear-transformation
extends: []
related:
  - basis
  - dimension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dual space of a vector space?"
---

# Quick Definition

The dual space $V^*$ of a vector space $V$ over $F$ is the vector space of all linear functionals from $V$ to $F$: $V^* = \text{Hom}(V, F)$.

# Core Definition

Let $V$ be an $F$-vector space. The **dual space** of $V$ is $V^* = \text{Hom}(V, F)$. Elements in the dual space of $V$ are called **linear functionals** (Judson, Exercise 18, p. 273).

Given an ordered basis $v_1, \ldots, v_n$ for $V$, the **dual basis** $\phi_1, \ldots, \phi_n$ for $V^*$ is defined by $\phi_i(v) = \alpha_i$ where $v = \alpha_1 v_1 + \cdots + \alpha_n v_n$.

# Prerequisites

- **Vector space** — The dual space is a vector space itself
- **Linear transformation** — Dual space elements are linear maps

# Key Properties

1. $V^*$ is a vector space over $F$ (Exercise 18a)
2. $\dim V^* = \dim V$ for finite-dimensional $V$
3. Every basis of $V$ gives rise to a dual basis of $V^*$ (Exercise 18b)
4. $V \cong V^{**}$ canonically for finite-dimensional $V$ (Exercise 18d)

# Examples

**Example 1** (p. 273): For $\mathbb{R}^2$ with basis $\{(3,1), (2,-2)\}$, the dual basis consists of the linear functionals extracting the coordinates in this basis.

# Relationships

## Builds Upon
- **Vector space** — The dual is itself a vector space
- **Linear transformation** — Elements are linear functionals

## Related
- **Basis** — Every basis gives a dual basis
- **Dimension** — $\dim V^* = \dim V$

# Source Reference

Chapter 20: Vector Spaces, Exercise 18, pages 272–273.

# Verification Notes

- Definition source: From Exercise 18, p. 273
- Confidence: MEDIUM — defined in exercises rather than main text
- Cross-reference status: Verified
- Uncertainties: None
