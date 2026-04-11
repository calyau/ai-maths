---
concept: Evaluation Homomorphism
slug: evaluation-homomorphism
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 247
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "substitution homomorphism"
prerequisites:
  - polynomial-ring
  - ring-homomorphism
extends:
  - ring-homomorphism
related:
  - roots-of-polynomial
  - quotient-ring
contrasts_with: []
answers_questions:
  - "What is the evaluation homomorphism?"
  - "How does evaluating a polynomial define a ring homomorphism?"
---

# Quick Definition
The evaluation homomorphism at $c$ maps a polynomial $p(x)$ to $p(c)$, substituting the element c for the indeterminate x.

# Core Definition
Let A be a ring and R the ring of functions from a set X to A. For each fixed $c \in X$, the map $E_c: R \to A$ defined by $E_c(f) = f(c)$ (evaluation at c) is a ring homomorphism. For polynomial rings, the evaluation map $p(x) \mapsto p(c)$ from $R[x]$ to R is a surjective ring homomorphism (Dummit & Foote, pp. 247-248).

# Prerequisites
- **Polynomial ring** — The domain of the evaluation map
- **Ring homomorphism** — Evaluation is a ring homomorphism

# Key Properties
1. Evaluation at c is a surjective ring homomorphism
2. The kernel consists of all polynomials vanishing at c
3. For $R[x] \to R$ evaluating at 0: kernel = polynomials with zero constant term
4. Evaluation at 0 maps $p(x) \mapsto p(0)$ (the constant term)

# Examples
**Example 1** (p. 241): $\mathbb{Q}[x] \to \mathbb{Q}$ defined by $p(x) \mapsto p(0)$ has kernel = polynomials with zero constant term.

**Example 2** (p. 247): For the ring of continuous functions on $[0,1]$, evaluation at $c$ has kernel $\{f \mid f(c) = 0\}$, giving $R/\ker E_c \cong \mathbb{R}$.

# Relationships

## Enables
- **roots-of-polynomial** — $\alpha$ is a root of $p(x)$ iff $\alpha \in \ker(E_\alpha)$ applied to $p$

## Related
- **quotient-ring** — $R[x]/\ker(E_c) \cong R$

# Source Reference
Chapter 7, Section 7.3, Examples 4-5, pages 247-248.

# Verification Notes
- Definition: From examples in pp. 247-248
- Confidence: HIGH — explicit construction
