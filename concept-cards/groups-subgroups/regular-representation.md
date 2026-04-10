---
concept: Regular Representation
slug: regular-representation
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 96
section: "8b Definition of a representation"
extraction_confidence: high
aliases:
  - right regular representation
prerequisites:
  - linear-representation
  - coordinate-ring
extends:
  - linear-representation
related:
  - faithful-representation
  - representation-comodule-correspondence
contrasts_with: []
answers_questions:
  - "What is the regular representation of an algebraic group?"
  - "Why does the regular representation contain all representations?"
---

# Quick Definition

The regular representation of an affine group G is the representation of G on its coordinate ring O(G), where g in G(R) acts on f in O(G) by (gf)_R(x) = f_R(xg). It is always faithful for algebraic groups.

# Core Definition

There is a unique linear representation r of G on O(G) (regarded as a k-vector space) such that (gf)_R(x) = f_R(xg) for all g in G(R), f in O(G), x in G(R). This is called the *regular representation*. The corresponding O(G)-comodule structure on O(G) is just the comultiplication Delta: O(G) -> O(G) tensor O(G) (Milne, Example 8.3 and 8.14, pp. 96, 103).

# Prerequisites

- **Linear representation** -- The regular representation is a specific instance
- **Coordinate ring** -- O(G) serves as both the representation space and the Hopf algebra

# Key Properties

1. The regular representation is faithful for algebraic groups (Theorem 8.31)
2. Every finite-dimensional representation embeds into a finite direct sum of copies of the regular representation (Propositions 8.35-8.37)
3. The comodule structure on O(G) corresponding to the regular representation is the comultiplication Delta
4. Every sufficiently large finite-dimensional subrepresentation of the regular representation is faithful

# Construction / Recognition

## To Construct:
1. Take V = O(G) as the representation space
2. Define the action: (gf)_R(x) = f_R(xg) for g in G(R), f in O(G), x in G(R)

## To Recognize:
1. The representation space is O(G) itself
2. The corresponding comodule structure is the comultiplication

# Context & Application

The regular representation is the universal representation: it contains all finite-dimensional representations as subrepresentations (up to direct sums). This is the key to proving that every algebraic group embeds into GL_n.

# Examples

**Example 1** (p. 94): For a finite group G, the regular representation is the action of G on the space of functions G -> k via (gf)(x) = f(xg). This gives an embedding G -> GL_n where n = |G|.

**Example 2** (p. 103): For G = G_a, the regular representation on k[X] has Delta(X) = X tensor 1 + 1 tensor X, so g = t acts by X -> X + t.

# Relationships

## Builds Upon
- **Linear representation** -- It is the canonical example

## Enables
- **Faithful representation** -- Subrepresentations of the regular representation provide faithful embeddings
- **Reconstruction theorem** -- The regular representation plays a key role in recovering G from Rep(G)

## Related
- **Representation-comodule correspondence** -- The regular representation corresponds to the comultiplication comodule

# Common Errors

- **Error**: Confusing left and right regular representations
  **Correction**: The formula (gf)(x) = f(xg) defines the right regular representation; the left version uses f(g^{-1}x)

# Common Confusions

- **Confusion**: Thinking the regular representation is always finite-dimensional
  **Clarification**: For algebraic groups, O(G) is typically infinite-dimensional; but it contains faithful finite-dimensional subrepresentations

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8b-8j, pages 96-107. Key results: Example 8.3, Theorem 8.31, Propositions 8.35-8.37.

# Verification Notes

- Definition source: Direct from Example 8.3, p. 96
- Confidence rationale: Explicit construction with many derived results
- Uncertainties: None
- Cross-reference status: Verified
