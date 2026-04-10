---
concept: Neutral Tannakian Category
slug: neutral-tannakian-category
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 234
section: "21b Neutral tannakian categories"
extraction_confidence: high
aliases:
  - "tannakian category"
prerequisites:
  - rigid-tensor-category
  - tensor-category
extends:
  - rigid-tensor-category
related:
  - tannaka-dual
  - fibre-functor
  - tannakian-correspondence
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
  - "What must I know before understanding tannakian duality?"
---

# Quick Definition

A neutral tannakian category over k is an abelian k-linear category with a rigid tensor structure admitting an exact tensor functor (fibre functor) to finite-dimensional vector spaces over k. The fundamental theorem says it is equivalent to the representation category of an affine group.

# Core Definition

A **neutral tannakian category** over k is an abelian k-linear category C endowed with a rigid tensor structure for which there exists an exact tensor functor omega: C -> Vec_k (called a **fibre functor**) (Milne, 21.9). The fundamental theorem (21.10) states that the functor R -> G(R), where G(R) consists of tensor-compatible natural transformations of omega_R, is an affine group, and omega induces an equivalence C -> Rep(G).

# Prerequisites

- **Rigid tensor category** -- A tannakian category must be rigid
- **Tensor category** -- A tannakian category is a special tensor category

# Key Properties

1. The affine group G = Aut^tensor(omega) is called the Tannaka dual (21.14)
2. The functor C -> Rep(G) is an equivalence of tensor categories
3. If C = Rep(H) and omega is the forgetful functor, then G = H (Example 21.15)
4. C is algebraic (21.13) iff G is an algebraic group iff C has a tensor generator
5. Normal subgroups of G correspond to tannakian subcategories of C (21.18b)

# Construction / Recognition

## To Construct:
1. Start with an abelian k-linear category C with a rigid tensor structure
2. Verify there exists an exact tensor functor omega: C -> Vec_k
3. The Tannaka dual G = Aut^tensor(omega) is then an affine group over k

## To Recognize:
1. Check abelian, k-linear, rigid tensor structure
2. Verify existence of a fibre functor

# Context & Application

Tannakian categories provide the abstract framework for recovering an algebraic group from its representations. This is the modern formulation of Tannaka duality: a group is determined (up to isomorphism) by its tensor category of representations together with a fibre functor. This perspective is crucial for motivic Galois groups and the Langlands program.

# Examples

**Example 1** (21.15): If C = Rep(H) for an algebraic group H with the forgetful functor omega, then the Tannaka dual is H itself.

**Example 2** (21.16): If N is a normal subgroup of G, the subcategory of Rep(G) on which N acts trivially has Tannaka dual G/N.

# Relationships

## Builds Upon
- **Rigid tensor category** -- Tannakian adds abelian structure and a fibre functor

## Enables
- **Tannaka dual** -- The affine group recovered from the category
- **Tannakian correspondence** -- Subcategories <-> normal subgroups

# Common Confusions

- **Confusion**: Believing the Tannaka dual depends only on the category, not the fibre functor
  **Clarification**: Different fibre functors can give different (but inner-isomorphic) groups

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21b, pages 234-236.

# Verification Notes

- Definition source: Direct from 21.9 and 21.10
- Confidence rationale: Explicit definition with main theorem
- Uncertainties: None
- Cross-reference status: Verified
