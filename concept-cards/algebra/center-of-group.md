---
concept: Center of a Group
slug: center-of-group
category: group-theory
subcategory: conjugation
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.2 The Class Equation"
extraction_confidence: high
aliases:
  - "Z"
  - "Z(G)"
prerequisites:
  - centralizer
extends: []
related:
  - class-equation
  - p-group
contrasts_with: []
answers_questions:
  - "What is the center of a group?"
---

# Quick Definition

The center Z of a group G is the set of elements that commute with every element: Z = {z in G | zy = yz for all y}. An element is central iff its conjugacy class is {x} alone.

# Core Definition

The center Z of a group G is Z = {z in G | zy = yz for all y in G} (Artin, p. 207). An element x is in the center iff Z(x) = G, iff C(x) = {x} (Proposition 7.2.5(b)).

# Prerequisites

- **Centralizer** — Z = intersection of all Z(x) = {g | Z(g) = G}

# Key Properties

1. Z is a normal subgroup of G
2. x in Z iff Z(x) = G iff C(x) = {x}
3. G is abelian iff Z = G
4. For p-groups, Z is nontrivial (Proposition 7.3.1)

# Examples

**Example 1** (p. 208): In S_3, the center is {1} (trivial).

**Example 2** (p. 209): In a p-group, the center is nontrivial.

# Relationships

## Builds Upon
- **Centralizer** — Z is the intersection of all centralizers

## Enables
- **Class equation** — Central elements contribute singleton classes
- **Groups of order p^2 are abelian** — Proved via the center

# Source Reference

Chapter 7, Section 7.2, Proposition 7.2.5, p. 207.

# Verification Notes

- Definition source: From p. 207 (originally defined in Chapter 2, recalled here)
- Confidence rationale: Explicitly described
- Uncertainties: None
- Cross-reference status: Verified
