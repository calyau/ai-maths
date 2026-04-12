---
concept: Finite Field
slug: finite-field
category: field-theory
subcategory: field-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.7 Finite Fields"
extraction_confidence: high
aliases:
  - "Galois field"
  - "F_q"
prerequisites:
  - field-extension
  - prime-field
extends: []
related:
  - frobenius-endomorphism
  - multiplicative-group-finite-field
contrasts_with: []
answers_questions:
  - "What is a finite field?"
  - "How many elements can a finite field have?"
---

# Quick Definition

A finite field is a field with finitely many elements. The order of a finite field is always a prime power q = p^r, and for each prime power there exists a unique (up to isomorphism) finite field F_q.

# Core Definition

A finite field K has characteristic p (a prime), contains the prime field F_p, and has order |K| = p^r = q where r = [K:F_p] (Artin, p. 473). The main facts (Theorem 15.7.3): (a) elements of K are roots of x^q - x; (b) irreducible factors of x^q - x over F_p are exactly the irreducible polynomials whose degree divides r; (c) the multiplicative group K* is cyclic of order q-1; (d) there exists a field of order q, and all fields of order q are isomorphic; (e) F_{p^r} contains F_{p^k} as a subfield iff k divides r.

# Prerequisites

- **Field extension** -- Finite fields are extensions of prime fields
- **Prime field** -- Every finite field contains a prime field F_p

# Key Properties

1. The order is always a prime power p^r
2. The multiplicative group K* is cyclic of order q-1 (15.7.3(c))
3. All fields of the same order are isomorphic (15.7.3(d))
4. For every prime power q, there exists a field F_q (15.7.3(d))
5. Subfield containment: F_{p^k} in F_{p^r} iff k | r (15.7.3(e))
6. For every positive integer r, there exists an irreducible polynomial of degree r over F_p (Corollary 15.7.4)

# Construction / Recognition

## To Construct:
1. Choose a prime p and positive integer r
2. Find an irreducible polynomial f of degree r over F_p
3. F_{p^r} = F_p[x]/(f)

## To Recognize:
1. Count elements: must be a prime power p^r
2. Verify field axioms (or that it's a subfield of a known field)

# Context & Application

Finite fields are fundamental in coding theory, cryptography, and algebraic geometry. Their complete classification (one field of each prime power order, all isomorphic) is remarkably clean.

# Examples

**Example 1** (p. 473-474): F_4 = F_2[alpha]/(alpha^2 + alpha + 1) = {0, 1, alpha, 1+alpha}. The multiplicative group F_4* is cyclic of order 3.

**Example 2** (p. 474): F_8 = F_2[beta]/(beta^3 + beta + 1) has 8 elements. The factorization x^8 - x = x(x-1)(x^3+x+1)(x^3+x^2+1) over F_2 shows the two irreducible cubics.

**Example 3** (p. 475): F_8 does not contain F_4 because 2 does not divide 3.

# Relationships

## Builds Upon
- **Field extension** -- Finite fields are finite extensions of prime fields

## Enables
- **Frobenius endomorphism** -- The map x -> x^p on finite fields

## Related
- **Multiplicative group of a finite field** -- Always cyclic

# Common Confusions

- **Confusion**: Confusing the finite field F_4 with Z/4Z
  **Clarification**: Z/4Z is not a field (2 is a zero divisor). F_4 has characteristic 2 but is a proper extension of F_2.

# Source Reference

Chapter 15: Fields, Section 15.7, pages 473-478. Theorem 15.7.3.

# Verification Notes

- Definition source: Direct from Artin, Theorem 15.7.3
- Confidence rationale: Complete classification with proofs
- Uncertainties: None
- Cross-reference status: Verified
