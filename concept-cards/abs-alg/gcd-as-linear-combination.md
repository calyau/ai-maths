---
concept: GCD as Linear Combination
slug: gcd-as-linear-combination
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 276
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "Bezout's identity"
prerequisites:
  - euclidean-domain
  - gcd-in-ring
extends: []
related:
  - euclidean-algorithm
  - principal-ideal-domain
contrasts_with: []
answers_questions:
  - "Can the GCD always be written as a linear combination?"
---

# Quick Definition
In a Euclidean Domain (or PID), the GCD d of a and b can be written as $d = ax + by$ for some elements $x, y$ in the ring. This is Bezout's identity.

# Core Definition
(Theorem 4(2)) In a Euclidean Domain, $d = \gcd(a, b)$ generates the ideal $(a, b)$, so $d = ax + by$ for some $x, y \in R$. More generally, in any PID, $\gcd(a,b)$ can be written as a linear combination (Proposition 6, Dummit & Foote, pp. 276, 282).

# Prerequisites
- **Euclidean domain** — The algorithm computes the linear combination
- **GCD in ring** — d is the GCD of a and b

# Key Properties
1. Computed by back-substitution in the Euclidean Algorithm
2. The linear combination is not unique: if $d = ax_0 + by_0$, then $d = a(x_0 + mb/(a,b)) + b(y_0 - ma/(a,b))$
3. In a UFD that is not a PID, the GCD may NOT be expressible as a linear combination

# Examples
**Example** (p. 278): $13 = \gcd(2210, 1131) = (-22)(2210) + (43)(1131)$.

# Source Reference
Chapter 8, Section 8.1, Theorem 4(2), page 276; Section 8.2, Proposition 6, page 282.

# Verification Notes
- Definition: Direct from Theorem 4(2), p. 276
- Confidence: HIGH — explicit result
