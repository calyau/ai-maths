---
# === CORE IDENTIFICATION ===
concept: Cycle Notation
slug: cycle-notation

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
pdf_page: 65
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cycle decomposition
  - disjoint cycle decomposition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation-group
extends: []
related:
  - cycle-type
  - transposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is cycle notation for permutations?"
---

# Quick Definition

A cycle $(i_1 i_2 \ldots i_r)$ is the permutation $i_1 \mapsto i_2 \mapsto \cdots \mapsto i_r \mapsto i_1$ (fixing all other elements). Every permutation decomposes uniquely into disjoint cycles.

# Core Definition

"A cycle is a permutation of the form $i_1 \mapsto i_2 \mapsto \cdots \mapsto i_r \mapsto i_1$, remaining $i$'s fixed. ... We denote this cycle by $(i_1 i_2 \ldots i_r)$, and call $r$ its length" (Milne, p. 65). "Every permutation can be written (in essentially one way) as a product of disjoint cycles" (Proposition 4.26).

# Prerequisites

- **Permutation group** — Cycles are elements of $S_n$

# Key Properties

1. A cycle of length $r$ has order $r$ in $S_n$
2. A cycle of length 2 is a transposition
3. Disjoint cycles commute
4. The order of a product of disjoint cycles is the lcm of their lengths
5. The decomposition into disjoint cycles is unique (up to ordering and starting point)
6. The support of $(i_1 \ldots i_r)$ is $\{i_1, \ldots, i_r\}$

# Construction / Recognition

## To decompose a permutation into cycles:
1. Start with any element $i$; follow $i \mapsto \sigma(i) \mapsto \sigma^2(i) \mapsto \cdots$ until returning to $i$
2. This gives one cycle; repeat with an element not yet seen
3. The orbits of $\langle \sigma \rangle$ correspond to the cycles

# Examples

**Example 1** (p. 66): $\begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 5 & 7 & 4 & 2 & 1 & 3 & 6 & 8 \end{pmatrix} = (15)(27634)(8)$, with order $\operatorname{lcm}(2, 5) = 10$.

# Relationships

## Builds Upon
- **permutation-group**

## Enables
- **cycle-type** — The multiset of cycle lengths
- **sign-of-permutation** — An $r$-cycle has sign $(-1)^{r-1}$

# Source Reference

Chapter 4: Groups Acting on Sets, "Permutation groups", Proposition 4.26, pages 65-66.

# Verification Notes

- Definition source: Direct from pp. 65-66
- Confidence: HIGH — explicit definition and theorem
- Uncertainties: None
