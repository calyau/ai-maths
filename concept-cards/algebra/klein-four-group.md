---
concept: Klein Four Group
slug: klein-four-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.4 Cyclic Groups"
extraction_confidence: high
aliases:
  - "V"
  - "Vierergruppe"
  - "C_2 x C_2"
prerequisites:
  - group
  - product-group
extends: []
related:
  - cyclic-group
contrasts_with:
  - cyclic-group
answers_questions:
  - "What is a group?"
---

# Quick Definition

The Klein four group V is the group of four 2x2 diagonal matrices with entries +/-1. It is isomorphic to C_2 x C_2 and is the simplest group that is not cyclic. Every non-identity element has order 2.

# Core Definition

The Klein four group V consists of the four matrices [[+/-1, 0],[0, +/-1]] (Artin, p. 59). It is isomorphic to C_2 x C_2 and is not cyclic: no single element generates it. There are two isomorphism classes of groups of order 4: C_4 (cyclic) and V (Proposition 2.11.5).

# Prerequisites

- **Group** — V is a group
- **Product group** — V ≅ C_2 x C_2

# Key Properties

1. |V| = 4
2. Every non-identity element has order 2
3. Not cyclic (no element of order 4)
4. Abelian
5. Any two non-identity elements generate V

# Construction / Recognition

## To Construct:
1. Take diagonal 2x2 matrices with entries +/-1

## To Recognize:
1. A group of order 4 where every non-identity element has order 2

# Context & Application

V is one of the two groups of order 4 and serves as a key example showing that not all groups are cyclic. It appears as the kernel of the homomorphism S_4 -> S_3 (formula 2.5.15).

# Examples

**Example 1** (p. 59): V = {[[1,0],[0,1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[-1,0],[0,-1]]}.

**Example 2** (p. 65): K = {1, (12)(34), (13)(24), (14)(23)} in S_4 is isomorphic to V.

# Relationships

## Related
- **Product group** — V ≅ C_2 x C_2

## Contrasts With
- **Cyclic group** — C_4 is the other group of order 4; it IS cyclic

# Common Errors

- **Error**: Thinking V is cyclic
  **Correction**: V has no element of order 4, so it cannot be cyclic

# Common Confusions

- **Confusion**: Confusing V with C_4
  **Clarification**: Both have order 4, but V has all elements of order <= 2, while C_4 has elements of order 4

# Source Reference

Chapter 2: Groups, Sections 2.4, 2.11, pages 59, 79-80.

# Verification Notes

- Definition source: Direct from p. 59 and Proposition 2.11.5
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
