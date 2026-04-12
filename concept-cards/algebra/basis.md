---
concept: Basis
slug: basis
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.4 Bases and Dimension"
extraction_confidence: high
aliases: []
prerequisites:
  - vector-space
  - linear-independence
  - span
extends: []
related:
  - dimension
  - coordinates
  - change-of-basis
  - standard-basis
contrasts_with: []
answers_questions:
  - "What is a basis and what is dimension?"
  - "How do I find a basis for a vector space?"
---

# Quick Definition

A basis of a vector space V is an ordered set of vectors (v_1, ..., v_n) that is linearly independent and spans V. Every vector in V can be written uniquely as a linear combination of the basis vectors.

# Core Definition

A basis of a vector space V is a set B = (v_1, ..., v_n) of vectors that is independent and spans V (Definition 3.4.13, Artin, p. 100). Equivalently, B is a basis iff every vector w in V can be written in a unique way as w = v_1 x_1 + ... + v_n x_n (Proposition 3.4.14). Any two bases of V have the same number of elements (Proposition 3.4.21).

# Prerequisites

- **Vector space** — A basis is a property of a vector space
- **Linear independence** — A basis must be independent
- **Span** — A basis must span V

# Key Properties

1. Every vector has a unique expression as a linear combination of basis vectors
2. Any two bases of V have the same number of elements
3. A spanning set can be reduced to a basis (by removing dependent vectors)
4. An independent set can be extended to a basis (by adding vectors from a spanning set)
5. The standard basis of F^n is E = (e_1, ..., e_n)

# Construction / Recognition

## To Construct:
1. Start with a spanning set and remove dependent vectors
2. Or start with an independent set and extend by adding vectors not in the span

## To Recognize:
1. The set spans V AND is linearly independent
2. Equivalently: every vector has a unique expression in terms of the set

# Context & Application

Bases provide the means to do computation in abstract vector spaces by reducing everything to coordinates. The choice of basis determines an isomorphism V -> F^n, turning abstract problems into matrix problems.

# Examples

**Example 1** (p. 100): The standard basis E = (e_1, ..., e_n) of F^n.

**Example 2** (p. 100): {(1,0,1)^t, (1,2,0)^t} is a basis for the solution space of 2x_1 - x_2 - 2x_3 = 0.

**Example 3** (p. 103): (cos t, sin t) is a basis for the solutions of y'' = -y.

# Relationships

## Builds Upon
- **Linear independence** — A basis is independent
- **Span** — A basis spans V

## Enables
- **Dimension** — The number of elements in a basis
- **Coordinates** — Coefficients in the basis expansion
- **Change of basis** — Relating different bases via an invertible matrix

# Common Errors

- **Error**: Assuming a basis is unique
  **Correction**: A vector space has many bases; any invertible change produces a new one

# Common Confusions

- **Confusion**: Confusing "spanning set" with "basis"
  **Clarification**: A spanning set may be dependent; a basis is spanning AND independent

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, pages 100-104.

# Verification Notes

- Definition source: Direct from Definition 3.4.13, p. 100
- Confidence rationale: Central definition with extensive discussion
- Uncertainties: None
- Cross-reference status: Verified
