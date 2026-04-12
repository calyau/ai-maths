---
concept: Ramified Prime
slug: ramified-prime
category: number-theory
subcategory: prime-decomposition
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Prime Ideals and Prime Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - prime-ideal
  - ring-of-integers
extends: []
related:
  - split-prime
  - inert-prime
contrasts_with:
  - split-prime
  - inert-prime
answers_questions:
  - "What is a ramified prime?"
---

# Quick Definition

An integer prime p ramifies in R if (p) = P^2 for a prime ideal P (i.e., P = P-bar). For d = 2 or 3 mod 4, the prime 2 always ramifies, and an odd prime p ramifies iff p divides d.

# Core Definition

An integer prime p ramifies if (p) = P*P-bar and P = P-bar, so (p) = P^2 (Artin, p. 408). For d = 2 or 3 mod 4: 2 always ramifies, and an odd prime p ramifies iff p | d (Lemma 13.8.4, Exercise 6.5).

# Prerequisites

- **Prime ideal** -- P is a prime ideal with P = P-bar
- **Ring of integers** -- Context is R

# Key Properties

1. (p) = P^2 where P is self-conjugate
2. 2 ramifies in all quadratic integer rings with d = 2 or 3 mod 4
3. The class (P) has order 2 in the class group (or order 1 if P is principal)
4. There are only finitely many ramified primes for each d

# Examples

**Example 1** (p. 408): In Z[sqrt(-5)], 2 ramifies: (2) = A^2 where A = (2, 1+sqrt(-5)).

# Relationships

## Contrasts With
- **Split prime** -- Ramified has P = P-bar; split has P != P-bar
- **Inert prime** -- Ramified means (p) factors; inert means it doesn't

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.6, page 408, Lemma 13.8.4.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
