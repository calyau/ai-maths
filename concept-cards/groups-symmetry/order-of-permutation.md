---
# === CORE IDENTIFICATION ===
concept: Order of a Permutation
slug: order-of-permutation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: properties
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Permutations"
chapter_number: 6
pdf_page: 33
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - disjoint-cycle-decomposition
extends: []
related:
  - k-cycle
  - cyclic-permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find the order of a permutation?"
  - "What determines the order of a permutation?"
---

# Quick Definition

The order of a permutation is the least common multiple of the lengths of its disjoint cycles.

# Core Definition

Exercise 6.12 states: "Prove that the order of an element $\alpha$ of $S_n$ is the least common multiple of the lengths of the cycles which are obtained when $\alpha$ is written as a product of disjoint cyclic permutations" (Armstrong, p. 38). This follows because disjoint cycles commute: $\alpha^k = \varepsilon$ precisely when $k$ is a multiple of each cycle length, and the smallest such $k$ is $\text{lcm}$ of the cycle lengths.

# Prerequisites

- **Disjoint cycle decomposition** — The order depends on the cycle structure

# Key Properties

1. Order of $\alpha$ = $\text{lcm}$ of disjoint cycle lengths
2. A $k$-cycle has order $k$
3. The identity has order 1
4. If $\alpha = (a_1 \ldots a_{k_1})(b_1 \ldots b_{k_2}) \cdots$, then $|\alpha| = \text{lcm}(k_1, k_2, \ldots)$

# Construction / Recognition

## To Find the Order:
1. Write the permutation in disjoint cycle form
2. Record the length of each cycle
3. Compute the least common multiple of the lengths

# Context & Application

The order of a permutation is essential for understanding the structure of $S_n$. It determines when repeated application of a permutation returns to the identity, and is used in computing subgroup orders and studying group actions.

# Examples

**Example**: The permutation $(12)(345) \in S_5$ has order $\text{lcm}(2, 3) = 6$.

**Example**: A transposition has order 2. A 3-cycle has order 3. The permutation $(12)(34)$ has order $\text{lcm}(2, 2) = 2$.

# Relationships

## Builds Upon
- **Disjoint cycle decomposition** — Determines the cycle lengths

## Related
- **k-cycle** — A $k$-cycle has order $k$

# Common Errors

- **Error**: Multiplying cycle lengths instead of taking lcm.
  **Correction**: The order is the lcm, not the product. $(12)(34)$ has order $\text{lcm}(2,2) = 2$, not $4$.

# Common Confusions

- **Confusion**: Thinking the order equals the number of elements moved.
  **Clarification**: The order depends on the cycle structure, not simply on how many elements are moved.

# Source Reference

Chapter 6: Permutations, Exercise 6.12, page 38 (pdf p. 38).

# Verification Notes

- Statement: Exercise 6.12
- Confidence: MEDIUM — stated as exercise without proof; standard result
