---
concept: Separable Polynomial
slug: separable-polynomial
category: field-theory
subcategory: polynomials
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.6 Adjoining Roots"
extraction_confidence: high
aliases:
  - "separable"
prerequisites:
  - irreducible-polynomial
  - field-extension
extends: []
related:
  - inseparable-polynomial
  - galois-extension
contrasts_with:
  - inseparable-polynomial
answers_questions:
  - "What is a separable polynomial?"
---

# Quick Definition

A polynomial is separable if it has no multiple roots in any extension field. Over a field of characteristic zero, every irreducible polynomial is separable. Multiple roots can occur only in characteristic p.

# Core Definition

An irreducible polynomial f in F[x] has no multiple root in any extension field unless the derivative f' is the zero polynomial (Artin, Proposition 15.6.8). In characteristic zero, f' is never zero for a nonconstant f, so every irreducible polynomial is separable (15.6.8(b)). The derivative f' is zero only when every exponent appearing in f is divisible by the characteristic p.

# Prerequisites

- **Irreducible polynomial** -- Separability is primarily for irreducible polynomials
- **Field extension** -- Roots live in extension fields

# Key Properties

1. In characteristic zero, every irreducible polynomial is separable (15.6.8(b))
2. f has a multiple root iff f and f' are not relatively prime (15.6.7)
3. An irreducible f has a multiple root iff f' = 0 (15.6.8(a))
4. In characteristic p, f' = 0 iff all exponents in f are divisible by p

# Context & Application

Separability is crucial for Galois theory. In characteristic zero (Artin's setting from Section 16.4 onward), separability is automatic, which simplifies the theory. Distinct roots are needed for the Galois group to act faithfully.

# Examples

**Example 1** (p. 471): In characteristic 5, f(x) = x^{15} + ax^{10} + bx^5 + c has f'(x) = 0, so all roots are multiple.

# Relationships

## Builds Upon
- **Irreducible polynomial** -- Separability is defined for irreducible polynomials

## Enables
- **Galois extension** -- Requires separability of the minimal polynomial

## Contrasts With
- **Inseparable polynomial** -- Has multiple roots (only in characteristic p)

# Source Reference

Chapter 15: Fields, Section 15.6, pages 470-472. Propositions 15.6.7 and 15.6.8.

# Verification Notes

- Definition source: Synthesized from Artin, Propositions 15.6.7-15.6.8
- Confidence rationale: Clear characterization via derivatives
- Uncertainties: None
- Cross-reference status: Verified
