---
concept: Tannakian Correspondence
slug: tannakian-correspondence
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 236
section: "21b Neutral tannakian categories"
extraction_confidence: high
aliases: []
prerequisites:
  - neutral-tannakian-category
  - tannaka-dual
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
---

# Quick Definition

The Tannakian correspondence gives a natural order-reversing bijection between tannakian subcategories of Rep(G) and normal algebraic subgroups of G.

# Core Definition

For C = Rep(G), the maps S -> H(S) = intersection of Ker(r_V) for V in S, and H -> C^H (representations on which H acts trivially), form a Galois correspondence between subsets of ob(C) and algebraic subgroups of G. This restricts to a bijection between tannakian subcategories and normal algebraic subgroups (Milne, 21.18b).

# Prerequisites

- **Neutral tannakian category** -- The correspondence applies to tannakian categories
- **Tannaka dual** -- G is the Tannaka dual of C

# Key Properties

1. A tannakian subcategory is a full subcategory closed under duals, tensor products, direct sums, and subquotients
2. C^H is a neutral tannakian category with Tannaka dual G/N, where N is the smallest normal subgroup containing H (21.18a)
3. The correspondence is order-reversing: larger subcategories correspond to smaller subgroups

# Context & Application

This correspondence is the representation-theoretic analogue of the Galois correspondence between subfields and subgroups. It shows that the internal structure of a tensor category mirrors the subgroup structure of its Tannaka dual.

# Examples

**Example 1** (21.16): The subcategory of Rep(G) on which a normal subgroup N acts trivially has Tannaka dual G/N.

# Relationships

## Builds Upon
- **Neutral tannakian category** -- The correspondence operates within tannakian categories

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21b, page 236.

# Verification Notes

- Definition source: Direct from 21.18b
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
