---
concept: Inert Prime
slug: inert-prime
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
  - "prime that remains prime"
prerequisites:
  - prime-ideal
  - ring-of-integers
extends: []
related:
  - split-prime
  - ramified-prime
contrasts_with:
  - split-prime
  - ramified-prime
answers_questions:
  - "What is an inert prime?"
---

# Quick Definition

An integer prime p is inert (remains prime) in R if the principal ideal (p) is itself a prime ideal of R. This happens when x^2 - d is irreducible mod p.

# Core Definition

An integer prime p remains prime (is inert) if the principal ideal (p) = pR is a prime ideal of R (Artin, p. 408). For d = 2 or 3 mod 4, p remains prime iff x^2 - d is irreducible in F_p[x], iff d is not a square mod p (Theorem 13.6.1(c)).

# Prerequisites

- **Prime ideal** -- (p) must be a prime ideal
- **Ring of integers** -- Context is R

# Key Properties

1. R/(p) is a field with p^2 elements when p is inert
2. Determined by irreducibility of x^2 - d mod p

# Examples

**Example 1** (p. 411): In Z[sqrt(-5)], 7 remains prime since x^2 + 5 is irreducible mod 7.

# Relationships

## Contrasts With
- **Split prime** -- Split means (p) = P*P-bar; inert means (p) is already prime

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.6, Theorem 13.6.1, page 408.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
