---
concept: Resolvent Cubic
slug: resolvent-cubic
category: galois-theory
subcategory: quartic-equations
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.9 Quartic Equations"
extraction_confidence: high
aliases: []
prerequisites:
  - galois-group
  - discriminant
extends: []
related:
  - quartic-equation-galois
contrasts_with: []
answers_questions:
  - "What is the resolvent cubic?"
  - "How do I determine the Galois group of a quartic polynomial?"
---

# Quick Definition

The resolvent cubic of a quartic polynomial f with roots alpha_1, ..., alpha_4 is the cubic polynomial g(x) = (x - beta_1)(x - beta_2)(x - beta_3), where beta_1 = alpha_1*alpha_2 + alpha_3*alpha_4, etc. Its reducibility determines the Galois group of the quartic.

# Core Definition

Given a quartic f(x) = x^4 - a_1*x^3 + a_2*x^2 - a_3*x + a_4 with roots alpha_1, ..., alpha_4 in a splitting field K, define (Artin, p. 503, equation 16.9.7): beta_1 = alpha_1*alpha_2 + alpha_3*alpha_4, beta_2 = alpha_1*alpha_3 + alpha_2*alpha_4, beta_3 = alpha_1*alpha_4 + alpha_2*alpha_3. The resolvent cubic is g(x) = (x - beta_1)(x - beta_2)(x - beta_3). Its coefficients are symmetric functions of the alpha_i, hence elements of F.

# Prerequisites

- **Galois group** -- The resolvent cubic helps determine the Galois group
- **Discriminant** -- Used together with the resolvent cubic

# Key Properties

1. The coefficients of g are in F (they are symmetric functions of the roots of f)
2. The beta_i are distinct if the alpha_i are distinct
3. The discriminants of f and g are equal (p. 504)
4. g irreducible implies G = S_4 or A_4; g splits completely implies G = D_2 (Proposition 16.9.8)
5. Combined with the discriminant: the table (16.9.9) nearly determines G

# Context & Application

The resolvent cubic is the main computational tool for analyzing quartic Galois groups. Lagrange discovered these expressions, which exploit the structure of the symmetric group S_4.

# Examples

**Example 1** (p. 503-505): For x^4 - 2 over Q, the resolvent cubic helps distinguish whether G = D_4, C_4, or D_2 among the quartic Galois groups.

# Relationships

## Builds Upon
- **Galois group** -- The resolvent cubic constrains the group
- **Discriminant** -- Together they nearly determine the quartic Galois group

## Related
- **Quartic equation** -- The resolvent cubic is defined for quartics

# Source Reference

Chapter 16: Galois Theory, Section 16.9, pages 502-507. Equation 16.9.7, Proposition 16.9.8, Table 16.9.9.

# Verification Notes

- Definition source: Direct from Artin, equation 16.9.7
- Confidence rationale: Explicit formula and classification table
- Uncertainties: None
- Cross-reference status: Verified
