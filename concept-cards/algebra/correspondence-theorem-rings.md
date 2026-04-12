---
concept: Correspondence Theorem (Rings)
slug: correspondence-theorem-rings
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
  - "lattice isomorphism theorem for rings"
prerequisites:
  - quotient-ring
  - ring-homomorphism
extends: []
related:
  - first-isomorphism-theorem-rings
contrasts_with: []
answers_questions:
  - "How do ideals relate to quotient rings?"
---

# Quick Definition

The Correspondence Theorem establishes a bijection between ideals of R containing K and ideals of R/K, where K is the kernel of a surjective homomorphism. Corresponding quotient rings are isomorphic.

# Core Definition

Let phi: R -> R' be a surjective ring homomorphism with kernel K. There is a bijective correspondence between ideals of R that contain K and ideals of R'. If I corresponds to I', then R/I ~ R'/I' (Artin, Theorem 11.4.3, p. 353).

# Prerequisites

- **Quotient ring** -- Relates ideals of R and R/K
- **Ring homomorphism** -- Requires a surjective homomorphism

# Key Properties

1. The bijection: I in R maps to phi(I) in R'; J in R' maps to phi^{-1}(J) in R
2. Quotient rings of corresponding ideals are isomorphic
3. Adding relations one at a time or all at once gives isomorphic results

# Context & Application

This theorem allows systematic analysis of ideals in quotient rings by studying ideals in the original ring. It is essential for understanding the structure of quotient rings.

# Examples

**Example 1** (p. 354): The ideals of C[t]/(t^2-1) correspond to the monic divisors of t^2-1, giving exactly four ideals.

# Relationships

## Builds Upon
- **Quotient ring** -- Describes the ideal structure of quotients

## Enables
- **Adjoining elements** -- Shows that adding relations in different orders gives the same result

# Source Reference

Chapter 11: Rings, Section 11.4, Theorem 11.4.3, pages 353-354.

# Verification Notes

- Definition source: Direct from Theorem 11.4.3
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
