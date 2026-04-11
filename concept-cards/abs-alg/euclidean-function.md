---
concept: Euclidean Function
slug: euclidean-function
category: ring-theory
subcategory: special-domains
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 270
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "norm on an integral domain"
  - "Euclidean norm"
prerequisites:
  - integral-domain
extends: []
related:
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is a norm on an integral domain?"
  - "What is a Euclidean function?"
---

# Quick Definition
A norm on an integral domain R is a function $N: R \to \mathbb{Z}^+ \cup \{0\}$ with $N(0) = 0$. It is a Euclidean function if it enables a division algorithm: for $b \neq 0$, $a = qb + r$ with $r = 0$ or $N(r) < N(b)$.

# Core Definition
Any function $N: R \to \mathbb{Z}^+ \cup \{0\}$ with $N(0) = 0$ is called a *norm* on the integral domain R. If $N(a) > 0$ for $a \neq 0$, it is a *positive norm*. The norm makes R a Euclidean Domain if for any $a, b \in R$ with $b \neq 0$, there exist $q, r \in R$ with $a = qb + r$ and $r = 0$ or $N(r) < N(b)$ (Dummit & Foote, pp. 270-271).

# Prerequisites
- **Integral domain** — Norms are defined on integral domains

# Key Properties
1. The same domain may possess several different norms (p. 271)
2. The norm need not be multiplicative
3. A ring can be Euclidean with respect to one norm but not another

# Construction / Recognition
## Common Norms:
1. $\mathbb{Z}$: $N(a) = |a|$ (absolute value)
2. $F[x]$: $N(p(x)) = \deg(p(x))$ (degree)
3. $\mathbb{Z}[i]$: $N(a+bi) = a^2 + b^2$ (field norm)

# Examples
**Example 1** (p. 272): On $\mathbb{Z}$, $N(a) = |a|$ is a Euclidean function.

**Example 2** (p. 272): On $F[x]$, $N(p) = \deg(p)$ is a Euclidean function.

**Example 3** (p. 273): On $\mathbb{Z}[i]$, $N(a+bi) = a^2+b^2$ is a Euclidean function.

# Relationships

## Related
- **euclidean-domain** — A domain with a Euclidean function

# Source Reference
Chapter 8, Section 8.1, Definitions on pages 270-271.

# Verification Notes
- Definition: Direct from pp. 270-271
- Confidence: HIGH — explicit definitions
