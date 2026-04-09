---
# === CORE IDENTIFICATION ===
concept: Simple vs. Indecomposable Groups
slug: simple-vs-indecomposable

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
  - simple-group
  - indecomposable-group
extends: []
related:
  - krull-schmidt-theorem
  - jordan-holder-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a simple group from an indecomposable group?"
---

# Quick Definition

A simple group has no proper nontrivial normal subgroups; an indecomposable group cannot be written as a direct product of two nontrivial groups. Every simple group is indecomposable, but not conversely: S_3 is indecomposable (not a direct product) but has C_3 as a normal subgroup.

# Core Definition

**Simple**: G has no normal subgroups other than {1} and G.
**Indecomposable**: G is isomorphic to H x H' implies H = 1 or H' = 1.

Simple implies indecomposable (a direct factor is always normal, so if G = H x H' nontrivially, both H and H' are proper nontrivial normal subgroups).

Indecomposable does NOT imply simple: S_3 is indecomposable but has C_3 as a normal subgroup (Example 6.30a).

(Milne, p. 97)

# Prerequisites

- **simple-group** -- the stronger notion
- **indecomposable-group** -- the weaker notion

# Key Properties

1. A group can have normal subgroups without being decomposable (the normal subgroup may not have a complement)
2. Composition factors (Jordan-Holder) are simple; direct factors (Krull-Schmidt) are indecomposable
3. The two uniqueness theorems are parallel: Jordan-Holder for simple factors, Krull-Schmidt for indecomposable factors

# Examples

**Example 1** (p. 97): S_3 has normal subgroup C_3 but is indecomposable: S_3 is not C_2 x C_3 because S_3 is nonabelian while C_2 x C_3 is abelian.

**Example 2** (p. 97): C_{p^n} is both simple (for n = 1) and indecomposable (for all n).

# Relationships

## Related
- **jordan-holder-theorem** -- uniqueness of simple factors (composition factors)
- **krull-schmidt-theorem** -- uniqueness of indecomposable factors (direct factors)

# Source Reference

Chapter 6, p. 97, Example 6.30.

# Verification Notes

- Definition source: Direct from p. 97
- Confidence rationale: HIGH -- explicit comparison
- Uncertainties: None
