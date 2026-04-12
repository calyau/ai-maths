---
# === CORE IDENTIFICATION ===
concept: Abelianness of Direct Products
slug: direct-product-abelianness

# === CLASSIFICATION ===
category: structure-theory
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Products"
chapter_number: 10
pdf_page: 59
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-product
extends: []
related:
  - isomorphism-preserves-commutativity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a direct product abelian?"
  - "How do direct products relate to the constituent groups?"
---

# Quick Definition

$G \times H$ is abelian if and only if both $G$ and $H$ are abelian.

# Core Definition

Armstrong states: "If $G$ and $H$ are both abelian, then $G \times H$ is abelian" (p. 59). The converse also holds: since $G$ is isomorphic to the subgroup $\{(g, e) \mid g \in G\}$ of $G \times H$, if $G \times H$ is abelian then this subgroup (isomorphic to $G$) must be abelian, hence $G$ is abelian. Similarly for $H$.

# Prerequisites

- **Direct product** — The construction whose commutativity is studied

# Key Properties

1. $G \times H$ is abelian iff both $G$ and $H$ are abelian
2. Forward direction: componentwise multiplication of commuting elements commutes
3. Reverse direction: factors embed as subgroups, which must be abelian

# Construction / Recognition

## To Check Abelianness:
1. Check if $G$ is abelian
2. Check if $H$ is abelian
3. $G \times H$ is abelian iff both are

# Context & Application

This characterization quickly determines the commutativity of product groups. Combined with the cyclicity criterion, it shows for instance that $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian (but not cyclic).

# Examples

**Example** (p. 59): $\mathbb{Z}_2 \times \mathbb{Z}_3$ is abelian because both $\mathbb{Z}_2$ and $\mathbb{Z}_3$ are abelian.

**Example**: $S_3 \times \mathbb{Z}_2$ is non-abelian because $S_3$ is non-abelian.

# Relationships

## Builds Upon
- **Direct product** — Property of the construction

## Related
- **Isomorphism preserves commutativity** — Related structural preservation

# Common Errors

- **Error**: Assuming $G \times H$ is non-abelian because $|G \times H|$ is large.
  **Correction**: Size does not determine abelianness. $\mathbb{Z}_{100} \times \mathbb{Z}_{200}$ is abelian despite having 20000 elements.

# Common Confusions

- **Confusion**: Confusing abelian with cyclic for products.
  **Clarification**: $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian but not cyclic. Abelianness is weaker than cyclicity.

# Source Reference

Chapter 10: Products, page 59 (pdf p. 59).

# Verification Notes

- Statement: Direct from p. 59
- Confidence: HIGH — explicit statement
