---
concept: Galois Theory for Quartics
slug: quartic-equation-galois
category: galois-theory
subcategory: applications
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.9 Quartic Equations"
extraction_confidence: high
aliases:
  - "quartic Galois group"
prerequisites:
  - galois-group
  - discriminant
  - resolvent-cubic
extends: []
related:
  - galois-theory-cubic
contrasts_with: []
answers_questions:
  - "How do I determine the Galois group of a quartic polynomial?"
---

# Quick Definition

The Galois group of an irreducible quartic is one of S_4, A_4, D_4, C_4, or D_2 (Klein four group). It is determined by the discriminant and the resolvent cubic: D square + g reducible -> D_2; D square + g irreducible -> A_4; D not square + g reducible -> D_4 or C_4; D not square + g irreducible -> S_4.

# Core Definition

The transitive subgroups of S_4 are S_4, A_4, D_4, C_4, D_2 (Artin, equation 16.9.1). The Galois group of an irreducible quartic is one of these. The discriminant D determines whether G is in A_4 (D a square) or not. The resolvent cubic g(x) further distinguishes: g splits completely implies G = D_2; g has one root implies G = D_4 or C_4; g irreducible implies G = S_4 or A_4 (Proposition 16.9.8, Table 16.9.9).

# Prerequisites

- **Galois group** -- The Galois group being classified
- **Discriminant** -- Determines whether G contains odd permutations
- **Resolvent cubic** -- Further constrains the group

# Key Properties

1. Five possible Galois groups: S_4, A_4, D_4, C_4, D_2 (16.9.1)
2. Table 16.9.9 determines G from D and g except for the D_4/C_4 ambiguity
3. D_2 (Klein four group) = {id, (12)(34), (13)(24), (14)(23)} is normal in S_4
4. The resolvent cubic has the same discriminant as f

# Context & Application

The quartic case is the most complex case fully analyzed in Artin. It demonstrates the interplay between symmetric functions (resolvent cubic), the discriminant, and group theory in determining Galois groups.

# Examples

**Example 1** (p. 502): f(x) = x^4 - 8x^2 + 11 (nested square root sqrt(4 + sqrt(5))). Galois group is D_4.

**Example 2** (p. 504): f(x) = x^4 - 4x^2 + 2. Galois group is C_4.

**Example 3** (p. 504): f(x) = x^4 - 8x^2 + 9. Galois group is D_2.

# Relationships

## Builds Upon
- **Discriminant** -- First invariant for classification
- **Resolvent cubic** -- Second invariant for classification

## Related
- **Galois theory for cubics** -- Simpler analog

# Source Reference

Chapter 16: Galois Theory, Section 16.9, pages 502-507. Table 16.9.9.

# Verification Notes

- Definition source: Direct from Artin, Table 16.9.9
- Confidence rationale: Complete classification with examples
- Uncertainties: D_4/C_4 ambiguity not fully resolved by these tools
- Cross-reference status: Verified
