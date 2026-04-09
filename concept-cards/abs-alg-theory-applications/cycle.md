---
# === CORE IDENTIFICATION ===
concept: Cycle
slug: cycle

# === CLASSIFICATION ===
category: permutation-groups
subcategory: cycle-notation
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 74
section: "Cycle Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - k-cycle
  - cycle of length k

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - cycle-notation
  - disjoint-cycles
  - transposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cycle in a permutation group?"
  - "What is a k-cycle?"
---

# Quick Definition

A cycle of length $k$ is a permutation $\sigma$ that cyclically permutes $k$ elements $a_1, a_2, \ldots, a_k$ (sending $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_k \mapsto a_1$) and fixes all other elements. It is written $(a_1, a_2, \ldots, a_k)$.

# Core Definition

A permutation $\sigma \in S_X$ is a *cycle of length* $k$ if there exist elements $a_1, a_2, \ldots, a_k \in X$ such that $\sigma(a_1) = a_2$, $\sigma(a_2) = a_3$, ..., $\sigma(a_k) = a_1$, and $\sigma(x) = x$ for all other elements $x \in X$. The cycle is denoted $(a_1, a_2, \ldots, a_k)$ (Judson, p. 74).

# Prerequisites

- **Permutation** — A cycle is a special type of permutation

# Key Properties

1. A cycle of length $k$ has order $k$ in the group
2. Cycles are the building blocks of all permutations
3. The notation $(a_1, a_2, \ldots, a_k)$ is not unique: $(a_1, a_2, \ldots, a_k) = (a_2, a_3, \ldots, a_k, a_1)$
4. A cycle fixes all elements not listed in its notation
5. Not every permutation is a single cycle

# Construction / Recognition

## To Construct:
1. Choose $k$ elements from the set
2. Define the permutation that maps each to the next in sequence, with the last mapping back to the first
3. All other elements are fixed

## To Recognize:
1. Check that the permutation moves exactly $k$ elements in a single circular chain
2. All other elements must be fixed points

# Context & Application

Cycles provide a compact notation for permutations and are fundamental to understanding the structure of permutation groups. Every permutation decomposes into a product of disjoint cycles.

# Examples

**Example 1** (p. 74): The permutation $\sigma = (162354)$ in $S_7$ is a cycle of length 6. It maps $1 \mapsto 6 \mapsto 2 \mapsto 3 \mapsto 5 \mapsto 4 \mapsto 1$ and fixes 7.

**Example 2** (p. 74): The permutation $\tau = (243)$ is a cycle of length 3.

**Example 3** (p. 74): The permutation $(1243)(56)$ is not a single cycle; it is a product of a 4-cycle and a 2-cycle.

# Relationships

## Builds Upon
- **Permutation** — A cycle is a permutation with a specific structure

## Enables
- **Cycle Decomposition** — Every permutation decomposes into disjoint cycles
- **Transposition** — A transposition is a cycle of length 2
- **Disjoint Cycles** — The key structural building blocks of permutations

# Common Errors

- **Error**: Forgetting that elements not listed in cycle notation are fixed
  **Correction**: $(1 3 5)$ in $S_6$ fixes 2, 4, and 6

# Common Confusions

- **Confusion**: Thinking the cycle notation is unique
  **Clarification**: $(1, 2, 3) = (2, 3, 1) = (3, 1, 2)$ are all the same cycle

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, "Cycle Notation," pages 74-75.

# Verification Notes

- Definition source: Direct from p. 74
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
