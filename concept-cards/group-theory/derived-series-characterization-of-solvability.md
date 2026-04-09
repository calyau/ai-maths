---
# === CORE IDENTIFICATION ===
concept: Derived Series Characterization of Solvability
slug: derived-series-characterization-of-solvability

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 91
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
  - derived-series
  - commutator-subgroup
extends: []
related:
  - solvable-length
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine whether a group is solvable?"
  - "How does the derived series relate to solvability?"
---

# Quick Definition

A group G is solvable if and only if G^(k) = {1} for some k, where G^(k) is the kth derived subgroup. The proof: if G^(k) = 1, the derived series is a solvable series. Conversely, for any solvable series G > G_1 > ... > G_s = 1, one shows G^(i) subset G_i by induction (since G_i/G_{i+1} abelian implies G^(i+1) subset G_{i+1}).

# Core Definition

**Proposition 6.10.** A group G is solvable if and only if its kth derived subgroup G^(k) = 1 for some k.

Moreover, the derived series is the shortest solvable series: if G > G_1 > ... > G_s = 1 is any solvable series, then G^(i) subset G_i for all i, and hence G^(s) = 1.

(Milne, Proposition 6.10, pp. 91-92)

# Prerequisites

- **solvable-group** -- the property being characterized
- **derived-series** -- the canonical solvable series
- **commutator-subgroup** -- each step of the derived series

# Key Properties

1. The derived series provides a canonical, computable test for solvability
2. The derived series is the shortest solvable series
3. G^(i) subset G_i for any solvable series, proved by induction using: G_{i-1}/G_i abelian implies G^(i) subset G_i

# Context & Application

This is the standard method for testing solvability in practice: compute G, G', G'', ... and check if you reach {1}. For matrix groups, this often reduces to computing commutator subgroups, which can be done explicitly.

# Relationships

## Builds Upon
- **derived-series** -- the series being tested

## Enables
- **solvable-length** -- the smallest k with G^(k) = 1

# Source Reference

Chapter 6, Proposition 6.10, pp. 91-92.

# Verification Notes

- Definition source: Direct from Proposition 6.10
- Confidence rationale: HIGH -- explicit proposition with proof
- Uncertainties: None
