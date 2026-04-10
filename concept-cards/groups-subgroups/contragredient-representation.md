---
concept: Contragredient Representation
slug: contragredient-representation
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 99
section: "8e The category of comodules"
extraction_confidence: high
aliases:
  - dual representation
prerequisites:
  - linear-representation
  - hopf-algebra
extends:
  - linear-representation
related:
  - category-of-representations
contrasts_with: []
answers_questions:
  - "What is the dual of a representation?"
---

# Quick Definition

The contragredient (or dual) of a representation (V, r) of a group G is the representation (V^dual, r^dual) on the dual vector space, where g acts on a linear functional f by (r^dual(g)(f))(v) = f(r(g^{-1})v).

# Core Definition

When G is an affine group, the *contragredient* or *dual* of a finite-dimensional representation (V, r) is (V^dual, r^dual) where r^dual_R(g)(f)(v) = f(r_R(g^{-1})v) for g in G(R), f in V^dual(R), v in V(R). At the comodule level, the right coaction rho^dual on V^dual is obtained from the left coaction rho' on V^dual (via the canonical isomorphism) by composing with the transposition and the antipode S: rho^dual = (V^dual tensor S) . t . rho' (Milne, pp. 99-100, 104-105).

# Prerequisites

- **Linear representation** -- The contragredient is defined for representations
- **Hopf algebra** -- The antipode S is needed to convert left coaction to right coaction

# Key Properties

1. (V^dual)^dual is canonically isomorphic to V
2. The contragredient of a tensor product is the tensor product of contragredients
3. A_{V^dual} = S(A_V) where A_V is the smallest subcoalgebra through which the coaction factors (Lemma 8.40)
4. The forgetful functor preserves duals

# Context & Application

Contragredients are essential for the tensor structure of Rep(G). Together with tensor products, they make Rep(G) into a rigid tensor category, which is the algebraic incarnation of Tannaka duality.

# Examples

**Example 1** (p. 105): For the standard representation of GL_n on k^n, the contragredient is the action on (k^n)^dual given by g.f = f . g^{-1}, i.e., the action by the inverse transpose.

# Relationships

## Builds Upon
- **Linear representation** -- Defined as the dual of a representation

## Enables
- **Category of representations** -- Provides the duality structure in Rep(G)
- **Faithful representation** -- Theorem 8.44 uses V direct-sum V^dual

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 8e and 8g, pages 99-100, 104-105.

# Verification Notes

- Definition source: Direct from pp. 99-100 and 104-105
- Confidence rationale: Explicit definition at both representation and comodule levels
- Uncertainties: None
- Cross-reference status: Verified
