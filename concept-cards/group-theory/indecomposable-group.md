---
# === CORE IDENTIFICATION ===
concept: Indecomposable Group
slug: indecomposable-group

# === CLASSIFICATION ===
category: groups-with-operators
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 97
section: "Krull-Schmidt theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - direct-product
extends: []
related:
  - krull-schmidt-theorem
  - simple-group
contrasts_with:
  - simple-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an indecomposable group?"
  - "What distinguishes a simple group from an indecomposable group?"
---

# Quick Definition

A group G is indecomposable if G != {1} and G cannot be written as a direct product of two nontrivial groups. Every simple group is indecomposable, but an indecomposable group need not be simple (it may have normal subgroups).

# Core Definition

A group G is *indecomposable* if G != 1 and G is not isomorphic to a direct product of two nontrivial groups:

G isomorphic to H x H' implies H = 1 or H' = 1.

(Milne, p. 97)

# Prerequisites

- **group** -- the ambient concept
- **direct-product** -- indecomposability is defined relative to direct products

# Key Properties

1. Simple implies indecomposable (no normal subgroups to form a product)
2. Indecomposable does NOT imply simple: S_3 is indecomposable (cannot be C_2 x C_3) but has C_3 as a normal subgroup
3. A finite commutative group is indecomposable iff it is cyclic of prime-power order
4. Every finite group can be written as a direct product of indecomposable groups

# Examples

**Example 1** (p. 97, 6.30a): S_3 is indecomposable but not simple (has normal subgroup C_3).

**Example 2** (p. 97, 6.30b): C_{p^n} is indecomposable (both factors in any product decomposition must be p-groups, and one must be C_{p^n} itself). Conversely, C_6 = C_2 x C_3 is decomposable.

**Example 3** (p. 97, 6.30c): Every finite group is a direct product of indecomposable groups.

# Relationships

## Enables
- **krull-schmidt-theorem** -- uniqueness of indecomposable decomposition

## Contrasts With
- **simple-group** -- simple implies indecomposable, but not conversely; simple means no *normal* subgroups, indecomposable means no *direct product* decomposition

# Common Confusions

- **Confusion**: Thinking indecomposable = simple
  **Clarification**: S_3 is indecomposable but not simple. A group can have normal subgroups without being a direct product.

# Source Reference

Chapter 6, p. 97. Examples 6.30.

# Verification Notes

- Definition source: Direct from p. 97
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
