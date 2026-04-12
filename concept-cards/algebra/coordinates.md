---
concept: Coordinates
slug: coordinates
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.5 Computing with Bases"
extraction_confidence: high
aliases:
  - "coordinate vector"
prerequisites:
  - basis
extends: []
related:
  - change-of-basis
  - standard-basis
contrasts_with: []
answers_questions:
  - "What is a basis and what is dimension?"
---

# Quick Definition

Given a basis B = (v_1, ..., v_n) of V, the coordinates of a vector v are the unique scalars x_1, ..., x_n such that v = v_1 x_1 + ... + v_n x_n. The column vector X = (x_1, ..., x_n)^t is the coordinate vector of v with respect to B.

# Core Definition

Given a basis B = (v_1, ..., v_n) of V, every vector v can be uniquely expressed as v = v_1 x_1 + ... + v_n x_n (Proposition 3.4.14). The scalars x_i are the coordinates of v, and X = (x_1, ..., x_n)^t is the coordinate vector (Artin, p. 103, formula 3.5.2). The map X -> BX defines an isomorphism F^n -> V.

# Prerequisites

- **Basis** — Coordinates are defined relative to a basis

# Key Properties

1. Coordinates are uniquely determined by the basis
2. The map v -> X (coordinates) is an isomorphism V -> F^n
3. Different bases give different coordinates for the same vector
4. Coordinates transform as PX' = X under change of basis B' = BP

# Construction / Recognition

## To Construct:
1. Express v as a linear combination of the basis vectors
2. The coefficients are the coordinates

## To Recognize:
1. A column vector representing an abstract vector in terms of a specific basis

# Context & Application

Coordinates translate abstract vector space problems into concrete matrix computations. Every computation in linear algebra ultimately reduces to coordinate calculations.

# Examples

**Example 1** (p. 103): For the standard basis E of F^n, the coordinate vector of v is just v itself.

**Example 2** (pp. 103-104): For the basis (cos t, sin t) of solutions of y'' = -y, the coordinates of a solution f(t) are (x_1, x_2) where f(t) = x_1 cos t + x_2 sin t.

# Relationships

## Builds Upon
- **Basis** — Coordinates depend on the choice of basis

## Enables
- **Change of basis** — Relates coordinates in different bases

## Related
- **Standard basis** — Gives the "default" coordinate system in F^n

# Common Errors

- **Error**: Forgetting that coordinates depend on the basis
  **Correction**: Always specify which basis is being used

# Common Confusions

- **Confusion**: Thinking the coordinate vector IS the vector
  **Clarification**: The coordinate vector represents the abstract vector in a particular basis

# Source Reference

Chapter 3: Vector Spaces, Section 3.5, pages 103-104.

# Verification Notes

- Definition source: Direct from (3.5.1)-(3.5.2), p. 103
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
