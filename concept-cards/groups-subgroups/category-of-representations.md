---
concept: Category of Representations
slug: category-of-representations
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 104
section: "8g The category of representations of G"
extraction_confidence: high
aliases:
  - Rep(G)
  - "Rep_k(G)"
prerequisites:
  - linear-representation
  - comodule
  - representation-comodule-correspondence
extends: []
related:
  - contragredient-representation
  - reconstruction-theorem
contrasts_with: []
answers_questions:
  - "What structure does the category Rep(G) have?"
  - "How are tensor products and duals of representations defined?"
---

# Quick Definition

Rep(G) is the category of finite-dimensional representations of G on k-vector spaces. It is an abelian category with a tensor product structure and, when G is a group, duals (contragredients). The forgetful functor to vector spaces is exact and faithful.

# Core Definition

Let G be an affine monoid over k. The category Rep(G) of representations of G on finite-dimensional k-vector spaces is essentially the same as the category of finite-dimensional O(G)-comodules. It is an abelian category and the forgetful functor omega: Rep(G) -> Vec_k is exact and faithful. The *tensor product* of (V,r) and (V',r') is (V tensor V', r tensor r') where (r tensor r')_R(g) = r_R(g) tensor r'_R(g). When G is a group, the *contragredient* of (V,r) is (V^dual, r^dual) where r^dual_R(g)(f)(v) = f(r_R(g^{-1})v) (Milne, pp. 104-105).

# Prerequisites

- **Linear representation** -- The objects of Rep(G)
- **Comodule** -- Rep(G) is equivalent to Comod(O(G))
- **Representation-comodule correspondence** -- The equivalence between the two categories

# Key Properties

1. Rep(G) is an abelian category
2. The forgetful functor omega to Vec_k is exact, faithful, and preserves tensor products and duals
3. Tensor products correspond to tensor products of comodules (as defined in 8e)
4. The trivial representation k (with trivial G-action) is the unit for tensor products
5. Replete subcategories closed under tensor products and contragredients correspond bijectively to quotient groups of G (Theorem 8.63)

# Construction / Recognition

## To Construct:
1. Objects: finite-dimensional k-vector spaces V with a representation r: G -> GL_V
2. Morphisms: G-equivariant k-linear maps
3. Tensor product: (V tensor W, r tensor r')
4. Duals: (V^dual, r^dual)

## To Recognize:
1. An abelian category with tensor product, duals, and a faithful exact functor to Vec_k satisfying the Tannakian conditions

# Context & Application

The category Rep(G) encodes the complete structure of G: by the reconstruction theorem (10.2), G can be recovered as Aut^tensor(omega) where omega is the forgetful functor. This is the algebraic analogue of Tannaka duality.

# Examples

**Example 1** (p. 104): For G = G_m, Rep(G) is equivalent to the category of Z-graded finite-dimensional vector spaces: V = direct-sum V_n where G_m acts on V_n by t -> t^n.

# Relationships

## Builds Upon
- **Linear representation** -- Rep(G) consists of representations

## Enables
- **Reconstruction theorem** -- G is recovered from Rep(G)
- **Characterization of representation categories** -- Abstract characterization via Tannakian categories

## Related
- **Contragredient representation** -- Dual objects in Rep(G)

# Common Confusions

- **Confusion**: Thinking Rep(G) determines G only up to isomorphism of abstract groups
  **Clarification**: Rep(G) together with the fiber functor omega determines G as an algebraic group (including its scheme structure)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8g and 8o, pages 104-105, 115-116. Summary 8.11, Theorem 8.63.

# Verification Notes

- Definition source: Direct from Section 8g
- Confidence rationale: Explicit construction with detailed analysis
- Uncertainties: None
- Cross-reference status: Verified
