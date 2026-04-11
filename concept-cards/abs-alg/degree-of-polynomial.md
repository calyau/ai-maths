---
concept: Degree of a Polynomial
slug: degree-of-polynomial
category: ring-theory
subcategory: polynomial-rings
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 235
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases:
  - "polynomial degree"
prerequisites:
  - polynomial-ring
extends: []
related:
  - leading-coefficient
  - monic-polynomial
contrasts_with: []
answers_questions:
  - "What is the degree of a polynomial?"
  - "How does degree behave under multiplication?"
---

# Quick Definition
The degree of a nonzero polynomial $a_nx^n + \cdots + a_0$ with $a_n \neq 0$ is n. The leading coefficient is $a_n$, and the polynomial is monic if $a_n = 1$.

# Core Definition
If $a_n \neq 0$, the polynomial $a_nx^n + \cdots + a_0$ is of *degree* n, $a_nx^n$ is the *leading term*, and $a_n$ is the *leading coefficient*. The polynomial is *monic* if $a_n = 1$ (Dummit & Foote, p. 235).

# Prerequisites
- **Polynomial ring** — Degree is defined for elements of $R[x]$

# Key Properties
1. $\deg(p \cdot q) = \deg(p) + \deg(q)$ when R is an integral domain (Proposition 1/4)
2. The units of $R[x]$ are exactly the units of R (when R is an integral domain)
3. Degree serves as the Euclidean norm for $F[x]$ when F is a field

# Examples
**Example 1** (p. 235): $3x^4 - 2x + 5$ has degree 4, leading coefficient 3.

**Example 2** (p. 237): In $\mathbb{Z}/2\mathbb{Z}[x]$, $(x+1)^2 = x^2 + 1$ has degree 2 (the $2x$ term vanishes).

# Relationships

## Related
- **leading-coefficient** — The coefficient of the highest degree term
- **monic-polynomial** — Leading coefficient equals 1

# Source Reference
Chapter 7, Section 7.2, page 235; Chapter 9, Section 9.1, page 295.

# Verification Notes
- Definition: Direct from p. 235
- Confidence: HIGH — explicit definition
