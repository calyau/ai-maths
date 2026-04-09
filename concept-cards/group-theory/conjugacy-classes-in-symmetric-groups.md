---
# === CORE IDENTIFICATION ===
concept: Conjugacy Classes in Symmetric Groups
slug: conjugacy-classes-in-symmetric-groups

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - cycle-type
extends:
  - conjugacy-class
related:
  - partition-of-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine the conjugacy classes of S_n?"
---

# Quick Definition

Two permutations in $S_n$ are conjugate if and only if they have the same cycle type (partition of $n$). Thus conjugacy classes in $S_n$ are in bijection with partitions of $n$.

# Core Definition

"Two elements $\sigma$ and $\tau$ of $S_n$ are conjugate if and only if they define the same partitions of $n$" (Milne, Proposition 4.30, p. 67). The conjugation formula is $g(i_1 \ldots i_k)g^{-1} = (g(i_1) \ldots g(i_k))$ (Example 4.29).

# Prerequisites

- **Conjugacy class** — These are the conjugacy classes being classified
- **Cycle type** — The invariant that characterizes conjugacy

# Key Properties

1. Conjugacy classes in $S_n$ $\leftrightarrow$ partitions of $n$
2. The number of $k$-cycles in $S_n$ is $\frac{n(n-1)\cdots(n-k+1)}{k}$ (Remark 4.32)
3. Computing class sizes requires care when the partition has repeated parts
4. For $S_4$: five classes with sizes 1, 6, 8, 3, 6

# Examples

**Example 1** (p. 68): $S_4$ conjugacy classes:

| Partition | Representative | Size | Parity |
|-----------|---------------|------|--------|
| $1+1+1+1$ | $1$ | 1 | even |
| $1+1+2$ | $(ab)$ | 6 | odd |
| $1+3$ | $(abc)$ | 8 | even |
| $2+2$ | $(ab)(cd)$ | 3 | even |
| $4$ | $(abcd)$ | 6 | odd |

**Example 2** (p. 67): The number of permutations of type $(ab)(cd)$ in $S_4$ is $\frac{1}{2}\left(\frac{4 \cdot 3}{2} \cdot \frac{2 \cdot 1}{2}\right) = 3$.

# Relationships

## Builds Upon
- **conjugacy-class**, **cycle-type**

## Enables
- Analysis of normal subgroups of $S_n$ (a normal subgroup is a union of conjugacy classes)

# Source Reference

Chapter 4: Groups Acting on Sets, "Permutation groups", Proposition 4.30, pages 67-68.

# Verification Notes

- Definition source: Proposition 4.30, p. 67
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
