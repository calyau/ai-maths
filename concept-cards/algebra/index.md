---
concept: Index
slug: index
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.8 Cosets"
extraction_confidence: high
aliases:
  - "[G:H]"
  - "index of a subgroup"
prerequisites:
  - subgroup
  - coset
extends: []
related:
  - lagranges-theorem
contrasts_with: []
answers_questions:
  - "What is a coset?"
---

# Quick Definition

The index [G:H] of a subgroup H in G is the number of left cosets of H in G. The counting formula gives |G| = |H| * [G:H].

# Core Definition

The number of left cosets of a subgroup H in G is called the index of H in G, denoted [G:H] (Artin, p. 71, formula 2.8.6). The counting formula is |G| = |H| * [G:H] (formula 2.8.8).

# Prerequisites

- **Subgroup** — H must be a subgroup of G
- **Coset** — The index counts cosets

# Key Properties

1. |G| = |H| * [G:H]
2. The index of ker(phi) equals |im(phi)|
3. [G:K] = [G:H][H:K] for subgroups G ⊃ H ⊃ K (Proposition 2.8.14)

# Construction / Recognition

## To Construct:
1. List all distinct left cosets of H in G
2. Count them

## To Recognize:
1. |G|/|H| for finite groups

# Context & Application

The index links the size of a group to the size of its subgroups and underlies Lagrange's theorem.

# Examples

**Example 1** (p. 71): [S_3 : <y>] = 3, since |S_3| = 6 and |<y>| = 2.

# Relationships

## Builds Upon
- **Coset** — Index counts cosets

## Related
- **Lagrange's theorem** — |H| divides |G| because [G:H] = |G|/|H|

# Common Errors

- **Error**: Assuming the index must be finite
  **Correction**: For infinite groups, the index can be infinite

# Common Confusions

- **Confusion**: Confusing the index [G:H] with the order |H|
  **Clarification**: [G:H] = number of cosets = |G|/|H|; |H| = size of each coset

# Source Reference

Chapter 2: Groups, Section 2.8, page 71.

# Verification Notes

- Definition source: Direct from (2.8.6), p. 71
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
