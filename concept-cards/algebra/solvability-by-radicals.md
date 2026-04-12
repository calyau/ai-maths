---
concept: Solvability by Radicals
slug: solvability-by-radicals
category: galois-theory
subcategory: applications
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.12 Quintic Equations"
extraction_confidence: high
aliases:
  - "solvable by radicals"
  - "radical extension"
prerequisites:
  - galois-group
  - galois-extension
  - solvable-group
  - kummer-extension
extends: []
related:
  - insolvability-of-quintic
  - abel-ruffini-theorem
contrasts_with: []
answers_questions:
  - "How do I determine if an equation is solvable by radicals?"
  - "What is solvability by radicals?"
---

# Quick Definition

A complex number alpha is solvable over a field F if it can be reached from F by a sequence of root extractions (nth roots). Equivalently, there is a chain of fields ending at alpha where each step is a Galois extension of prime degree.

# Core Definition

A complex number alpha is called solvable over F if either of these equivalent conditions holds (Artin, Proposition 16.12.2): (a) There is a chain F = F_0 in F_1 in ... in F_r = K with alpha in K, where each F_j = F_{j-1}(beta_j) with a power of beta_j in F_{j-1}; (b) There is a chain where each F_{j+1} is a Galois extension of F_j of prime degree.

# Prerequisites

- **Galois group** -- Solvability depends on the Galois group
- **Galois extension** -- The chain consists of Galois extensions
- **Solvable group** -- The connection to group theory
- **Kummer extension** -- Galois extensions of prime degree by root extraction

# Key Properties

1. Conditions (a) and (b) are equivalent (Proposition 16.12.2)
2. Roots of polynomials of degree at most 4 are always solvable (16.12.3)
3. The Galois group of a solvable polynomial is a solvable group
4. If the Galois group is A_5 or S_5, the roots are NOT solvable (Theorem 16.12.4)
5. Solvability by radicals is fundamentally about the structure of the Galois group

# Construction / Recognition

## To Determine Solvability:
1. Find the splitting field K of the polynomial over F
2. Compute the Galois group G(K/F)
3. Check if G is a solvable group (has a composition series with abelian factors)
4. If G is solvable, the roots are solvable by radicals; if not, they are not

# Context & Application

This is the culmination of Galois theory: connecting the algebraic solvability of polynomial equations to the group-theoretic property of solvability. The quadratic formula, Cardano's formula for cubics, and the solution of quartics all fit into this framework.

# Examples

**Example 1** (p. 510): Cardano's formula expresses roots of x^3 + 3px + 2q as cube_root(-q + sqrt(q^2 + p^3)) + cube_root(-q - sqrt(q^2 + p^3)) (equation 16.11.5).

**Example 2** (p. 514): The polynomial x^5 - 16x + 2 is irreducible over Q with exactly three real roots. Its Galois group is S_5 (by Corollary 16.12.6), so its roots are not solvable over Q.

# Relationships

## Builds Upon
- **Galois group** -- Solvability determined by the Galois group
- **Solvable group** -- The group-theoretic criterion
- **Kummer extension** -- Each step in the radical tower

## Enables
- **Insolvability of the quintic** -- A_5 and S_5 are not solvable groups

## Related
- **Abel-Ruffini theorem** -- The general quintic is not solvable by radicals

# Source Reference

Chapter 16: Galois Theory, Section 16.12, pages 510-518. Proposition 16.12.2, Theorem 16.12.4, Corollary 16.12.6.

# Verification Notes

- Definition source: Direct from Artin, Proposition 16.12.2
- Confidence rationale: Two equivalent characterizations with complete proof
- Uncertainties: None
- Cross-reference status: Verified
