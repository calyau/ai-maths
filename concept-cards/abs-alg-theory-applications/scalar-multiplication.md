---
# === CORE IDENTIFICATION ===
concept: Scalar Multiplication
slug: scalar-multiplication

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
section: "20.1 Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "scalar product (in vector space sense)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vector-space
  - scalar
extends: []
related:
  - linear-combination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is scalar multiplication in a vector space?"
---

# Quick Definition

Scalar multiplication is the operation $\alpha \cdot v$ (or $\alpha v$) that multiplies a scalar $\alpha \in F$ by a vector $v \in V$, producing a vector in $V$. It is one of the two fundamental operations defining a vector space.

# Core Definition

A vector space $V$ over a field $F$ has a **scalar product** $\alpha \cdot v$ or $\alpha v$ defined for all $\alpha \in F$ and all $v \in V$ (Judson, p. 266). This operation must satisfy four axioms: associativity $\alpha(\beta v) = (\alpha\beta)v$, two distributive laws, and the identity $1v = v$.

# Prerequisites

- **Vector space** — Scalar multiplication is part of the vector space definition
- **Scalar** — Scalars come from the field $F$

# Key Properties

1. $0v = \mathbf{0}$ for all $v \in V$
2. $\alpha \mathbf{0} = \mathbf{0}$ for all $\alpha \in F$
3. $(-1)v = -v$
4. If $\alpha v = \mathbf{0}$, then $\alpha = 0$ or $v = \mathbf{0}$

# Examples

**Example 1** (p. 266): In $\mathbb{R}^n$: $\alpha(u_1, \ldots, u_n) = (\alpha u_1, \ldots, \alpha u_n)$.

**Example 2** (p. 267): In $F[x]$: $\alpha p(x)$ multiplies each coefficient by $\alpha$.

# Relationships

## Related
- **Linear combination** — Uses scalar multiplication

# Source Reference

Chapter 20: Vector Spaces, Section 20.1, page 266.

# Verification Notes

- Definition source: Direct from p. 266
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
