---
# === CORE IDENTIFICATION ===
concept: Quadric
slug: quadric

# === CLASSIFICATION ===
category: bilinear-forms
subcategory: conics-quadrics
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.7 Conics and Quadrics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "quadric surface"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conic
  - spectral-theorem-symmetric
extends:
  - conic
related:
  - quadratic-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quadric?"
  - "How are quadrics classified?"
---

# Quick Definition

A quadric is a locus in R^n (n >= 3) defined by a quadratic equation. In R^3, the nondegenerate quadrics are ellipsoids, one-sheeted hyperboloids, two-sheeted hyperboloids, elliptic paraboloids, and hyperbolic paraboloids.

# Core Definition

A quadric is a locus in R^n defined by f(x_1, ..., x_n) = X^t A X + BX + c = 0 where A is a symmetric matrix (Artin, (8.7.11)-(8.7.12), p. 262). Theorem 8.7.14 classifies nondegenerate quadrics in R^3 up to congruence into five types.

# Prerequisites

- **Conic** — Quadrics are the higher-dimensional analogue
- **Spectral theorem for symmetric operators** — Used for diagonalization

# Key Properties

1. In R^3, the five types are: ellipsoid, one-sheeted hyperboloid, two-sheeted hyperboloid, elliptic paraboloid, hyperbolic paraboloid
2. Classification uses: (1) orthogonal transformation to diagonalize A, (2) completing the square
3. The type depends on the signature of A and whether linear/constant terms remain
4. When f is a homogeneous quadratic form (B=0, c=0), the locus is a cone — a union of lines through the origin (8.7.15)

# Construction / Recognition

## To Classify:
1. Write in matrix form X^t A X + BX + c = 0
2. Diagonalize A using the spectral theorem
3. Complete the square
4. Match to standard forms in Theorem 8.7.14

# Context & Application

Quadrics appear in differential geometry, optics (quadric surfaces as mirrors), and general relativity (classification of spacetime curvature). The cone (degenerate quadric) is a limiting case between one-sheeted and two-sheeted hyperboloids.

# Examples

**Example 1** (p. 262): x_1^2 + x_2^2 + x_3^2 = 1 is an ellipsoid (all coefficients equal gives a sphere).

**Example 2** (p. 262): The locus a_{11}x_1^2 + a_{22}x_2^2 - x_3^2 = 0 (a_{ii} > 0) is a double cone through the origin.

# Relationships

## Builds Upon
- **Conic** — Quadrics generalize conics to higher dimension

## Related
- **Quadratic form** — The degree-2 part of the quadric equation

# Common Errors

- **Error**: Assuming all quadratic equations in R^3 give one of the five standard types
  **Correction**: Degenerate cases (cylinders, cones, planes, etc.) are possible

# Common Confusions

- **Confusion**: Confusing a one-sheeted hyperboloid with a two-sheeted one
  **Clarification**: One-sheeted has signature (2,1) in the quadratic part (connected surface); two-sheeted has signature (1,2) (disconnected)

# Source Reference

Chapter 8: Bilinear Forms, Section 8.7, pages 262-263. Theorem 8.7.14.

# Verification Notes

- Definition source: Direct from (8.7.11), (8.7.12), and Theorem 8.7.14
- Confidence rationale: Explicitly classified
- Uncertainties: None
- Cross-reference status: Verified
