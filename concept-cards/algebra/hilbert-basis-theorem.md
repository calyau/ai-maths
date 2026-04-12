---
concept: Hilbert Basis Theorem
slug: hilbert-basis-theorem
category: module-theory
subcategory: ring-properties
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.6 Noetherian Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - noetherian-ring
extends: []
related:
  - polynomial-ring-several-variables
contrasts_with: []
answers_questions:
  - "Why is the polynomial ring over a Noetherian ring Noetherian?"
---

# Quick Definition

The Hilbert Basis Theorem states that if R is a Noetherian ring, then the polynomial ring R[x] is also Noetherian. By induction, R[x_1, ..., x_n] is Noetherian.

# Core Definition

Let R be a Noetherian ring. The polynomial ring R[x] is Noetherian (Artin, Theorem 14.6.7). By induction, this shows that the polynomial ring R[x_1, ..., x_n] in several variables over a Noetherian ring R is Noetherian. Therefore Z[x_1, ..., x_n] and F[x_1, ..., x_n] (F a field) are Noetherian.

# Prerequisites

- **Noetherian ring** -- The theorem assumes the base ring is Noetherian

# Key Properties

1. R[x] Noetherian implies R[x_1, ..., x_n] Noetherian by induction
2. Quotients of Noetherian rings are Noetherian (14.6.8)
3. Any ring isomorphic to a quotient P/I, where P is a polynomial ring over Z or a field, is Noetherian (14.6.9)

# Context & Application

This theorem ensures that the rings arising most commonly in algebra are Noetherian, guaranteeing the finite generation of ideals and submodules needed for the theory of generators and relations.

# Examples

**Example 1** (p. 449): Z[x_1, ..., x_n] is Noetherian, since Z is Noetherian and we apply the theorem n times.

**Example 2** (p. 449): F[x_1, ..., x_n] for any field F is Noetherian.

# Relationships

## Builds Upon
- **Noetherian ring** -- The hypothesis of the theorem

## Enables
- **Finite generation of submodules** -- Over polynomial rings
- **Polynomial rings in several variables** -- Section 14.9

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.6, pages 449-451. Theorem 14.6.7.

# Verification Notes

- Definition source: Direct theorem statement from Artin, Theorem 14.6.7
- Confidence rationale: Complete proof provided
- Uncertainties: None
- Cross-reference status: Verified
