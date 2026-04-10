---
concept: Faithful Representation
slug: faithful-representation
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 105
section: "8i Algebraic groups admit finite-dimensional faithful representations"
extraction_confidence: high
aliases: []
prerequisites:
  - linear-representation
  - regular-representation
extends:
  - linear-representation
related:
  - chevalley-theorem
contrasts_with: []
answers_questions:
  - "What is a faithful representation of an algebraic group?"
  - "Can every algebraic group be embedded in GL_n?"
---

# Quick Definition

A faithful representation is a representation r: G -> GL_V such that all the homomorphisms r_R: G(R) -> GL(V(R)) are injective. Every algebraic group admits a faithful finite-dimensional representation, hence embeds into GL_n for some n.

# Core Definition

A linear representation (V, r) of an affine group G is *faithful* if all the homomorphisms r_R are injective. Equivalently, it is faithful if the corresponding Hopf algebra map O(GL_V) -> O(G) is surjective. Theorem 8.31 states: for any algebraic group G, the regular representation has faithful finite-dimensional subrepresentations. Furthermore, if V is any faithful representation, then every finite-dimensional representation is a quotient of a sub-representation of a direct sum of tensor powers of V and its dual (Theorem 8.44, Milne, pp. 105-110).

# Prerequisites

- **Linear representation** -- Faithful is a property of a representation
- **Regular representation** -- Source of faithful subrepresentations

# Key Properties

1. Every algebraic group has a faithful finite-dimensional representation (Theorem 8.31)
2. A faithful representation V generates Rep(G): every simple G-module is a Jordan-Holder quotient of tensor powers of V direct-sum V^dual (Corollary 8.45)
3. The representation on V is faithful iff A(V direct-sum V^dual) = O(G) (Lemma 8.43)
4. V is a union of its finite-dimensional faithful subrepresentations (Proposition 8.33)

# Construction / Recognition

## To Construct:
1. Take a finite-dimensional subcomodule V of O(G) containing generators for O(G) as a k-algebra
2. The corresponding representation G -> GL_V is faithful

## To Recognize:
1. Check that the map O(GL_V) -> O(G) is surjective
2. Equivalently, check that the matrix coefficients a_{ij} generate O(G)

# Context & Application

The existence of faithful representations is the bridge between the abstract theory of algebraic groups and concrete matrix group theory. It justifies calling algebraic groups "linear algebraic groups" and enables the use of matrix techniques.

# Examples

**Example 1** (p. 106): For GL_n, the standard representation on k^n is faithful. The matrix coefficients X_{ij} generate O(GL_n).

# Relationships

## Builds Upon
- **Regular representation** -- Faithful representations arise as subrepresentations of the regular representation

## Enables
- **Chevalley theorem** -- Every subgroup is the stabilizer of a line in some faithful representation

# Common Confusions

- **Confusion**: Thinking faithful means faithful on k-points only
  **Clarification**: Faithfulness requires injectivity on R-points for ALL k-algebras R, not just k itself

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8i-8k, pages 105-111. Theorem 8.31, Theorem 8.44.

# Verification Notes

- Definition source: Direct from text, p. 95 and Theorem 8.31
- Confidence rationale: Explicit definition and major theorem
- Uncertainties: None
- Cross-reference status: Verified
