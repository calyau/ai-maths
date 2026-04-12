---
concept: Splitting Theorem
slug: splitting-theorem
category: galois-theory
subcategory: main-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.3 Splitting Fields"
extraction_confidence: high
aliases:
  - "normal extension property"
prerequisites:
  - splitting-field
  - symmetric-functions-theorem
extends: []
related:
  - galois-extension
contrasts_with: []
answers_questions:
  - "What is the Splitting Theorem?"
---

# Quick Definition

If K is a splitting field over F, then any irreducible polynomial over F with at least one root in K splits completely in K. This characteristic property defines splitting fields.

# Core Definition

Let K be an extension of F that is a splitting field of a polynomial f(x) with coefficients in F. If an irreducible polynomial g(x) with coefficients in F has one root in K, then it splits completely in K (Artin, Theorem 16.3.2). The proof uses symmetric functions: the roots of g are evaluations of polynomials from the orbit of a polynomial p_1 expressing the known root in terms of the roots of f.

# Prerequisites

- **Splitting field** -- The theorem characterizes splitting fields
- **Symmetric Functions Theorem** -- Used in the proof

# Key Properties

1. This is the characteristic property of splitting fields
2. The proof depends essentially on the Symmetric Functions Theorem (16.1.6)
3. Equivalently: a splitting field is a finite extension where every irreducible polynomial with one root splits completely

# Context & Application

The Splitting Theorem is the key technical result connecting splitting fields to Galois extensions. It shows that splitting fields are "closed" under taking roots of irreducible polynomials.

# Examples

**Example 1**: If K is the splitting field of x^3 - 2 over Q, and g(x) = x^2 + x + 1 has a root omega in K, then g splits completely in K (both roots omega and omega^2 are in K).

# Relationships

## Builds Upon
- **Splitting field** -- The theorem characterizes them
- **Symmetric Functions Theorem** -- Used in the proof

## Enables
- **Galois extension** -- Splitting fields are exactly Galois extensions (char 0)

# Source Reference

Chapter 16: Galois Theory, Section 16.3, pages 489-490. Theorem 16.3.2.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.3.2
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
