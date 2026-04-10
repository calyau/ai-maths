---
concept: Cartier Duality
slug: cartier-duality
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 149
section: "12d Cartier duality"
extraction_confidence: high
aliases:
  - Cartier dual
prerequisites:
  - finite-flat-affine-group
  - hopf-algebra
extends: []
related:
  - group-of-multiplicative-type
contrasts_with: []
answers_questions:
  - "What is the Cartier dual of a finite flat group scheme?"
---

# Quick Definition

The Cartier dual of a finite flat commutative affine group G is the affine group G^dual with bialgebra O(G)^dual (linear dual with interchanged multiplication/comultiplication). Functorially, G^dual(R) = Hom(G_R, G_{m,R}). The functor G -> G^dual is an involution on finite flat commutative groups.

# Core Definition

Let G be a finite flat commutative affine group with bialgebra (O(G), m, e, Delta, epsilon). The *Cartier dual* G^dual is the affine group with bialgebra (O(G)^dual, Delta^dual, epsilon^dual, m^dual, e^dual) -- the linear dual with multiplication and comultiplication interchanged. Theorem 12.16 states: G^dual is canonically isomorphic to Hom(G, G_m), i.e., G^dual(R) = Hom(G_R, G_{m,R}) as group-valued functors. The Cartier duality functor is a contravariant equivalence with (G^dual)^dual = G (Milne, pp. 149-151).

# Prerequisites

- **Finite flat affine group** -- Cartier duality applies to finite flat commutative groups
- **Hopf algebra** -- The dual is defined by dualizing the Hopf algebra

# Key Properties

1. G^dual(R) = Hom(G_R, G_{m,R}) (Theorem 12.16)
2. (G^dual)^dual = G canonically
3. The order of G^dual equals the order of G
4. Contravariant equivalence of the category of finite flat commutative groups with itself
5. alpha_p is self-dual: alpha_p^dual = alpha_p (Example 12.17)

# Context & Application

Cartier duality is the analogue of Pontryagin duality for finite flat group schemes. It plays an important role in the theory of abelian varieties and p-divisible groups.

# Examples

**Example 1** (p. 151): (Z/nZ)^dual = mu_n and mu_n^dual = Z/nZ.

**Example 2** (p. 151): alpha_p^dual = alpha_p (self-dual). The pairing is (a,b) -> exp(ab) with truncated exponential.

# Relationships

## Builds Upon
- **Finite flat affine group** -- The source category

## Related
- **Group of multiplicative type** -- Cartier duality relates etale groups and multiplicative type groups

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 12d, pages 149-151. Theorem 12.16, Example 12.17.

# Verification Notes

- Definition source: Direct from Section 12d
- Confidence rationale: Explicit definition and classification
- Uncertainties: None
- Cross-reference status: Verified
