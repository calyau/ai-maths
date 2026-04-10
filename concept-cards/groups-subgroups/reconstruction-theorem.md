---
concept: Reconstruction Theorem
slug: reconstruction-theorem
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 128
section: "10a Recovering a group from its representations"
extraction_confidence: high
aliases:
  - Tannaka reconstruction
  - "Tannaka-Krein duality for algebraic groups"
prerequisites:
  - category-of-representations
  - faithful-representation
extends: []
related:
  - jordan-decomposition
  - characterization-of-representation-categories
contrasts_with: []
answers_questions:
  - "How can an algebraic group be recovered from its representations?"
---

# Quick Definition

The reconstruction theorem (Theorem 10.2) states that an affine group G can be recovered from its category of representations: G(R) is isomorphic to the group of tensor-compatible natural transformations of the forgetful functor omega_R on Rep(G). In short, G = Aut^tensor(omega).

# Core Definition

*Theorem 10.2*: Let G be an affine monoid (or group) over k, and let R be a k-algebra. Suppose that for each finite-dimensional representation (V, r_V) of G, we are given an R-linear map lambda_V: V_R -> V_R. If the family (lambda_V) satisfies: (a) lambda_{V tensor W} = lambda_V tensor lambda_W, (b) lambda_{trivial} = id, and (c) lambda_W . alpha_R = alpha_R . lambda_V for all G-equivariant alpha, then there exists a unique g in G(R) such that lambda_V = r_V(g) for all V (Milne, Theorem 10.2, pp. 129-131).

# Prerequisites

- **Category of representations** -- The input data: Rep(G) with forgetful functor
- **Faithful representation** -- Ensures uniqueness of the recovered element

# Key Properties

1. G is recovered as End^tensor(omega) when G is a monoid, or Aut^tensor(omega) when G is a group
2. The theorem uses the regular representation as a universal object
3. The proof reduces to Lemma 10.1: any algebra endomorphism of O(G) compatible with comultiplication is right translation by a unique g
4. When G is a group, each lambda_V is automatically an isomorphism

# Context & Application

This is the algebraic analogue of Tannaka duality for compact groups. It shows that the abstract category-theoretic data of Rep(G) (with the fiber functor) determines G completely. This is the foundation for the Tannakian formalism.

# Examples

**Example 1** (p. 131): For G = G_m, the representations are Z-graded vector spaces. The reconstruction gives G_m(R) = R^x as the automorphisms of the grading functor.

# Relationships

## Builds Upon
- **Category of representations** -- The input data

## Enables
- **Jordan decomposition** -- Uses the reconstruction theorem to define g_s and g_u
- **Characterization of representation categories** -- The description theorem (Section 11)

# Common Confusions

- **Confusion**: Thinking G is determined by Rep(G) alone (without the fiber functor)
  **Clarification**: Two non-isomorphic groups can have equivalent tensor categories; the fiber functor omega is essential

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 10a, pages 128-131. Theorem 10.2, Lemma 10.1.

# Verification Notes

- Definition source: Direct from Theorem 10.2
- Confidence rationale: Central theorem with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
