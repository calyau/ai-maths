---
concept: Frobenius Endomorphism
slug: frobenius-endomorphism
category: field-theory
subcategory: finite-fields
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.7 Finite Fields"
extraction_confidence: medium
aliases:
  - "Frobenius map"
prerequisites:
  - finite-field
extends: []
related:
  - multiplicative-group-finite-field
contrasts_with: []
answers_questions:
  - "What is the Frobenius endomorphism?"
---

# Quick Definition

The Frobenius endomorphism of a field of characteristic p is the map x -> x^p. Over a finite field F_q with q = p^r, the Frobenius generates the Galois group of F_q over F_p, which is cyclic of order r.

# Core Definition

In a field F of prime characteristic p, the map phi: x -> x^p is a field endomorphism. This follows from the identity (x + y)^p = x^p + y^p in characteristic p (Artin, Lemma 15.7.10(b)). For a finite field F_q = F_{p^r}, the Frobenius phi: x -> x^p generates the cyclic Galois group of F_q over F_p, which has order r.

# Prerequisites

- **Finite field** -- The Frobenius acts on fields of characteristic p

# Key Properties

1. (x + y)^p = x^p + y^p in characteristic p (15.7.10(b))
2. The Frobenius is always injective (hence bijective on finite fields)
3. The elements fixed by x -> x^q are exactly the elements of F_q (they are roots of x^q - x)
4. The Frobenius generates the Galois group Gal(F_{p^r}/F_p)

# Context & Application

The Frobenius endomorphism is the fundamental automorphism in the theory of finite fields and plays a central role in algebraic geometry over finite fields and in number theory.

# Examples

**Example 1** (p. 477): Over F_4 = {0, 1, alpha, 1+alpha}, the Frobenius x -> x^2 sends alpha to alpha^2 = 1 + alpha and 1 + alpha to (1+alpha)^2 = alpha.

# Relationships

## Builds Upon
- **Finite field** -- The Frobenius acts on finite fields

## Related
- **Galois group** -- The Frobenius generates the Galois group of F_{p^r}/F_p

# Source Reference

Chapter 15: Fields, Section 15.7, pages 476-478. Lemma 15.7.10.

# Verification Notes

- Definition source: Synthesized from Artin's treatment of finite fields
- Confidence rationale: The map is defined implicitly; explicit definition synthesized
- Uncertainties: Artin does not name it "Frobenius" explicitly
- Cross-reference status: Verified
