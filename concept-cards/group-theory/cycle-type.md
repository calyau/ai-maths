---
# === CORE IDENTIFICATION ===
concept: Cycle Type
slug: cycle-type

# === CLASSIFICATION ===
category: group-actions
subcategory: permutation-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 67
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - partition type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cycle-notation
extends: []
related:
  - conjugacy-class
  - partition-of-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do conjugacy classes in S_n relate to cycle types?"
---

# Quick Definition

The cycle type of a permutation is the partition of $n$ given by the lengths of its disjoint cycles (including fixed points as 1-cycles).

# Core Definition

Each permutation $\sigma \in S_n$ determines a partition of $n$ from the sizes of its orbits. "Two elements $\sigma$ and $\tau$ of $S_n$ are conjugate if and only if they define the same partitions of $n$" (Milne, Proposition 4.30, p. 67).

# Prerequisites

- **Cycle notation** — Cycle type comes from the disjoint cycle decomposition

# Key Properties

1. Conjugacy classes in $S_n$ are in bijection with partitions of $n$
2. Two permutations are conjugate iff they have the same cycle type (Proposition 4.30)
3. To conjugate: $g(i_1 \ldots i_r)g^{-1} = (g(i_1) \ldots g(i_r))$ (Example 4.29)

# Examples

**Example 1** (p. 66): $(15)(27634)(8) \in S_8$ has cycle type $1, 2, 5$ (partition of 8).

**Example 2** (p. 68): $S_4$ has five conjugacy classes corresponding to partitions: $1{+}1{+}1{+}1$, $1{+}1{+}2$, $1{+}3$, $2{+}2$, $4$, with sizes 1, 6, 8, 3, 6.

# Relationships

## Builds Upon
- **cycle-notation**

## Enables
- Determining conjugacy classes in $S_n$

## Related
- **conjugacy-class** — Conjugacy classes in $S_n$ = cycle types

# Source Reference

Chapter 4: Groups Acting on Sets, "Permutation groups", Proposition 4.30, page 67.

# Verification Notes

- Definition source: Proposition 4.30, p. 67
- Confidence: HIGH — explicit theorem
- Uncertainties: None
