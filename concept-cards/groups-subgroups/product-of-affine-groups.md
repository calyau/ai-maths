---
# === CORE IDENTIFICATION ===
concept: Product of Affine Groups
slug: product-of-affine-groups

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 34
section: "Some basic constructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-group
extends: []
related:
  - fibred-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The product G_1 x G_2 of affine groups has functor R -> G_1(R) x G_2(R) and coordinate ring O(G_1) tensor O(G_2). Finite products of algebraic groups are algebraic groups.

# Core Definition

For affine groups G_1, G_2 over k, the **product** G_1 x G_2 is the functor R -> G_1(R) x G_2(R), which is an affine group with coordinate ring O(G_1 x G_2) = O(G_1) tensor_k O(G_2) (Section 4a, p. 34, equation (18)).

This follows from the universal property of tensor products: Hom_{k-alg}(A_1 tensor A_2, R) = Hom_{k-alg}(A_1, R) x Hom_{k-alg}(A_2, R).

More generally, arbitrary products of affine groups exist (infinite products use infinite tensor products).

# Prerequisites

- **Affine group** — Products of affine groups

# Key Properties

1. O(G_1 x G_2) = O(G_1) tensor O(G_2)
2. Finite products of algebraic groups are algebraic
3. G_1 x G_2 with projection maps is the categorical product

# Source Reference

Chapter I, Section 4a (p. 34).

# Verification Notes

- Definition source: Direct from Section 4a
- Confidence rationale: Explicit construction
- Uncertainties: None
- Cross-reference status: Verified
