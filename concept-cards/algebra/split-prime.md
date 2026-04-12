---
concept: Split Prime
slug: split-prime
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
aliases:
  - "splitting prime"
prerequisites:
  - prime-ideal
  - ring-of-integers
extends: []
related:
  - inert-prime
  - ramified-prime
contrasts_with:
  - inert-prime
  - ramified-prime
answers_questions:
  - "What does it mean for a prime to split?"
---

# Quick Definition

An integer prime p splits in the ring of integers R if (p) = P*P-bar where P != P-bar are distinct prime ideals. If additionally P = P-bar, then p ramifies. If (p) itself is prime, p is inert.

# Core Definition

An integer prime p is said to split if (p) = P*P-bar where P and P-bar are distinct conjugate prime ideals. It ramifies if P = P-bar. It remains prime (is inert) if (p) is itself a prime ideal of R (Artin, p. 408). For d = 2 or 3 mod 4: p remains prime iff x^2 - d is irreducible in F_p[x]; for d = 1 mod 4: p remains prime iff x^2 - x + h is irreducible in F_p[x] (Theorem 13.6.1).

# Prerequisites

- **Prime ideal** -- The factorization (p) = P*P-bar
- **Ring of integers** -- Working in R

# Key Properties

1. Every odd prime p either splits, ramifies, or remains prime
2. p splits iff d is a nonzero square mod p (when d = 2,3 mod 4)
3. p ramifies iff p | d or p = 2 (for d = 2,3 mod 4)
4. The behavior is determined by a polynomial modular irreducibility test

# Examples

**Example 1** (p. 408): In Z[sqrt(-5)], 3 splits: (3) = B*B-bar with B = (3, 1+delta).

**Example 2** (p. 408): In Z[sqrt(-5)], 2 ramifies: (2) = A^2 with A = (2, 1+delta).

# Relationships

## Related
- **Inert prime** -- (p) remains prime
- **Ramified prime** -- (p) = P^2

## Contrasts With
- **Inert prime** -- Splits vs remains prime
- **Ramified prime** -- Splits into distinct vs identical factors

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.6, Theorem 13.6.1, pages 407-409.

# Verification Notes

- Definition source: Direct from text and Theorem 13.6.1
- Confidence rationale: Explicit classification
- Uncertainties: None
- Cross-reference status: Verified
