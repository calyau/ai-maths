---
# === CORE IDENTIFICATION ===
concept: Solvable Length
slug: solvable-length

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
pdf_page: 92
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - derived length

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
  - derived-series
extends: []
related:
  - nilpotency-class
contrasts_with:
  - nilpotency-class

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the solvable length of a group?"
---

# Quick Definition

The solvable length of a solvable group G is the length of its derived series, i.e., the smallest k such that G^(k) = {1}. It is the minimum length of any solvable series for G.

# Core Definition

A solvable group G has a canonical solvable series, the derived series, in which all the groups are normal in G. The derived series is the shortest solvable series for G. Its length is called the *solvable length* of G.

(Milne, p. 92)

# Prerequisites

- **solvable-group** -- solvable length is defined only for solvable groups
- **derived-series** -- the solvable length is the length of this series

# Key Properties

1. Solvable length 0: only the trivial group
2. Solvable length 1: abelian groups
3. Solvable length 2: metabelian groups (G' is abelian)
4. The derived series achieves the minimum length among all solvable series

# Examples

**Example 1**: S_3 has solvable length 2 (derived series S_3 > C_3 > 1).
**Example 2**: S_4 has solvable length 3 (derived series S_4 > A_4 > V > 1).

# Relationships

## Builds Upon
- **derived-series** -- the length of the derived series

## Contrasts With
- **nilpotency-class** -- measures nilpotency; solvable length measures solvability

# Source Reference

Chapter 6, p. 92.

# Verification Notes

- Definition source: Direct from p. 92
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
