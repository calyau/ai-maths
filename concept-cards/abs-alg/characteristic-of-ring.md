---
concept: Characteristic of a Ring
slug: characteristic-of-ring
category: ring-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 250
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring-with-identity
extends: []
related:
  - integral-domain
  - field
contrasts_with: []
answers_questions:
  - "What is the characteristic of a ring?"
---

# Quick Definition
The characteristic of a ring R with identity is the smallest positive integer n such that $\underbrace{1 + 1 + \cdots + 1}_{n} = 0$; if no such n exists, the characteristic is 0.

# Core Definition
The *characteristic* of a ring R is the smallest positive integer n such that $1 + 1 + \cdots + 1 = 0$ (n times) in R; if no such integer exists the characteristic is said to be 0 (Exercise 26, Dummit & Foote, p. 250).

# Prerequisites
- **Ring with identity** — The characteristic uses the multiplicative identity 1

# Key Properties
1. The map $\mathbb{Z} \to R$ by $k \mapsto k \cdot 1$ is a ring homomorphism with kernel $n\mathbb{Z}$ (Exercise 26(a))
2. An integral domain has characteristic 0 or prime p (Exercise 28, p. 251)
3. $\mathbb{Z}/n\mathbb{Z}$ has characteristic n
4. $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ have characteristic 0
5. In characteristic p (prime): $(a+b)^p = a^p + b^p$ in commutative rings (Exercise 26(c))

# Examples
**Example 1**: $\mathbb{Z}$ has characteristic 0.

**Example 2**: $\mathbb{Z}/n\mathbb{Z}$ has characteristic n.

**Example 3**: Any field of characteristic 0 contains a copy of $\mathbb{Q}$; any field of characteristic p contains $\mathbb{Z}/p\mathbb{Z}$.

# Relationships

## Related
- **integral-domain** — Integral domains have characteristic 0 or prime
- **field** — Fields have characteristic 0 or prime

# Source Reference
Chapter 7, Section 7.3, Exercise 26, page 250.

# Verification Notes
- Definition: From Exercise 26, p. 250
- Confidence: HIGH — standard definition
