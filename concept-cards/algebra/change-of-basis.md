---
concept: Change of Basis
slug: change-of-basis
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
  - "basechange matrix"
  - "change of coordinates"
prerequisites:
  - basis
  - invertible-matrix
extends: []
related:
  - coordinates
  - similar-matrices
contrasts_with: []
answers_questions:
  - "What is a basis and what is dimension?"
---

# Quick Definition

The change of basis (basechange) matrix P relates two bases B and B' of a vector space: B' = BP. The coordinate vectors transform as X = PX', where X and X' are coordinates with respect to B and B', respectively.

# Core Definition

Given bases B and B' of V, the basechange matrix P is the unique invertible matrix such that B' = BP (Artin, p. 104, formula 3.5.8). The jth column of P is the coordinate vector of the new basis vector v'_j with respect to the old basis B. Coordinate vectors transform as PX' = X, where X is the coordinate of a vector in basis B and X' in basis B' (formula 3.5.10).

# Prerequisites

- **Basis** — Two bases being related
- **Invertible matrix** — P is always invertible

# Key Properties

1. B' = BP and PX' = X
2. P is invertible (Proposition 3.5.9)
3. Any invertible P gives a valid new basis B' = BP
4. For the standard basis E: [B] (the matrix of coordinate vectors) is the basechange matrix from E to B

# Construction / Recognition

## To Construct:
1. Express each new basis vector as a combination of the old basis
2. The coefficients form the columns of P

## To Recognize:
1. An invertible matrix relating two bases: B' = BP

# Context & Application

Change of basis is essential for relating different coordinate representations. For linear operators, it leads to similarity: A' = P^(-1)AP. The choice of a good basis can dramatically simplify a problem.

# Examples

**Example 1** (p. 105): For the solution space of 2x_1 - x_2 - 2x_3 = 0 with bases B = {(1,0,1)^t, (1,2,0)^t} and B' = {(0,2,-1)^t, (1,4,-1)^t}, the basechange matrix is P = [[-1,-1],[1,2]].

**Example 2** (p. 106): (e^{it}, e^{-it}) = (cos t, sin t) * [[1,1],[i,-i]], relating exponential and trigonometric bases.

# Relationships

## Builds Upon
- **Basis** — Relates two bases

## Enables
- **Similar matrices** — A' = P^(-1)AP

## Related
- **Coordinates** — How coordinate vectors change under basis change

# Common Errors

- **Error**: Confusing B' = BP with X' = PX
  **Correction**: B' = BP (bases) but PX' = X (coordinates go the OTHER way)

# Common Confusions

- **Confusion**: Thinking P acts on vectors (not coordinates)
  **Clarification**: P relates coordinate vectors; the actual vectors in V don't change

# Source Reference

Chapter 3: Vector Spaces, Section 3.5, pages 104-107.

# Verification Notes

- Definition source: Direct from (3.5.8) and (3.5.10)
- Confidence rationale: Explicitly defined with dual properties
- Uncertainties: None
- Cross-reference status: Verified
