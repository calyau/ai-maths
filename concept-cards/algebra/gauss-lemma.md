---
concept: "Gauss's Lemma"
slug: gauss-lemma
category: factorization
subcategory: integer-polynomials
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Gauss's Lemma"
extraction_confidence: high
aliases: []
prerequisites:
  - primitive-polynomial
  - prime-element
extends: []
related:
  - unique-factorization-domain
  - factoring-integer-polynomials
contrasts_with: []
answers_questions:
  - "What is Gauss's Lemma?"
---

# Quick Definition

Gauss's Lemma states that the product of two primitive polynomials is primitive. This is the key result enabling the proof that Z[x] is a UFD.

# Core Definition

(Gauss's Lemma) The product of primitive polynomials is primitive (Artin, Proposition 12.3.4(b), p. 380).

The proof uses the fact that an integer prime p is a prime element of Z[x]: if p divides fg, then p divides f or g. Since neither primitive factor is divisible by p, neither is the product.

# Prerequisites

- **Primitive polynomial** -- The statement involves primitive polynomials
- **Prime element** -- An integer prime is prime in Z[x]

# Key Properties

1. Consequence: if a primitive polynomial divides an integer polynomial in Q[x], it divides it in Z[x] (Theorem 12.3.6)
2. This bridges factorization in Z[x] and Q[x]
3. Leads to Z[x] being a UFD (Theorem 12.3.8)

# Context & Application

Gauss's Lemma is the bridge between factoring in Z[x] and Q[x]. It shows that integer polynomials that are irreducible in Q[x] remain irreducible in Z[x] (up to content).

# Examples

**Example 1** (p. 379): (2x + 1)(x^2 + x + 1) is primitive since both factors are.

# Relationships

## Builds Upon
- **Primitive polynomial** -- The product of primitives is primitive

## Enables
- **Z[x] is a UFD** -- Theorem 12.3.8 follows from Gauss's Lemma

# Source Reference

Chapter 12: Factoring, Section 12.3, Proposition 12.3.4, pages 380-381.

# Verification Notes

- Definition source: Direct from Proposition 12.3.4
- Confidence rationale: Explicit theorem statement with proof
- Uncertainties: None
- Cross-reference status: Verified
