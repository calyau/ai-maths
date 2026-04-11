---
concept: Prime
slug: prime
category: foundations
subcategory: number-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.2 Properties of the Integers"
extraction_confidence: high
aliases:
  - "prime number"
prerequisites:
  - set
extends: []
related:
  - greatest-common-divisor
  - fundamental-theorem-of-arithmetic
contrasts_with: []
answers_questions:
  - "What is a prime number?"
  - "What is the key divisibility property of primes?"
---

# Quick Definition
A positive integer p > 1 is prime if its only positive divisors are 1 and p. Key property: if p divides ab, then p divides a or p divides b.

# Core Definition
An element $p \in \mathbb{Z}^+$ is *prime* if $p > 1$ and the only positive divisors of p are 1 and p. An integer $n > 1$ which is not prime is *composite*. The key property: if p is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$. The Fundamental Theorem of Arithmetic: every $n > 1$ can be factored uniquely as a product of primes (Dummit & Foote, pp. 5-6).

# Prerequisites
- **Set** — primes are elements of $\mathbb{Z}^+$

# Key Properties
1. If $p \mid ab$ then $p \mid a$ or $p \mid b$ (characterizing property)
2. Unique factorization into primes (Fundamental Theorem of Arithmetic)
3. $\varphi(p) = p - 1$ for prime p
4. $\mathbb{Z}/p\mathbb{Z}$ is a field when p is prime
5. Groups of prime order are cyclic (and simple)

# Context & Application
Primes are fundamental to number theory and group theory. Groups of prime order are cyclic. Cauchy's Theorem guarantees elements of prime order. The Sylow theorems concern prime power subgroups.

# Examples
**Example 1** (p. 5): 2, 3, 5, 7, 11, 13, 17, 19, ... are primes.
**Example 2** (p. 6): $1852423848 = 2^3 \cdot 3^2 \cdot 11^2 \cdot 19^3 \cdot 31$ (unique factorization).

# Relationships
## Builds Upon
None within this source.

## Enables
- **cyclic-group** — groups of prime order are cyclic
- **cauchy-theorem** — guarantees elements of prime order

## Related
- **greatest-common-divisor** — computed via prime factorization or Euclidean Algorithm

# Source Reference
Chapter 0, Section 0.2, pages 5-6.

# Verification Notes
- Definition source: direct from source p. 5
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
