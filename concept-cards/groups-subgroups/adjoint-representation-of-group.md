---
concept: Adjoint Representation of an Algebraic Group
slug: adjoint-representation-of-group
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 247
section: "1g The adjoint map Ad"
extraction_confidence: high
aliases:
  - "Ad"
  - "ad"
  - "adjoint map"
prerequisites:
  - lie-algebra-of-algebraic-group
extends: []
related:
  - adjoint-representation-of-lie-algebra
  - lie-bracket
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

The adjoint representation Ad: G -> Aut(g) sends g in G(R) to the automorphism Ad(g)(x) = i(g) . x . i(g)^{-1} of g(R), where x is in g(R) = Ker(G(R[epsilon]) -> G(R)). Applying Lie to Ad gives ad: g -> End(g) with [a,x] = ad(a)(x).

# Core Definition

For an algebraic group G over k with Lie algebra g, the **adjoint representation** is the homomorphism Ad: G(R) -> Aut_{R-lin}(g(R)) defined by Ad(g)x = i(g) . x . i(g)^{-1} for g in G(R), x in g(R) contained in G(R[epsilon]) (Milne, Section 1g). Applying the functor Lie gives ad: g -> End_{k-lin}(g), and the bracket is defined by [a,x] = ad(a)(x) (Definition 1.30).

# Prerequisites

- **Lie algebra of algebraic group** -- Ad acts on Lie(G)

# Key Properties

1. For GL_n: Ad(A)(X) = AXA^{-1} and ad(A)(X) = AX - XA (Lemma 1.31)
2. Ad preserves the Lie bracket: Ad(g) is a Lie algebra automorphism (Lemma 5.27)
3. Ker(Ad) = Z(G) for connected G (Proposition 5.29)
4. For semisimple G: G -> Aut(g)^0 is surjective with kernel Z(G) (Theorem 5.30)
5. The construction is functorial: Lie(f)(Ad_G(g).x) = Ad_H(f(g)).x (equation 136)

# Context & Application

The adjoint representation connects the group to its Lie algebra in a canonical way. It defines the Lie bracket via ad, and the exactness of 1 -> Z(G) -> G -> Aut(g)^0 -> 1 for semisimple groups (Theorem 5.30) is the key structural result connecting algebraic groups to Lie algebras.

# Examples

**Example 1** (p. 248): For GL_n, Ad(g)X = gXg^{-1} for g in GL_n(R) and X in M_n(R). Then ad(A)X = AX - XA.

# Relationships

## Builds Upon
- **Lie algebra of algebraic group** -- Ad acts on Lie(G)

## Enables
- **Lie bracket** -- The bracket [a,x] = ad(a)(x) is defined via ad

## Related
- **Adjoint representation of Lie algebra** -- ad is the Lie algebra level version

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Sections 1g-1h, pages 247-250.

# Verification Notes

- Definition source: Direct from Sections 1g-1h
- Confidence rationale: Explicit construction
- Uncertainties: None
- Cross-reference status: Verified
