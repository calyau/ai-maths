---
concept: Dimension
slug: dimension
category: linear-algebra
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 412
section: "11.1 Definitions and Basic Theory"
extraction_confidence: high
aliases:
  - "dim"
prerequisites:
  - basis
extends: []
related:
  - rank-of-free-module
  - degree-of-extension
contrasts_with: []
answers_questions:
  - "What is the dimension of a vector space?"
---

# Quick Definition
The dimension of a vector space V over F, denoted $\dim_F V$, is the cardinality of any basis. This is well-defined since all bases have the same cardinality.

# Core Definition
If V is a finitely generated F-module (has a finite basis), the cardinality of any basis is called the dimension of V, denoted $\dim_F V$ or just $\dim V$. If V is not finitely generated, V is infinite dimensional (Dummit & Foote, p. 412).

# Prerequisites
- **basis** — Dimension is the size of a basis

# Key Properties
1. $\dim V = \dim W + \dim V/W$ for any subspace W (Theorem 7)
2. $\dim V = \dim \ker\varphi + \dim \text{image}(\varphi)$ for any linear map $\varphi$ (Corollary 8)
3. $V \cong F^n$ iff $\dim V = n$ (Theorem 6)
4. Two finite dimensional spaces are isomorphic iff they have the same dimension

# Examples
**Example** (p. 412): $\dim_F F[x]/(f(x)) = \deg f(x)$ for nonzero $f(x)$.

# Relationships
## Builds Upon
- **basis**

## Enables
- **degree-of-extension** — The degree $[K:F]$ is $\dim_F K$

## Related
- **rank-of-free-module** — Dimension for modules over a field

# Source Reference
Chapter 11, Section 11.1, pp. 412-414.

# Verification Notes
- Confidence: HIGH — explicit definition
