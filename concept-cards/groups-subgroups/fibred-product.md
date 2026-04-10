---
# === CORE IDENTIFICATION ===
concept: Fibred Product of Affine Groups
slug: fibred-product

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
aliases:
  - fibre product

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-group
  - coordinate-ring
extends: []
related:
  - kernel-of-homomorphism
  - product-of-affine-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The fibred product G_1 x_H G_2 of affine groups G_1 -> H <- G_2 is the functor R -> G_1(R) x_{H(R)} G_2(R), with coordinate ring O(G_1) tensor_{O(H)} O(G_2). Kernels, intersections, and equalizers are special cases.

# Core Definition

Given natural transformations G_1 -> H <- G_2 of functors, the **fibred product functor** G_1 x_H G_2 is the functor R -> G_1(R) x_{H(R)} G_2(R) (Section 4b, p. 34).

When G_1, G_2, H are represented by k-algebras A_1, A_2, B, the fibred product is represented by A_1 tensor_B A_2 (equation (21), p. 35). When these are affine groups with homomorphisms, the fibred product is an affine group with O(G_1 x_H G_2) = O(G_1) tensor_{O(H)} O(G_2) (equation (22)).

The **kernel** of alpha: G -> H is the fibred product G x_H * (where * is the trivial group), with O(Ker) = O(G) tensor_{O(H)} k = O(G)/I_H * O(G) (equation (23), p. 35).

# Prerequisites

- **Affine group** — The construction applies to affine groups
- **Coordinate ring** — The fibred product has coordinate ring given by a tensor product

# Key Properties

1. O(G_1 x_H G_2) = O(G_1) tensor_{O(H)} O(G_2)
2. Kernels are a special case of fibred products
3. Equalizers and intersections can be realized as fibred products
4. All finite direct limits exist in the category of affine groups

# Examples

**Example 1** (p. 35): Ker(G -> H) = G x_H *, with coordinate ring O(G)/I_H * O(G).

# Relationships

## Related
- **Kernel of homomorphism** — Ker(alpha) = G x_H *
- **Product of affine groups** — Products are fibred products over the trivial group

# Source Reference

Chapter I, Section 4b (p. 34-35).

# Verification Notes

- Definition source: Direct from Section 4b
- Confidence rationale: Explicit construction with formulas
- Uncertainties: None
- Cross-reference status: Verified
