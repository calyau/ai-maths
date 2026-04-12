---
concept: Computing the Class Group
slug: computing-the-class-group
category: number-theory
subcategory: class-group
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Computing the Class Group"
extraction_confidence: high
aliases: []
prerequisites:
  - class-group
  - minkowski-bound
  - split-prime
extends: []
related:
  - class-number
contrasts_with: []
answers_questions:
  - "How do I find the class group of a quadratic number field?"
---

# Quick Definition

To compute the class group: (1) compute the Minkowski bound mu, (2) determine which primes p < mu split, ramify, or remain inert, (3) the splitting/ramifying primes generate the class group, (4) compute norms of small elements to find relations.

# Core Definition

The procedure to compute the class group C of the ring of integers R in Q[sqrt(d)] is: first compute mu (the Minkowski bound). Then examine each prime p <= floor(mu): if p splits or ramifies, include a prime factor as a generator. Discard inert primes. Then compute norms of elements a + b*delta to discover relations among generators (Artin, Section 13.8, pp. 416-419).

# Prerequisites

- **Class group** -- What we are computing
- **Minkowski bound** -- Limits the primes to examine
- **Split prime** -- Determines which primes contribute generators

# Key Properties

1. Only finitely many primes need examination
2. Relations come from norm computations: if N(alpha) = p^i q^j s^k, this gives a class group relation
3. If no primes split, the class group is trivial
4. The prime 2 ramifies when d = 2 or 3 mod 4 (and d < -2), giving an element of order 2

# Construction / Recognition

## To Compute:
1. Compute mu from d
2. List primes p <= floor(mu)
3. For each p, check if x^2 - d has a root mod p (splitting test)
4. Splitting/ramifying primes give generators
5. Compute N(a + b*delta) for small a, b to find relations
6. Determine the group structure from generators and relations

# Examples

**Example 1** (p. 416): d = -163: mu ~ 8.28, primes 2,3,5,7 all remain inert. C is trivial, R is a UFD.

**Example 2** (p. 414): d = -26: primes 2,3,5 all split. Norms N(1+delta) = 27, N(2+delta) = 30 give relations. C = C_6.

# Relationships

## Builds Upon
- **Class group** -- The object being computed
- **Minkowski bound** -- Bounds the search

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.8, pages 416-419.

# Verification Notes

- Definition source: Synthesized from Section 13.8 procedure
- Confidence rationale: Multiple worked examples demonstrate the method
- Uncertainties: None
- Cross-reference status: Verified
