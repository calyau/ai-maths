---
# === CORE IDENTIFICATION ===
concept: Dimension
slug: dimension

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
aliases:
  - "dim V"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - basis
extends: []
related:
  - degree-of-field-extension
  - linear-independence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dimension of a vector space?"
  - "Why is dimension well-defined?"
---

# Quick Definition

The dimension of a vector space $V$ is the number of elements in any basis for $V$, written $\dim V = n$. This number is well-defined because all bases of $V$ have the same size.

# Core Definition

If $\{e_1, e_2, \ldots, e_n\}$ is a basis for a vector space $V$, then we say that the **dimension** of $V$ is $n$ and we write $\dim V = n$ (Judson, p. 270).

The dimension is well-defined by Proposition 20.14: if $\{e_1, \ldots, e_m\}$ and $\{f_1, \ldots, f_n\}$ are two bases for $V$, then $m = n$.

# Prerequisites

- **Basis** — Dimension is defined as the cardinality of a basis

# Key Properties

1. All bases of a finite-dimensional vector space have the same number of elements (Proposition 20.14)
2. $\dim \mathbb{R}^n = n$
3. $\dim \mathbb{Q}(\sqrt{2}) = 2$ over $\mathbb{Q}$
4. $\dim \{\mathbf{0}\} = 0$
5. In a space of dimension $n$: any $n$ independent vectors form a basis; any $n$ spanning vectors form a basis (Theorem 20.15)

# Construction / Recognition

## To Determine:
1. Find a basis for the vector space
2. Count the number of basis elements
3. This count is the dimension

# Context & Application

Dimension is the fundamental invariant of a vector space. Two finite-dimensional vector spaces over the same field are isomorphic if and only if they have the same dimension. In field extension theory, the dimension of the extension $E$ viewed as a vector space over $F$ is the degree $[E:F]$, which controls the entire structure of the extension.

# Examples

**Example 1** (p. 269): $\dim \mathbb{R}^3 = 3$, since $\{(1,0,0), (0,1,0), (0,0,1)\}$ is a basis with three elements.

**Example 2** (p. 270): $\dim_{\mathbb{Q}} \mathbb{Q}(\sqrt{2}) = 2$, since $\{1, \sqrt{2}\}$ is a basis.

# Relationships

## Builds Upon
- **Basis** — Dimension counts basis elements

## Enables
- **Degree of field extension** — $[E:F] = \dim_F E$

## Related
- **Linear independence** — Independent sets have size at most $\dim V$
- **Spanning set** — Spanning sets have size at least $\dim V$

# Common Errors

- **Error**: Confusing the dimension with the number of elements in the vector space
  **Correction**: $\mathbb{R}^3$ has dimension 3 but uncountably many elements

# Common Confusions

- **Confusion**: Thinking dimension depends on the choice of basis
  **Clarification**: Dimension is an invariant; all bases have the same size

# Source Reference

Chapter 20: Vector Spaces, Section 20.3, page 270. See Proposition 20.14 and Theorem 20.15.

# Verification Notes

- Definition source: Direct from p. 270
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
