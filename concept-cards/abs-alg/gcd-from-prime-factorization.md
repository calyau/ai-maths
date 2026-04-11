---
concept: GCD from Prime Factorization
slug: gcd-from-prime-factorization
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 287
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - unique-factorization-domain
  - gcd-in-ring
extends: []
related:
  - gcd-in-ring
  - euclidean-algorithm
contrasts_with: []
answers_questions:
  - "How do you compute GCDs in a UFD using prime factorizations?"
---

# Quick Definition
In a UFD, if $a = u p_1^{e_1} \cdots p_n^{e_n}$ and $b = v p_1^{f_1} \cdots p_n^{f_n}$, then $\gcd(a, b) = p_1^{\min(e_1, f_1)} \cdots p_n^{\min(e_n, f_n)}$.

# Core Definition
(Proposition 13) In a UFD with prime factorizations $a = u \prod p_i^{e_i}$ and $b = v \prod p_i^{f_i}$ (allowing $e_i = 0$ or $f_i = 0$), the element $d = \prod p_i^{\min(e_i, f_i)}$ is a greatest common divisor of a and b (Dummit & Foote, pp. 287-288).

# Prerequisites
- **Unique factorization domain** — Need unique factorization
- **GCD in ring** — Computing GCDs

# Key Properties
1. Gives GCD instantly from known factorizations
2. Finding prime factorizations is computationally much harder than the Euclidean Algorithm
3. The Euclidean Algorithm is faster but gives no factorization information

# Examples
**Example** (p. 289): $2210 = 2 \cdot 5 \cdot 13 \cdot 17$ and $1131 = 3 \cdot 13 \cdot 29$, so $\gcd(2210, 1131) = 13$.

# Source Reference
Chapter 8, Section 8.3, Proposition 13, pages 287-288.

# Verification Notes
- Definition: Direct from Proposition 13, pp. 287-288
- Confidence: HIGH — explicit proposition
