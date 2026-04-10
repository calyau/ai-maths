---
concept: Almost-Direct Product
slug: almost-direct-product
category: group-structure
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 197
section: "17d Semisimple groups"
extraction_confidence: high
aliases: []
prerequisites:
  - semisimple-algebraic-group
  - almost-simple-algebraic-group
extends: []
related:
  - isogeny
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

An algebraic group G is the almost-direct product of subgroups G_1,...,G_r if the multiplication map G_1 x ... x G_r -> G is a surjective homomorphism with finite kernel.

# Core Definition

An algebraic group G is said to be the **almost-direct product** of its algebraic subgroups G_1,...,G_r if the map (g_1,...,g_r) -> g_1...g_r from G_1 x ... x G_r to G is a surjective homomorphism with finite kernel (Milne, p. 197). This implies the G_i commute pairwise and each G_i is normal in G.

# Prerequisites

- **Semisimple algebraic group** -- The decomposition theorem applies to semisimple groups
- **Almost-simple algebraic group** -- The factors in the decomposition are almost-simple

# Key Properties

1. The G_i commute pairwise and are each normal in G
2. The kernel of the multiplication map is finite (an isogeny)
3. Every semisimple group is an almost-direct product of almost-simple groups (Theorem 17.16)
4. For simply connected semisimple groups, the decomposition is a direct product

# Construction / Recognition

## To Construct:
1. Identify the almost-simple normal subgroups G_1,...,G_r of G
2. Verify the multiplication map is surjective with finite kernel

## To Recognize:
1. Check that G_1,...,G_r commute, are normal, and generate G
2. Verify the intersection of any G_i with the product of the rest is finite

# Context & Application

The almost-direct product structure is the group-theoretic analogue of the direct sum decomposition of semisimple Lie algebras into simple ideals. At the Lie algebra level, the decomposition is always direct; at the group level, the kernel may be nontrivial (e.g., the centre).

# Examples

**Example 1** (p. 197): SL_2 x SL_2 -> SO_4 is an almost-direct product with kernel Z/2Z.

# Relationships

## Builds Upon
- **Semisimple algebraic group** -- Provides the context for the decomposition

## Enables
- **Classification of semisimple groups** -- Reduces to classifying almost-simple groups

# Common Errors

- **Error**: Assuming an almost-direct product is a direct product
  **Correction**: The kernel of the multiplication map can be nontrivial

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17d, pages 197-199.

# Verification Notes

- Definition source: Direct from p. 197
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
