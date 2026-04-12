---
concept: First Isomorphism Theorem (Rings)
slug: first-isomorphism-theorem-rings
category: ring-theory
subcategory: quotient-constructions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Quotient Rings"
extraction_confidence: high
aliases:
  - "first isomorphism theorem for rings"
prerequisites:
  - quotient-ring
  - ring-homomorphism
  - kernel-of-ring-homomorphism
extends: []
related:
  - correspondence-theorem-rings
contrasts_with: []
answers_questions:
  - "How do ideals relate to quotient rings?"
---

# Quick Definition

If f: R -> R' is a surjective ring homomorphism with kernel K, then R/K is isomorphic to R'. This is the fundamental method for identifying quotient rings.

# Core Definition

(First Isomorphism Theorem) If f: R -> R' is a surjective ring homomorphism and I = ker f, then the induced map f-bar: R/I -> R' is an isomorphism (Artin, Theorem 11.4.2(b), p. 352).

More generally, if I is any ideal contained in K = ker f, there is a unique homomorphism f-bar: R/I -> R' such that f-bar composed with the canonical map equals f.

# Prerequisites

- **Quotient ring** -- The domain R/K
- **Ring homomorphism** -- The surjective map f
- **Kernel of ring homomorphism** -- K = ker f is an ideal

# Key Properties

1. Identifies R/ker(f) with the image of f
2. The most common method for proving two rings are isomorphic
3. Quotient rings are often "new" rings not isomorphic to anything familiar

# Examples

**Example 1** (p. 352): Z[x]/(x^2+1) ~ Z[i], since the substitution map Z[x] -> Z[i] sending x to i has kernel (x^2+1).

**Example 2** (p. 352): Z[i]/(i-2) ~ F_5, obtained by killing x^2+1 and x-2 in Z[x] in either order.

# Relationships

## Builds Upon
- **Quotient ring** -- The theorem concerns quotient rings
- **Ring homomorphism** -- Uses surjective homomorphisms

## Enables
- **Adjoining elements** -- R[alpha] = R[x]/(f) identification

# Source Reference

Chapter 11: Rings, Section 11.4, Theorem 11.4.2, page 352.

# Verification Notes

- Definition source: Direct from Theorem 11.4.2
- Confidence rationale: Explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
