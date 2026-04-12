---
concept: "Galois Theory for Cubics"
slug: galois-theory-cubic
category: galois-theory
subcategory: applications
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.8 Cubic Equations"
extraction_confidence: high
aliases:
  - "cubic Galois group"
prerequisites:
  - galois-group
  - discriminant
  - splitting-field
extends: []
related:
  - resolvent-cubic
  - galois-theory-quartic
contrasts_with: []
answers_questions:
  - "How do I determine the Galois group of a cubic polynomial?"
---

# Quick Definition

The Galois group of an irreducible cubic over F is either A_3 (cyclic of order 3) or S_3 (symmetric group of order 6), determined entirely by whether the discriminant is a square in F.

# Core Definition

Let f(x) be an irreducible cubic polynomial over F with splitting field K and discriminant D (Artin, Theorem 16.8.5): If D is a square in F, then [K:F] = 3 and G = A_3. If D is not a square in F, then [K:F] = 6 and G = S_3. The proof uses the square root delta = product(alpha_i - alpha_j): a permutation multiplies delta by the sign of the permutation, so G in A_3 iff delta is in F iff D is a square.

# Prerequisites

- **Galois group** -- The Galois group being determined
- **Discriminant** -- The key invariant
- **Splitting field** -- Where the roots live

# Key Properties

1. G is a transitive subgroup of S_3; the only options are A_3 and S_3
2. D is a square iff delta is in F iff G consists of even permutations iff G = A_3
3. When G = A_3, there are no proper intermediate fields
4. When G = S_3, there are four proper intermediate fields: F(alpha_1), F(alpha_2), F(alpha_3), F(delta)

# Context & Application

The cubic case is the simplest nontrivial application of Galois theory and serves as a model for analyzing higher-degree polynomials. The discriminant criterion is clean and computable.

# Examples

**Example 1** (p. 499): f(x) = x^3 + 3x + 1 has discriminant -5*3^3 = -135 (not a square), so G = S_3.

**Example 2** (p. 499): f(x) = x^3 - 3x + 1 has discriminant 3^4 = 81 = 9^2 (a square), so G = A_3.

# Relationships

## Builds Upon
- **Discriminant** -- Determines the Galois group for cubics
- **Galois group** -- Being determined

## Related
- **Resolvent cubic** -- The analogous tool for quartics

# Source Reference

Chapter 16: Galois Theory, Section 16.8, pages 499-501. Theorem 16.8.5.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.8.5
- Confidence rationale: Complete classification with examples
- Uncertainties: None
- Cross-reference status: Verified
