---
concept: Greatest Common Divisor
slug: greatest-common-divisor
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
  - "g.c.d."
  - "gcd"
prerequisites:
  - set
extends: []
related:
  - division-algorithm
  - euclidean-algorithm
  - prime
  - euler-phi-function
contrasts_with: []
answers_questions:
  - "What is the greatest common divisor of two integers?"
  - "What does it mean for two integers to be relatively prime?"
---

# Quick Definition
The greatest common divisor of nonzero integers a and b is the unique positive integer d that divides both a and b and is divisible by every common divisor. It is denoted (a,b). If (a,b) = 1, then a and b are relatively prime.

# Core Definition
If $a, b \in \mathbb{Z} - \{0\}$, there is a unique positive integer d, called the *greatest common divisor* of a and b, satisfying: (a) $d \mid a$ and $d \mid b$, and (b) if $e \mid a$ and $e \mid b$, then $e \mid d$. The g.c.d. is denoted $(a,b)$. If $(a,b) = 1$, a and b are *relatively prime*. Furthermore, there exist integers x, y such that $(a,b) = ax + by$ (Dummit & Foote, pp. 4-6).

# Prerequisites
- **Set** — integers as a set

# Key Properties
1. $(a,b) = ax + by$ for some integers x, y (Bezout's identity)
2. If p is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$
3. The g.c.d. can be computed efficiently by the Euclidean Algorithm
4. Connection to l.c.m.: $dl = ab$ where d is the g.c.d. and l the l.c.m.

# Construction / Recognition
## To Construct/Create:
1. Apply the Euclidean Algorithm to a and b
2. The last nonzero remainder is $(a,b)$
3. Back-substitute to express $(a,b)$ as $ax + by$

# Context & Application
The g.c.d. is essential for determining generators of cyclic groups, computing orders of elements in $\mathbb{Z}/n\mathbb{Z}$, and finding multiplicative inverses in $(\mathbb{Z}/n\mathbb{Z})^\times$. Relatively prime integers characterize invertible residue classes.

# Examples
**Example 1** (p. 5): $(57970, 10353) = 17$, computed via the Euclidean Algorithm.
**Example 2** (p. 6): $17 = (302)57970 - (1691)10353$ expresses the g.c.d. as a linear combination.

# Relationships
## Builds Upon
None within this source.

## Enables
- **congruence-mod-n** — relatively prime integers have multiplicative inverses mod n
- **cyclic-group** — generators of $\mathbb{Z}/n\mathbb{Z}$ are residue classes with $(a,n) = 1$
- **euler-phi-function** — counts integers relatively prime to n

## Related
- **euclidean-algorithm** — computes the g.c.d.
- **division-algorithm** — foundation for the Euclidean Algorithm

# Common Errors
- **Error**: Computing the g.c.d. via prime factorization for large integers. **Correction**: The Euclidean Algorithm is far more efficient; prime factorization is computationally expensive for large numbers.

# Common Confusions
- **Confusion**: Confusing "greatest" with numerically largest common divisor. **Clarification**: The g.c.d. d is greatest in the divisibility sense: every common divisor divides d.

# Source Reference
Chapter 0: Preliminaries, Section 0.2 "Properties of the Integers," pages 4-6.

# Verification Notes
- Definition source: direct from source pp. 4-5
- Confidence rationale: explicitly defined with worked examples
- Uncertainties: none
- Cross-reference status: verified
