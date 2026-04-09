---
# === CORE IDENTIFICATION ===
concept: Klein Four-Group
slug: klein-four-group

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
pdf_page: 13
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Vierergruppe
  - Klein Vierergruppe
  - 4-group
  - "V"
  - "V₄"
  - "D₂"
  - "C₂ × C₂"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - direct-product-of-groups
  - cyclic-group
extends:
  - abelian-group
related:
  - dihedral-group
  - groups-of-small-order
contrasts_with:
  - cyclic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Klein four-group?"
  - "What is the smallest non-cyclic group?"
  - "What are the groups of order 4?"
---

# Quick Definition

The Klein four-group V_4 (or V) is the group C_2 x C_2 = {1, r, s, rs} of order 4. It is the unique non-cyclic group of order 4 and equals D_2.

# Core Definition

The group D_2 is defined to be C_2 x C_2 = {1, r, s, rs}. It is also called the **Klein Vierergruppe** or, more simply, the **4-group**, and denoted V or V_4 (p. 13).

# Prerequisites

- **Group** — V_4 is a group
- **Direct product of groups** — V_4 = C_2 x C_2
- **Cyclic group** — V_4 is a product of cyclic groups but is not itself cyclic

# Key Properties

1. |V_4| = 4
2. V_4 = C_2 x C_2 = D_2
3. Every non-identity element has order 2
4. V_4 is abelian
5. V_4 is not cyclic (no element of order 4)
6. V_4 is one of exactly two groups of order 4 (the other is C_4)

# Construction / Recognition

## To Construct:
1. Take C_2 = {0, 1} with addition mod 2
2. Form C_2 x C_2 = {(0,0), (1,0), (0,1), (1,1)}
3. The operation is componentwise addition mod 2

## To Recognize:
1. A group of order 4 in which every non-identity element has order 2
2. Equivalently, a group of order 4 that is not cyclic

# Context & Application

The Klein four-group is the smallest non-cyclic group. It demonstrates that groups of the same order need not be isomorphic (C_4 vs. V_4). It is the starting point for understanding how the classification of groups of a given order can yield multiple non-isomorphic groups.

# Examples

**Example 1** (p. 13, 1.17): D_2 = C_2 x C_2 = {1, r, s, rs}.

**Example 2** (p. 14, table): The two groups of order 4 are C_4 and C_2 x C_2.

# Relationships

## Builds Upon
- **direct-product-of-groups** — V_4 = C_2 x C_2
- **abelian-group** — V_4 is abelian

## Related
- **dihedral-group** — V_4 = D_2
- **groups-of-small-order** — one of the two groups of order 4

## Contrasts With
- **cyclic-group** — C_4 is cyclic with an element of order 4; V_4 has no such element

# Common Confusions

- **Confusion**: Thinking all groups of order 4 are cyclic
  **Clarification**: V_4 = C_2 x C_2 is a non-cyclic group of order 4

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.17, page 13.

# Verification Notes

- Definition source: Direct from 1.17, p. 13
- Confidence rationale: HIGH — explicitly defined and named
- Uncertainties: None
- Cross-reference status: Verified against planned cards
