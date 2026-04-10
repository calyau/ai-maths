---
concept: Characterization of Representation Categories
slug: characterization-of-representation-categories
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 137
section: "11 Characterizations of categories of representations"
extraction_confidence: high
aliases:
  - Tannakian description theorem
  - description theorem
prerequisites:
  - category-of-representations
  - reconstruction-theorem
  - comodule
extends:
  - reconstruction-theorem
related: []
contrasts_with: []
answers_questions:
  - "Which abstract categories arise as Rep(G) for some algebraic group G?"
---

# Quick Definition

The description theorem (Theorem 11.14) characterizes which abstract tensor categories arise as categories of representations of affine groups: a k-linear abelian category C with a k-bilinear tensor product and a faithful exact functor omega: C -> Vec_k satisfying tensor compatibility conditions is equivalent to Rep(G) for a unique affine monoid G.

# Core Definition

*Theorem 11.14*: Let C be a k-linear abelian category with a k-bilinear functor tensor: C x C -> C. Let omega: C -> Vec_k be an exact faithful k-linear functor satisfying: (a) omega(X tensor Y) = omega(X) tensor omega(Y), (b) the associativity and commutativity isomorphisms live in C, (c) there exists an identity object 1 with omega(1) = k. Then C is equivalent to Rep(G) for a unique affine monoid G = End^tensor(omega). If additionally (d) every 1-dimensional object has an inverse under tensor, then G is an affine group (Milne, pp. 142-143).

# Prerequisites

- **Category of representations** -- The target of the equivalence
- **Reconstruction theorem** -- The monoid/group is recovered from the category
- **Comodule** -- The intermediate step: C is first shown to be Comod(B)

# Key Properties

1. The proof proceeds in two steps: first show C = Comod(B) for a coalgebra B (Theorem 11.1), then show the tensor structure makes B a bialgebra (Theorem 11.13)
2. Condition (d) (existence of duals for 1-dim objects) is what gives an inversion (antipode), making G a group
3. This is the algebraic version of Tannaka-Krein duality
4. The forgetful functor omega (the "fiber functor") is an essential part of the data

# Context & Application

This theorem provides the abstract foundation for Tannakian categories. It shows that the concept of "algebraic group" is not an arbitrary definition but is forced by the axioms of tensor categories with fiber functors.

# Examples

**Example 1** (p. 143): Starting with (Rep_k(G), forget), following through the proof recovers Theorem 10.2: Aut^tensor(omega) is represented by G.

# Relationships

## Builds Upon
- **Reconstruction theorem** -- Generalized from "recovering G" to "characterizing Rep(G)"

## Enables
- Applications to motives and Galois representations (Tannakian formalism)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 11, pages 137-144. Theorems 11.1, 11.5, 11.13, 11.14.

# Verification Notes

- Definition source: Direct from Theorem 11.14
- Confidence rationale: Major theorem with systematic proof
- Uncertainties: None
- Cross-reference status: Verified
