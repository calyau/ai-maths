---
concept: Greatest Common Divisor (in Rings)
slug: gcd-in-ring
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 274
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "g.c.d."
  - "GCD"
prerequisites:
  - commutative-ring
  - principal-ideal
extends:
  - greatest-common-divisor
related:
  - euclidean-domain
  - principal-ideal-domain
contrasts_with: []
answers_questions:
  - "What is a greatest common divisor in a ring?"
  - "When do GCDs exist?"
---

# Quick Definition
A greatest common divisor of elements a and b in a commutative ring R is a nonzero element d that divides both a and b, and such that any common divisor of a and b also divides d.

# Core Definition
A *greatest common divisor* of a and b is a nonzero element d such that (i) $d \mid a$ and $d \mid b$, and (ii) if $d' \mid a$ and $d' \mid b$ then $d' \mid d$ (Dummit & Foote, p. 275).

# Prerequisites
- **Commutative ring** — GCDs are defined in commutative rings
- **Principal ideal** — GCDs are generators of the smallest principal ideal containing both elements

# Key Properties
1. GCD is unique up to associates (Proposition 3, p. 277)
2. In a PID: $\gcd(a,b)$ exists and $(a,b) = (d)$, with $d = ax + by$ (Proposition 6, p. 282)
3. In a Euclidean Domain: the Euclidean Algorithm computes GCDs efficiently (Theorem 4, p. 276)
4. In a UFD: GCD found from prime factorizations using min of exponents (Proposition 13, p. 287)
5. GCDs need not exist in all integral domains

# Construction / Recognition
## In a Euclidean Domain:
1. Apply the Euclidean Algorithm to find the last nonzero remainder
## In a UFD:
1. Factor both elements into primes
2. Take minimum exponent for each prime

# Examples
**Example 1** (p. 278): $\gcd(2210, 1131) = 13$ in $\mathbb{Z}$, computed via the Euclidean Algorithm.

**Example 2** (p. 278): $13 = (-22) \cdot 2210 + 43 \cdot 1131$ (as linear combination).

# Relationships

## Related
- **euclidean-domain** — GCDs computed algorithmically
- **principal-ideal-domain** — GCDs always exist

# Source Reference
Chapter 8, Section 8.1, Definition on page 275. See Theorem 4 and Propositions 2-3.

# Verification Notes
- Definition: Direct from p. 275
- Confidence: HIGH — explicit definition
