---
concept: Companion Matrix
slug: companion-matrix
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 477
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix-of-linear-transformation
extends: []
related:
  - rational-canonical-form
  - characteristic-polynomial
  - minimal-polynomial
contrasts_with: []
answers_questions:
  - "What is a companion matrix?"
---

# Quick Definition
The companion matrix of a monic polynomial $a(x) = x^k + b_{k-1}x^{k-1} + \cdots + b_0$ is the $k \times k$ matrix with 1's on the first subdiagonal, $-b_0, -b_1, \ldots, -b_{k-1}$ in the last column, and zeros elsewhere.

# Core Definition
Let $a(x) = x^k + b_{k-1}x^{k-1} + \cdots + b_1 x + b_0$ be a monic polynomial in F[x]. The companion matrix $C_{a(x)}$ is the matrix representing multiplication by x on $F[x]/(a(x))$ with respect to the basis $\{1, \bar{x}, \ldots, \bar{x}^{k-1}\}$. Its characteristic polynomial and minimal polynomial are both equal to $a(x)$ (Dummit & Foote, p. 477).

# Prerequisites
- **matrix-of-linear-transformation** — Companion matrices represent linear maps

# Key Properties
1. The characteristic polynomial of $C_{a(x)}$ is $a(x)$
2. The minimal polynomial of $C_{a(x)}$ is $a(x)$
3. Companion matrices are the building blocks of the rational canonical form
4. $C_{a(x)}$ is the matrix of multiplication by x on $F[x]/(a(x))$

# Relationships
## Enables
- **rational-canonical-form** — Block diagonal of companion matrices

## Related
- **characteristic-polynomial**, **minimal-polynomial**

# Source Reference
Chapter 12, Section 12.2, p. 477.

# Verification Notes
- Confidence: HIGH — explicit definition and construction
