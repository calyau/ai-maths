---
# === CORE IDENTIFICATION ===
concept: Defining Relations
slug: defining-relations

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - relators
  - relations

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-group
  - normal-subgroup
extends: []
related:
  - presentation-of-a-group
  - finitely-presented-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are defining relations of a group?"
  - "How do defining relations determine a group?"
---

# Quick Definition

Defining relations are a collection R of words in a free group F(X) that, together with all their conjugates, generate the kernel N of the surjection F(X) -> G. They specify exactly which products of generators equal the identity in G.

# Core Definition

"Let R be a collection of words in F(X) which together with all their conjugates generate N. That is to say, N is the smallest normal subgroup of F(X) which contains R. These words determine precisely which words in F(X) become the identity when we pass from F(X) to G or, equivalently, which products of elements of G are the identity in G. We shall call R a set of defining relations for G" (Armstrong, Ch. 27, p. 176).

# Prerequisites

- **Free group** -- Relations are words in the free group F(X)
- **Normal subgroup** -- The relations generate a normal subgroup (the kernel)

# Key Properties

1. R is a subset of F(X) whose elements represent the identity in G
2. N = normal closure of R is the smallest normal subgroup containing R
3. G = F(X)/N
4. Different choices of R can give the same group G
5. The empty set of relations gives the free group itself

# Construction / Recognition

## To Verify a Set of Relations
1. Show each relation w in R maps to the identity under pi: F(X) -> G
2. Show the normal closure of R equals ker(pi)
3. One approach (Armstrong's method for D_n): show |F(X)/M| = |G| where M is the normal closure of R

# Context & Application

Armstrong demonstrates the verification of defining relations through the dihedral group example (Example (i), p. 176), showing that {r^n, s^2, (rs)^2} are defining relations for D_n by proving |F(X)/M| = 2n.

# Examples

**Example 1** (p. 176): For D_n with generators r, s: the words r^n, s^2, (rs)^2 form a set of defining relations.

**Example 2** (p. 177): For Z x Z with generators x, y: the single word xyx^{-1}y^{-1} is the only defining relation.

**Example 3** (p. 177): For Z_6 = {x | x^6}: the single word x^6 is the defining relation.

# Relationships

## Enables
- **Presentation of a group** -- A presentation is a pair (X, R)
- **Finitely presented group** -- When R is finite

## Related
- **Free group** -- R = empty set gives a free group

# Common Errors

- **Error**: Listing redundant relations as if they are all necessary
  **Correction**: A set of defining relations need not be minimal; but verifying sufficiency requires checking |F(X)/N| = |G|

# Common Confusions

- **Confusion**: Thinking the relations r^n = e, s^2 = e are equations rather than words
  **Clarification**: Formally, the relations are the words r^n, s^2, (rs)^2; the equation r^n = e means the word r^n lies in N

# Source Reference

Chapter 27: Free Groups and Presentations, page 176 (pdf p. 176).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 176
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
