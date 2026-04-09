---
# === CORE IDENTIFICATION ===
concept: Direct Product of Groups
slug: direct-product-of-groups

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 8
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - direct product
  - "G × H"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - klein-four-group
  - groups-of-small-order
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you construct new groups from existing ones?"
  - "What is the direct product of two groups?"
---

# Quick Definition

The direct product G x H of two groups G and H is the group whose underlying set is the cartesian product of G and H, with componentwise multiplication: (g, h)(g', h') = (gg', hh').

# Core Definition

When G and H are groups, the **(direct) product** G x H is constructed as follows: as a set, it is the cartesian product of G and H, and multiplication is defined by (g, h)(g', h') = (gg', hh') (Example 1.5, p. 8).

# Prerequisites

- **Group** — the factors G and H must be groups

# Key Properties

1. |G x H| = |G| * |H|
2. The operation is componentwise
3. The neutral element is (e_G, e_H)
4. The inverse of (g, h) is (g^{-1}, h^{-1})
5. G x H is abelian if and only if both G and H are abelian

# Construction / Recognition

## To Construct:
1. Form the cartesian product of the underlying sets
2. Define multiplication componentwise: (g, h)(g', h') = (gg', hh')
3. The group axioms are inherited from G and H

# Context & Application

The direct product is a fundamental construction for building larger groups from smaller ones. Many groups of small order are direct products, for example C_6 ≈ C_2 x C_3, and the Klein four-group V_4 = C_2 x C_2. The construction extends to any finite number of factors.

# Examples

**Example 1** (p. 13, 1.17): D_2 = C_2 x C_2, the Klein four-group.

**Example 2** (p. 14, table): C_2 x C_2 is one of the two groups of order 4.

**Example 3** (p. 14, table): C_2 x C_4 and C_2 x C_2 x C_2 appear among the five groups of order 8.

# Relationships

## Builds Upon
- **group** — the factors must be groups

## Enables
- **klein-four-group** — defined as C_2 x C_2
- **groups-of-small-order** — many small groups are direct products

## Related
- **abelian-group** — direct products of abelian groups are abelian

# Common Errors

- **Error**: Confusing the direct product with the cartesian product of sets
  **Correction**: The direct product includes the componentwise group operation, not just the set

# Common Confusions

- **Confusion**: Thinking G x H is always different from H x G
  **Clarification**: G x H and H x G are isomorphic (the isomorphism swaps components)

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.5, page 8.

# Verification Notes

- Definition source: Direct from Example 1.5, p. 8
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
