---
concept: Euclidean Algorithm
slug: euclidean-algorithm
category: ring-theory
subcategory: special-domains
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 271
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - euclidean-domain
extends: []
related:
  - gcd-in-ring
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is the Euclidean Algorithm?"
  - "How do you compute GCDs in Euclidean Domains?"
---

# Quick Definition
The Euclidean Algorithm repeatedly applies the division algorithm: $a = q_0 b + r_0$, $b = q_1 r_0 + r_1$, ..., until reaching a zero remainder. The last nonzero remainder is the GCD.

# Core Definition
By successive divisions in a Euclidean Domain R, $a = q_0 b + r_0$, $b = q_1 r_0 + r_1$, ..., $r_{n-1} = q_{n+1} r_n$, the last nonzero remainder $r_n$ is a greatest common divisor of a and b, and $r_n = ax + by$ for some $x, y \in R$ (Theorem 4, Dummit & Foote, pp. 271, 276).

# Prerequisites
- **Euclidean domain** — The algorithm works in Euclidean Domains

# Key Properties
1. Terminates because norms form a decreasing sequence of nonneg. integers
2. The last nonzero remainder generates the ideal $(a, b)$ (Theorem 4)
3. The GCD can be written as a linear combination of a and b (back-substitution)
4. In $\mathbb{Z}$: requires at most $5 \times (\text{number of digits of smaller input})$ steps (p. 278)

# Examples
**Example** (p. 278): $\gcd(2210, 1131) = 13$ via: $2210 = 1 \cdot 1131 + 1079$, $1131 = 1 \cdot 1079 + 52$, $1079 = 20 \cdot 52 + 39$, $52 = 1 \cdot 39 + 13$, $39 = 3 \cdot 13$. Then $13 = (-22)(2210) + (43)(1131)$.

# Relationships

## Related
- **gcd-in-ring** — The algorithm computes GCDs
- **euclidean-domain** — The algorithm uses the division algorithm

# Source Reference
Chapter 8, Section 8.1, Theorem 4, pages 271-278.

# Verification Notes
- Definition: Direct from pp. 271, 276
- Confidence: HIGH — explicit algorithm with worked examples
