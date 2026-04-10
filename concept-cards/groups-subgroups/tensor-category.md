---
concept: Tensor Category
slug: tensor-category
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 233
section: "21a Tensor categories"
extraction_confidence: high
aliases:
  - "monoidal category"
prerequisites: []
extends: []
related:
  - neutral-tannakian-category
  - rigid-tensor-category
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
  - "What must I know before understanding tannakian duality?"
---

# Quick Definition

A tensor category over k is a k-linear category equipped with a k-bilinear bifunctor tensor, together with compatible associativity and commutativity constraints, and a neutral object (identity for tensor product).

# Core Definition

A **tensor category** over k is a k-linear category C together with a k-bilinear functor tensor: C x C -> C and compatible associativity and commutativity constraints ensuring that the tensor product of any unordered finite set of objects is well-defined up to a well-defined isomorphism (Milne, 21.2). A **neutral object** is an object U with an isomorphism u: U -> U tensor U such that V -> V tensor U is an equivalence.

# Prerequisites

This is a foundational categorical concept within this context.

# Key Properties

1. A k-linear category has finite-dimensional Hom sets with k-bilinear composition (21.1)
2. Associativity constraint: phi_{U,V,W}: U tensor (V tensor W) -> (U tensor V) tensor W (21.2)
3. Commutativity constraint: psi_{V,W}: V tensor W -> W tensor V (21.2)
4. Compatibility conditions: certain diagrams must commute (21.2)
5. A tensor functor (F,c) between tensor categories preserves the tensor structure (21.6)

# Context & Application

Tensor categories provide the abstract framework for representation theory. The category of finite-dimensional representations of a group or Lie algebra is a tensor category, and the Tannaka reconstruction theorem shows that groups can be recovered from their tensor categories of representations.

# Examples

**Example 1** (21.4): The category of finitely generated modules over a ring R is a tensor category with the usual tensor product.

**Example 2** (21.5): The category of finite-dimensional representations of a Lie algebra or algebraic group is a tensor category.

# Relationships

## Enables
- **Rigid tensor category** -- A tensor category where every object has a dual
- **Neutral tannakian category** -- A rigid abelian tensor category with a fibre functor

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21a, pages 233-234.

# Verification Notes

- Definition source: Direct from 21.2
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
