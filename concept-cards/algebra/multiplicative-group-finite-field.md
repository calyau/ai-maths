---
concept: Multiplicative Group of a Finite Field
slug: multiplicative-group-finite-field
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
extraction_confidence: high
aliases:
  - "K*"
  - "F_q*"
prerequisites:
  - finite-field
extends: []
related:
  - cyclic-group
  - frobenius-endomorphism
contrasts_with: []
answers_questions:
  - "What is the multiplicative group of a finite field?"
  - "Why is it cyclic?"
---

# Quick Definition

The multiplicative group K* of a finite field K of order q consists of the q-1 nonzero elements, and it is always a cyclic group of order q-1.

# Core Definition

Let K be a field of order q. The multiplicative group K* of nonzero elements is a cyclic group of order q-1 (Artin, Theorem 15.7.3(c)). The proof uses the Structure Theorem for abelian groups: if K* were not cyclic, every element would satisfy x^d = 1 for some d < q-1, giving at most d roots for a degree-d polynomial, contradicting |K*| = q-1.

# Prerequisites

- **Finite field** -- K must be a finite field

# Key Properties

1. K* is cyclic of order q-1
2. A generator for K* is called a primitive element of K
3. A generator alpha for K* also generates K as a field extension: K = F_p(alpha)
4. This holds for any finite field, regardless of characteristic

# Context & Application

The cyclicity of K* is essential for the theory of finite fields. It implies the existence of primitive elements and irreducible polynomials of every degree.

# Examples

**Example 1** (p. 473): F_4* is cyclic of order 3.

**Example 2** (p. 474): F_8* is cyclic of order 7.

# Relationships

## Builds Upon
- **Finite field** -- The field whose multiplicative group is being described

## Related
- **Cyclic group** -- K* is always cyclic

# Source Reference

Chapter 15: Fields, Section 15.7, pages 473-478. Theorem 15.7.3(c).

# Verification Notes

- Definition source: Direct from Artin, Theorem 15.7.3(c)
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
