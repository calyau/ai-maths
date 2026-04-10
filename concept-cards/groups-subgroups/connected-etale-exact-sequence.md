---
concept: Connected-Etale Exact Sequence
slug: connected-etale-exact-sequence
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 157
section: "13c Algebraic groups"
extraction_confidence: high
aliases: []
prerequisites:
  - connected-component-group
  - etale-affine-group
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How does an algebraic group decompose into connected and discrete parts?"
---

# Quick Definition

Every algebraic group G fits into a canonical exact sequence 1 -> G^0 -> G -> pi_0(G) -> 1 where G^0 is the connected identity component and pi_0(G) is the etale group of connected components. This is called the connected-etale exact sequence.

# Core Definition

For any algebraic group G, Proposition 13.17 establishes that G^0 is the unique connected normal subgroup of G such that G/G^0 is etale. The exact sequence 1 -> G^0 -> G -> pi_0(G) -> 1 is called the *connected-etale exact sequence*. Over perfect fields, this sequence splits for finite groups: G = G^0 rtimes pi_0(G) (Milne, pp. 157-158).

# Prerequisites

- **Connected component group** -- G^0 and pi_0(G) are the terms
- **Etale affine group** -- pi_0(G) is etale

# Key Properties

1. G^0 is connected and normal; pi_0(G) is etale
2. This decomposition is unique (Proposition 13.17)
3. Commutes with field extension (Proposition 13.18)
4. For products: pi_0(G x G') = pi_0(G) x pi_0(G') (Proposition 13.19)
5. Splits over perfect fields for finite G (13.22)

# Context & Application

This is the first step in the structural decomposition of any algebraic group: separate the connected part from the finite discrete part.

# Examples

**Example 1** (p. 159): For O(q) (orthogonal group): 1 -> SO(q) -> O(q) -> {+/-1} -> 1.

**Example 2** (p. 159): For monomial matrices in GL_n: 1 -> D_n -> G -> S_n -> 1.

# Relationships

## Builds Upon
- **Connected component group** -- The terms in the sequence

# Source Reference

Chapter I, Section 13c, pages 157-158. Proposition 13.17.

# Verification Notes

- Definition source: Direct from Proposition 13.17
- Confidence rationale: Named sequence with explicit characterization
- Uncertainties: None
- Cross-reference status: Verified
