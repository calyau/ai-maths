---
concept: Leading Coefficient
slug: leading-coefficient
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
  - "leading term"
prerequisites:
  - polynomial-ring
extends: []
related:
  - degree-of-polynomial
  - monic-polynomial
contrasts_with: []
answers_questions:
  - "What is the leading coefficient of a polynomial?"
  - "What is the leading term?"
---

# Quick Definition
The leading coefficient of a nonzero polynomial $a_nx^n + \cdots + a_0$ (with $a_n \neq 0$) is $a_n$. The leading term is $a_nx^n$.

# Core Definition
If $a_n \neq 0$, the leading coefficient of $a_nx^n + \cdots + a_0$ is $a_n$ and the leading term is $a_nx^n$ (Dummit & Foote, p. 235). The leading coefficient of the zero polynomial is defined to be 0.

# Prerequisites
- **Polynomial ring** — Leading coefficient is a property of polynomials

# Key Properties
1. If R is an integral domain, the leading term of $fg$ is the product of the leading terms (Proposition 4)
2. Division algorithm in $F[x]$ requires dividing by the leading coefficient
3. A polynomial is monic iff its leading coefficient is 1

# Source Reference
Chapter 7, Section 7.2, page 235.

# Verification Notes
- Definition: Direct from p. 235
- Confidence: HIGH — explicit definition
