---
concept: Matrix Ring
slug: matrix-ring
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 238
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases:
  - "ring of matrices"
prerequisites:
  - ring
extends:
  - ring
related:
  - polynomial-ring
  - group-ring
contrasts_with:
  - commutative-ring
answers_questions:
  - "What is a matrix ring?"
  - "Why are matrix rings noncommutative?"
---

# Quick Definition
The matrix ring $M_n(R)$ is the set of all $n \times n$ matrices with entries from a ring R, under componentwise addition and the standard matrix multiplication.

# Core Definition
Fix an arbitrary ring R and a positive integer n. The set $M_n(R)$ of all $n \times n$ matrices with entries from R becomes a ring under componentwise addition and matrix multiplication, where the $(i,j)$ entry of the product $(a_{ij}) \times (b_{ij})$ is $\sum_{k=1}^{n} a_{ik}b_{kj}$ (Dummit & Foote, p. 238).

# Prerequisites
- **Ring** — Entries come from a ring R

# Key Properties
1. $M_n(R)$ is noncommutative for $n \geq 2$ and nontrivial R (p. 238)
2. $M_n(R)$ has zero divisors for $n \geq 2$ (p. 239)
3. The scalar matrices form a subring isomorphic to R (p. 239)
4. If R has identity, $M_n(R)$ has identity (the identity matrix) (p. 239)
5. The center of $M_n(R)$ is the set of scalar matrices (Exercise 7, p. 240)
6. Every two-sided ideal of $M_n(R)$ has the form $M_n(J)$ for an ideal J of R (Exercise 21, p. 250)

# Construction / Recognition
## To Construct:
1. Choose a ring R and positive integer n
2. Form all $n \times n$ arrays with entries in R
3. Add componentwise, multiply by matrix multiplication

# Context & Application
Matrix rings are a primary source of noncommutative rings. They connect ring theory with linear algebra and are central to the study of modules and representations.

# Examples
**Example 1** (p. 238): $M_2(\mathbb{Z})$ is a noncommutative ring with zero divisors.

**Example 2** (p. 239): Upper triangular matrices form a subring of $M_n(R)$.

# Relationships

## Related
- **polynomial-ring** — Another fundamental ring construction
- **group-ring** — Related via representation theory (Part VI)

## Contrasts With
- **commutative-ring** — Matrix rings ($n \geq 2$) are never commutative

# Common Errors
- **Error**: Assuming matrix multiplication is commutative
  **Correction**: $AB \neq BA$ in general for $n \geq 2$

# Common Confusions
- **Confusion**: Thinking the determinant is a ring homomorphism
  **Clarification**: The determinant preserves multiplication but not addition; it is not a ring homomorphism (Exercise 6, p. 249)

# Source Reference
Chapter 7, Section 7.2, pages 238-239.

# Verification Notes
- Definition: Direct from p. 238
- Confidence: HIGH — standard construction
