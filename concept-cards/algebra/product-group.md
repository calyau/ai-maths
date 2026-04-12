---
concept: Product Group
slug: product-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.11 Product Groups"
extraction_confidence: high
aliases:
  - "direct product"
  - "G x G'"
prerequisites:
  - group
extends: []
related:
  - cyclic-group
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The product of groups G and G' is the group G x G' whose elements are pairs (a, a') with component-wise multiplication: (a,a')(b,b') = (ab, a'b'). The order is |G| * |G'|.

# Core Definition

The product G x G' has elements (a, a') with a in G and a' in G', with multiplication (a,a')(b,b') = (ab, a'b'). Identity is (1,1); inverse of (a,a') is (a^(-1), a'^(-1)) (Artin, p. 78, formula 2.11.1). C_rs ≅ C_r x C_s when gcd(r,s) = 1 (Proposition 2.11.3).

# Prerequisites

- **Group** — The factors are groups

# Key Properties

1. |G x G'| = |G| * |G'|
2. G x {1} and {1} x G' are normal subgroups
3. C_rs ≅ C_r x C_s when gcd(r,s) = 1
4. C_4 is NOT isomorphic to C_2 x C_2

# Construction / Recognition

## To Construct:
1. Form all pairs (a, a') with a in G and a' in G'
2. Multiply component-wise

## To Recognize:
1. H and K normal subgroups with H ∩ K = {1} and HK = G implies G ≅ H x K

# Context & Application

Product decomposition simplifies group analysis. Proposition 2.11.4 gives conditions for recognizing when a group is a product.

# Examples

**Example 1** (p. 78): C_6 ≅ C_2 x C_3 because gcd(2,3) = 1.

**Example 2** (p. 79): There are exactly two groups of order 4: C_4 and C_2 x C_2 (Klein four group).

# Relationships

## Builds Upon
- **Group** — Factors are groups

## Related
- **Cyclic group** — C_rs ≅ C_r x C_s when gcd(r,s) = 1
- **Normal subgroup** — Both factors embed as normal subgroups

# Common Errors

- **Error**: Assuming C_n x C_m is always cyclic
  **Correction**: C_n x C_m is cyclic iff gcd(n,m) = 1

# Common Confusions

- **Confusion**: Confusing product group with quotient group
  **Clarification**: Product builds a bigger group; quotient makes a smaller one

# Source Reference

Chapter 2: Groups, Section 2.11, pages 78-80.

# Verification Notes

- Definition source: Direct from (2.11.1), p. 78
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
