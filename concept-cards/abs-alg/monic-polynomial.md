---
concept: Monic Polynomial
slug: monic-polynomial
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
aliases: []
prerequisites:
  - polynomial-ring
  - degree-of-polynomial
extends: []
related:
  - leading-coefficient
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "What is a monic polynomial?"
---

# Quick Definition
A polynomial is monic if its leading coefficient equals 1.

# Core Definition
A polynomial $a_nx^n + \cdots + a_0$ with $a_n \neq 0$ is *monic* if $a_n = 1$ (Dummit & Foote, p. 235).

# Prerequisites
- **Polynomial ring** — Monic is a property of polynomials
- **Degree of polynomial** — The leading coefficient is the coefficient of the highest-degree term

# Key Properties
1. A monic polynomial is always primitive (content = 1 if the ring has 1)
2. In a monic factorization $f = gh$, both g and h can be chosen monic (over an integral domain)
3. GCDs in $F[x]$ can be made unique by requiring them to be monic

# Source Reference
Chapter 7, Section 7.2, page 235.

# Verification Notes
- Definition: Direct from p. 235
- Confidence: HIGH — explicit definition
