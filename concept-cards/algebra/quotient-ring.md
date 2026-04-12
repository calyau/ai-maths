---
concept: Quotient Ring
slug: quotient-ring
category: ring-theory
subcategory: quotient-constructions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Quotient Rings"
extraction_confidence: high
aliases:
  - "factor ring"
  - "R/I"
prerequisites:
  - ring
  - ideal
extends: []
related:
  - first-isomorphism-theorem-rings
  - correspondence-theorem-rings
  - canonical-map
contrasts_with: []
answers_questions:
  - "How do ideals relate to quotient rings?"
---

# Quick Definition

The quotient ring R/I is the set of additive cosets of an ideal I in a ring R, with multiplication defined by [a+I][b+I] = [ab+I]. The canonical map pi: R -> R/I sending a to its coset is a surjective ring homomorphism with kernel I.

# Core Definition

Let I be an ideal of a ring R. There is a unique ring structure on the set R-bar of additive cosets of I such that the map pi: R -> R-bar that sends a to a-bar = [a + I] is a ring homomorphism. The kernel of pi is I (Artin, Theorem 11.4.1, p. 351).

# Prerequisites

- **Ring** -- The ambient ring
- **Ideal** -- Needed to form cosets

# Key Properties

1. Elements of R/I are cosets a + I
2. Addition and multiplication are well-defined on cosets
3. The canonical map pi: R -> R/I is a surjective ring homomorphism
4. ker(pi) = I

# Construction / Recognition

## To Construct:
1. Start with a ring R and an ideal I
2. Form the set of cosets {a + I | a in R}
3. Define addition: (a+I) + (b+I) = (a+b) + I
4. Define multiplication: (a+I)(b+I) = ab + I

# Context & Application

Quotient rings are the ring-theoretic analogue of quotient groups. They provide "new" rings: for example, C[x,y]/(y^2 - x^3 + 1) is the coordinate ring of an elliptic curve.

# Examples

**Example 1** (p. 351): Z/(n) = Z/nZ is the ring of integers modulo n.

**Example 2** (p. 352): The ring R[x]/(x^2 + 1) is isomorphic to C.

# Relationships

## Builds Upon
- **Ring** -- R is the ambient ring
- **Ideal** -- I defines the cosets

## Enables
- **First Isomorphism Theorem (rings)** -- R/ker(phi) ~ im(phi)
- **Adjoining elements** -- R[alpha] = R[x]/(f) adjoins a root of f

# Source Reference

Chapter 11: Rings, Section 11.4 "Quotient Rings," Theorem 11.4.1, pages 351-352.

# Verification Notes

- Definition source: Direct from Theorem 11.4.1
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
