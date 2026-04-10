---
concept: Fibre Functor
slug: fibre-functor
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
aliases: []
prerequisites:
  - tensor-category
  - rigid-tensor-category
extends: []
related:
  - neutral-tannakian-category
  - tannaka-dual
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
  - "What must I know before understanding tannakian duality?"
---

# Quick Definition

A fibre functor on a tannakian category C is an exact tensor functor omega: C -> Vec_k to the category of finite-dimensional vector spaces. The Tannaka dual group is recovered as the group of tensor automorphisms of omega.

# Core Definition

A **fibre functor** over k for an abelian k-linear category C with rigid tensor structure is an exact tensor functor omega: C -> Vec_k (Milne, 21.9). A pair (C, omega) is called a **neutral tannakian category**.

# Prerequisites

- **Tensor category** -- A fibre functor is a tensor functor
- **Rigid tensor category** -- The source category must be rigid

# Key Properties

1. The fibre functor "forgets" the algebraic structure, retaining only the linear algebra
2. Different fibre functors on the same category give inner-isomorphic Tannaka duals
3. For C = Rep(G), the forgetful functor V -> V is a fibre functor

# Context & Application

The fibre functor is the key ingredient that makes Tannaka reconstruction possible. Without it, one has only an abstract tensor category; with it, one can recover a group. The existence of a fibre functor over k is what makes the tannakian category "neutral."

# Examples

**Example 1** (21.15): For C = Rep(G), the forgetful functor omega(V) = V (forgetting the G-action) is a fibre functor.

# Relationships

## Enables
- **Neutral tannakian category** -- A tannakian category with a fibre functor
- **Tannaka dual** -- G = Aut^tensor(omega)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21b, page 234.

# Verification Notes

- Definition source: Direct from 21.9
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
