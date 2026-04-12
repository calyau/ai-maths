---
concept: "Cardano's Formula"
slug: cardanos-formula
category: galois-theory
subcategory: applications
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.11 Kummer Extensions"
extraction_confidence: high
aliases:
  - "Cardano-Tartaglia formula"
  - "cubic formula"
prerequisites:
  - kummer-extension
  - discriminant
extends: []
related:
  - solvability-by-radicals
  - galois-theory-cubic
contrasts_with: []
answers_questions:
  - "How do I solve a cubic equation?"
---

# Quick Definition

Cardano's formula expresses the roots of a cubic x^3 + 3px + 2q in terms of nested radicals: u_1 = cube_root(-q + sqrt(q^2 + p^3)) + cube_root(-q - sqrt(q^2 + p^3)).

# Core Definition

For the cubic f(x) = x^3 + 3px + 2q (with zero quadratic term, achieved by Tschirnhausen transformation), the roots are given by (Artin, equation 16.11.5): u_1 = cube_root(-q + sqrt(q^2 + p^3)) + cube_root(-q - sqrt(q^2 + p^3)). This is derived from Kummer theory: the Galois group A_3 acts on the vector z = u_1 + omega*u_2 + omega^2*u_3 as an eigenvector, and z^3 can be expressed in terms of the coefficients.

# Prerequisites

- **Kummer extension** -- The theoretical framework
- **Discriminant** -- D = -2^2 * 3^3 * (q^2 + p^3)

# Key Properties

1. The formula involves square roots and cube roots (two levels of radicals)
2. The formula is ambiguous: there are 6 ways to read each cube root term
3. The discriminant is D = -4 * (3p)^3 - 27 * (2q)^2 = -108(q^2 + p^3)
4. When D > 0 (three real roots), the formula involves cube roots of complex numbers (casus irreducibilis)
5. The derivation uses eigenvectors of the cyclic permutation (123)

# Context & Application

Cardano's formula (discovered by Tartaglia, published by Cardano in 1545) is the first instance of solving equations by radicals beyond the quadratic formula. It demonstrates that Galois theory provides a systematic framework for what was historically discovered by ad hoc methods.

# Examples

**Example 1** (p. 512): For f(x) = x^3 + 3x + 2 (p = 1, q = 1): x = cube_root(-1 + sqrt(2)) + cube_root(-1 - sqrt(2)).

# Relationships

## Builds Upon
- **Kummer extension** -- The formula comes from Kummer theory

## Related
- **Solvability by radicals** -- Cardano's formula is a radical solution
- **Galois theory for cubics** -- The Galois group determines solvability

# Common Confusions

- **Confusion**: Thinking Cardano's formula always gives a useful numerical answer
  **Clarification**: When all three roots are real, the formula involves cube roots of complex numbers, making it practically useless (casus irreducibilis).

# Source Reference

Chapter 16: Galois Theory, Section 16.11, pages 511-512. Equation 16.11.5.

# Verification Notes

- Definition source: Direct from Artin, equation 16.11.5
- Confidence rationale: Complete derivation given
- Uncertainties: None
- Cross-reference status: Verified
