---
# === CORE IDENTIFICATION ===
concept: Cyclic Permutation
slug: cyclic-permutation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: cycle-structure
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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cycle"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
  - cycle-notation
extends: []
related:
  - k-cycle
  - transposition
  - disjoint-cycle-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic permutation?"
  - "How does a cyclic permutation act on elements?"
---

# Quick Definition

A cyclic permutation $(a_1 a_2 \ldots a_k)$ sends $a_1$ to $a_2$, $a_2$ to $a_3$, ..., $a_{k-1}$ to $a_k$, and $a_k$ to $a_1$, leaving all other integers fixed.

# Core Definition

"A permutation $(a_1 a_2 \ldots a_k)$ inside a single pair of brackets is called a *cyclic permutation*. It sends $a_1$ to $a_2$, $a_2$ to $a_3$, ..., $a_{k-1}$ to $a_k$ and $a_k$ to $a_1$, leaving all other integers fixed. The number $k$ is its length" (Armstrong, p. 34).

# Prerequisites

- **Permutation** — A cyclic permutation is a special type of permutation
- **Cycle notation** — Cyclic permutations are expressed using cycle notation

# Key Properties

1. A cyclic permutation of length $k$ moves exactly $k$ elements cyclically
2. All elements not in the cycle are left fixed
3. A cyclic permutation of length $k$ has order $k$
4. A cyclic permutation is even precisely when its length is odd (p. 36)
5. Every permutation can be written as a product of disjoint cyclic permutations
6. Every cyclic permutation can be written as a product of transpositions: $(a_1 a_2 \ldots a_k) = (a_1 a_k) \ldots (a_1 a_3)(a_1 a_2)$

# Construction / Recognition

## To Construct:
1. Choose $k$ elements $a_1, a_2, \ldots, a_k$ from $\{1, \ldots, n\}$
2. Define the permutation: $a_i \mapsto a_{i+1}$ for $i < k$, and $a_k \mapsto a_1$
3. Fix all elements not in $\{a_1, \ldots, a_k\}$

## To Recognize:
1. Write the permutation in cycle notation
2. If it consists of a single cycle, it is a cyclic permutation

# Context & Application

Cyclic permutations are the building blocks for all permutations, since every element of $S_n$ decomposes uniquely into disjoint cyclic permutations. The cycle structure (lengths of cycles) determines important properties such as the order and sign of the permutation.

# Examples

**Example** (p. 34): $(123)$ is a cyclic permutation of length 3 in $S_3$. It sends $1 \to 2$, $2 \to 3$, $3 \to 1$.

**Example** (p. 33): $(15)(246)$ represents the permutation as a product of a 2-cycle and a 3-cycle, each of which is a cyclic permutation.

# Relationships

## Builds Upon
- **Permutation** — A cyclic permutation is a permutation with a single cycle

## Enables
- **Disjoint cycle decomposition** — Every permutation is a product of disjoint cyclic permutations
- **Sign of a permutation** — The sign depends on cycle lengths

## Related
- **k-cycle** — A cyclic permutation of length $k$
- **Transposition** — A cyclic permutation of length 2

# Common Errors

- **Error**: Confusing the cyclic permutation $(a_1 a_2 \ldots a_k)$ with $(a_2 a_3 \ldots a_k a_1)$.
  **Correction**: These are the same cyclic permutation written with a different starting point. For example, $(123) = (231) = (312)$.

# Common Confusions

- **Confusion**: Thinking a cyclic permutation must move all elements.
  **Clarification**: A cyclic permutation fixes all elements not in the cycle. Only the $k$ elements in the cycle are moved.

# Source Reference

Chapter 6: Permutations, page 34 (pdf p. 34). Definition in the paragraph following Example (iv).

# Verification Notes

- Definition: Direct quote from p. 34
- Decomposition formula: Explicit in Theorem 6.1 proof, p. 35
- Parity result: Explicit on p. 36
- Confidence: HIGH — explicit definition in source
