---
concept: Rigid Tensor Category
slug: rigid-tensor-category
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 234
section: "21a Tensor categories"
extraction_confidence: high
aliases: []
prerequisites:
  - tensor-category
extends:
  - tensor-category
related:
  - neutral-tannakian-category
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
  - "What must I know before understanding tannakian duality?"
---

# Quick Definition

A rigid tensor category is a tensor category in which every object has a dual. The dual of V is a pair (V^v, ev: V^v tensor V -> 1) satisfying the standard adjunction conditions.

# Core Definition

A tensor category is **rigid** if every object V admits a dual (V^v, ev: V^v tensor V -> 1), where there exists a morphism delta_V: 1 -> V tensor V^v such that the standard compositions are identity morphisms (Milne, 21.7, 21.8). The dual is unique up to a unique isomorphism.

# Prerequisites

- **Tensor category** -- Rigidity is an additional property of tensor categories

# Key Properties

1. Vec_k (finite-dimensional vector spaces) is rigid, with V^v = Hom_k(V,k) (21.7)
2. The category of finite-dimensional representations of a Lie algebra or algebraic group is rigid (21.8)
3. A module over a ring admits a dual iff it is finitely generated and projective (21.7)
4. For representations, the contragredient is the dual

# Context & Application

Rigidity is a necessary condition for a tensor category to be tannakian. It corresponds to the fact that representations of groups have contragredient representations.

# Examples

**Example 1** (21.7): For a finite-dimensional k-vector space V, the dual is V^v = Hom_k(V,k) with ev(f tensor v) = f(v).

# Relationships

## Builds Upon
- **Tensor category** -- Rigidity is an additional property

## Enables
- **Neutral tannakian category** -- Requires rigidity

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21a, pages 234.

# Verification Notes

- Definition source: Direct from 21.7, 21.8
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
