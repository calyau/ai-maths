---
concept: Connected Components of an Algebraic Group
slug: connected-component-group
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 152
section: "13 The connected components of an algebraic group"
extraction_confidence: high
aliases:
  - identity component
  - pi_0(G)
  - G^0
prerequisites:
  - affine-algebraic-group
  - etale-affine-group
extends: []
related:
  - connected-etale-exact-sequence
contrasts_with: []
answers_questions:
  - "What is the identity component of an algebraic group?"
  - "What is the group of connected components?"
---

# Quick Definition

For an algebraic group G, the identity component G^0 is the largest connected normal subgroup, and pi_0(G) = G/G^0 is the etale group of connected components. There is a canonical exact sequence 1 -> G^0 -> G -> pi_0(G) -> 1.

# Core Definition

Let G be an algebraic group over k with coordinate ring A = O(G). The largest etale k-subalgebra pi_0(A) of A inherits a Hopf algebra structure. The *group of connected components* pi_0(G) is the etale quotient group corresponding to pi_0(A), and the *identity component* G^0 is the kernel of G -> pi_0(G) (Definition 13.12). An algebraic group G is *connected* iff any of the equivalent conditions hold: pi_0(G) is trivial; spm(O(G)) is connected; spm(O(G)) is irreducible; O(G)/N is an integral domain (Proposition 13.13, Milne, pp. 156-157).

# Prerequisites

- **Affine algebraic group** -- G is an algebraic group
- **Etale affine group** -- pi_0(G) is always etale

# Key Properties

1. G^0 is connected, normal, and every homomorphism from a connected group to G factors through G^0 (Proposition 13.16)
2. G^0 is the unique connected normal subgroup with etale quotient (Proposition 13.17)
3. The functors G -> pi_0(G) and G -> G^0 commute with field extension (Proposition 13.18)
4. pi_0(G x G') = pi_0(G) x pi_0(G') (Proposition 13.19)
5. Connected algebraic groups are geometrically connected (Remark 13.20)
6. If 1 -> N -> G -> Q -> 1 is exact and N, Q connected, then G is connected (Proposition 13.21)

# Construction / Recognition

## To Construct pi_0(G):
1. Find the largest etale subalgebra pi_0(O(G)) of O(G)
2. This is a Hopf subalgebra; pi_0(G) = Spec(pi_0(O(G)))

## To Recognize connectedness:
1. Check that O(G) has no nontrivial idempotents
2. Or check that O(G)/nilradical is an integral domain

# Context & Application

The connected-etale decomposition is the first step in the structural analysis of any algebraic group. It separates the "continuous" part (G^0) from the "discrete" part (pi_0(G)). Over perfect fields and for finite groups, G = G^0 rtimes pi_0(G).

# Examples

**Example 1** (p. 159): GL_n, SL_n, G_a, T_n, U_n, D_n are all connected because their coordinate rings are integral domains.

**Example 2** (p. 159): The orthogonal group O(q) has pi_0 = {+/- 1} (via determinant) and identity component SO(q).

**Example 3** (p. 159): The group of monomial matrices has pi_0 = S_n and G^0 = D_n.

# Relationships

## Builds Upon
- **Etale affine group** -- pi_0(G) is etale

## Enables
- **Solvable algebraic group** -- Structural analysis begins with the connected component
- **Group of multiplicative type** -- Connected groups of multiplicative type are tori

## Related
- **Connected-etale exact sequence** -- 1 -> G^0 -> G -> pi_0(G) -> 1

# Common Confusions

- **Confusion**: Thinking G connected implies G(k) is connected (in the real topology)
  **Clarification**: GL_2 is connected as an algebraic group but GL_2(R) is not connected in the real topology (Example 13.29)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 13, pages 152-161. Definition 13.12, Propositions 13.13-13.21.

# Verification Notes

- Definition source: Direct from Definition 13.12
- Confidence rationale: Explicit definition with full characterization
- Uncertainties: None
- Cross-reference status: Verified
