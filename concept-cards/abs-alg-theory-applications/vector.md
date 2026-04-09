---
# === CORE IDENTIFICATION ===
concept: Vector
slug: vector

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vector-space
extends: []
related:
  - scalar
  - linear-combination
contrasts_with:
  - scalar

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a vector in abstract algebra?"
---

# Quick Definition

In a vector space $V$ over a field $F$, the elements of $V$ are called vectors. Vectors can be added together and multiplied by scalars, but in general cannot be multiplied together.

# Core Definition

The elements of $V$ are called **vectors** (Judson, p. 266). It is important to notice that in most cases two vectors cannot be multiplied. In general, it is only possible to multiply a vector with a scalar.

# Prerequisites

- **Vector space** — Vectors are defined as elements of a vector space

# Key Properties

1. Vectors form an abelian group under addition
2. Vectors can be multiplied by scalars
3. In general, there is no product of two vectors
4. The vector zero $\mathbf{0}$ is distinct from the scalar zero $0$

# Context & Application

In abstract algebra, "vector" has a much broader meaning than in physics or basic linear algebra. Vectors can be polynomials, functions, field elements, or any objects in a vector space.

# Examples

**Example 1** (p. 266): In $\mathbb{R}^n$, vectors are $n$-tuples $(u_1, \ldots, u_n)$.

**Example 2** (p. 267): In $F[x]$ as a vector space, vectors are polynomials.

**Example 3** (p. 267): In $C[a,b]$, vectors are continuous functions.

# Relationships

## Related
- **Scalar** — Vectors are multiplied by scalars
- **Linear combination** — Vectors are combined via linear combinations

## Contrasts With
- **Scalar** — Vectors are elements of the space; scalars are elements of the field

# Source Reference

Chapter 20: Vector Spaces, Section 20.1, page 266.

# Verification Notes

- Definition source: Direct from p. 266
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
