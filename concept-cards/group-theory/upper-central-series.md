---
# === CORE IDENTIFICATION ===
concept: Upper Central Series
slug: upper-central-series

# === CLASSIFICATION ===
category: nilpotent-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 92
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ascending central series

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - center-of-group
  - commutator
extends: []
related:
  - nilpotent-group
  - nilpotency-class
  - lower-central-series
  - derived-series
contrasts_with:
  - derived-series
  - lower-central-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the upper central series relate to nilpotency?"
  - "What is the ascending central series?"
---

# Quick Definition

The upper central series is the ascending chain {1} subset Z(G) subset Z^2(G) subset ..., where Z^i(G)/Z^{i-1}(G) = Z(G/Z^{i-1}(G)). A group is nilpotent if and only if this series reaches G.

# Core Definition

Let G be a group. Define Z^0(G) = {1}, Z^1(G) = Z(G), and for i >= 1, Z^{i+1}(G) is the subgroup of G corresponding to Z(G/Z^i(G)) under the correspondence theorem. Thus:

g in Z^i(G) iff [g, x] in Z^{i-1}(G) for all x in G.

The sequence {1} subset Z(G) subset Z^2(G) subset ... is called the *upper central series* (or *ascending central series*) of G.

(Milne, p. 92)

# Prerequisites

- **center-of-group** -- Z(G) is the first term
- **commutator** -- membership is defined via commutator conditions

# Key Properties

1. Each Z^i(G) is a characteristic (hence normal) subgroup of G
2. Z^{i+1}(G)/Z^i(G) = Z(G/Z^i(G))
3. The series is ascending: {1} subset Z^1 subset Z^2 subset ...
4. G is nilpotent of class m iff Z^m(G) = G and Z^{m-1}(G) != G
5. For non-nilpotent groups, the series stabilizes without reaching G

# Context & Application

The upper central series is the canonical tool for measuring nilpotency. It is ascending (starts small, grows), in contrast to the derived series (which is descending). The derived series measures solvability; the upper central series measures nilpotency.

# Examples

**Example 1** (p. 92): For an abelian group, Z(G) = G, so the series reaches G in one step (class 1).

**Example 2** (p. 92, 6.12b): For the 3x3 unitriangular group, Z(G) consists of matrices with (1,3)-entry free and all others fixed. Then Z^2(G) = G, giving class 2.

# Relationships

## Builds Upon
- **center-of-group** -- the first step of the series

## Enables
- **nilpotent-group** -- defined by the termination of this series
- **nilpotency-class** -- the length of this series

## Contrasts With
- **derived-series** -- descending, measures solvability
- **lower-central-series** -- descending, also measures nilpotency

# Source Reference

Chapter 6, p. 92.

# Verification Notes

- Definition source: Direct from p. 92
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
