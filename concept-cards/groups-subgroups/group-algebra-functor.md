---
concept: Group Algebra and D(M) Functor
slug: group-algebra-functor
category: multiplicative-groups
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 163
section: "14c The affine group D(M)"
extraction_confidence: high
aliases:
  - D(M)
  - group algebra k[M]
prerequisites:
  - hopf-algebra
  - group-like-element
extends: []
related:
  - diagonalizable-group
  - character-of-affine-group
contrasts_with: []
answers_questions:
  - "How does the group algebra k[M] define an affine group?"
---

# Quick Definition

For a commutative group M, the group algebra k[M] has basis M with multiplication extending that of M, and becomes a Hopf algebra via Delta(m) = m tensor m, epsilon(m) = 1, S(m) = m^{-1}. The affine group D(M) = Spec k[M] satisfies D(M)(R) = Hom(M, R^x).

# Core Definition

Let M be a commutative group (written multiplicatively). The *group algebra* k[M] is the k-vector space with basis M, equipped with the multiplication extending that of M. It becomes a Hopf algebra with Delta(m) = m tensor m, epsilon(m) = 1, S(m) = m^{-1} for m in M. The affine group D(M) has coordinate ring k[M] and satisfies D(M)(R) = Hom_{groups}(M, R^x). When M is finitely generated, D(M) is algebraic and isomorphic to a product of copies of G_m and various mu_n (Proposition 14.6, Milne, pp. 163-165).

# Prerequisites

- **Hopf algebra** -- k[M] is a Hopf algebra
- **Group-like element** -- The elements of M are group-like in k[M]

# Key Properties

1. k[M_1 x M_2] = k[M_1] tensor k[M_2] (Example 14.5)
2. k[Z] = k[X, X^{-1}] gives D(Z) = G_m (Example 14.4a)
3. k[Z/nZ] = k[x]/(x^n - 1) gives D(Z/nZ) = mu_n (Example 14.4b)
4. The group-like elements of k[M] are exactly the elements of M (Lemma 14.7)
5. X(D(M)) = M (characters correspond to basis elements)

# Context & Application

The D(M) construction is the universal way to produce diagonalizable groups. Every diagonalizable group arises this way, and the functor M -> D(M) is a contravariant equivalence.

# Examples

**Example 1** (p. 164): D(Z) = G_m with k[Z] = k[X, X^{-1}].

**Example 2** (p. 164): D(Z/nZ) = mu_n with k[Z/nZ] = k[x]/(x^n - 1).

**Example 3** (p. 165): D(Z^n) = G_m^n.

# Relationships

## Enables
- **Diagonalizable group** -- Every diagonalizable group is D(M) for some M

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14c, pages 163-165. Examples 14.4-14.5, Proposition 14.6.

# Verification Notes

- Definition source: Direct from Section 14c
- Confidence rationale: Explicit construction with examples
- Uncertainties: None
- Cross-reference status: Verified
