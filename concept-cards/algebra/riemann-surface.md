---
concept: Riemann Surface
slug: riemann-surface
category: ring-theory
subcategory: algebraic-geometry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Algebraic Geometry"
extraction_confidence: medium
aliases:
  - "plane algebraic curve"
prerequisites:
  - algebraic-variety
  - irreducible-polynomial
extends:
  - algebraic-variety
related: []
contrasts_with: []
answers_questions:
  - "What is a Riemann surface?"
---

# Quick Definition

The Riemann surface of an irreducible polynomial f(t, x) is the locus X = {(t, x) in C^2 | f(t, x) = 0}. When f has degree n in x, the projection X -> C is an n-sheeted branched covering.

# Core Definition

The locus X of zeros in C^2 of a polynomial f(t, x) is called the Riemann surface of f (Artin, p. 369). When f is irreducible and has positive degree n in x, X is an n-sheeted branched covering of the complex t-plane (Theorem 11.9.16, p. 370).

# Prerequisites

- **Algebraic variety** -- A Riemann surface is a one-dimensional variety
- **Irreducible polynomial** -- The defining polynomial should be irreducible

# Key Properties

1. Also called a plane algebraic curve (though it has real dimension 2)
2. The fibre over most points t_0 consists of exactly n points
3. Branch points are where the fibre has fewer than n points
4. Singular points (nodes, cusps) must be excluded for the covering space structure

# Examples

**Example 1** (p. 370): The Riemann surface of x^2 - t is a 2-sheeted covering of C, branched at t = 0.

**Example 2** (p. 370): x^2 = t^3 - t^2 has a node at the origin; x^2 = t^3 has a cusp.

# Relationships

## Builds Upon
- **Algebraic variety** -- A special one-dimensional variety in C^2

# Source Reference

Chapter 11: Rings, Section 11.9, pages 369-372, Theorem 11.9.16.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Medium -- definition synthesized from discussion, not a boxed definition
- Uncertainties: The full treatment of Riemann surfaces continues in Chapter 15
- Cross-reference status: Verified
