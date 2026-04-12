---
# === CORE IDENTIFICATION ===
concept: Cycle Notation
slug: cycle-notation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: notation
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
  - "cycle representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
  - symmetric-group
extends: []
related:
  - cyclic-permutation
  - disjoint-cycle-decomposition
  - transposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a permutation in cycle notation?"
  - "How do I read cycle notation?"
---

# Quick Definition

Cycle notation is a compact way to write a permutation by grouping elements into cycles, where each element maps to the next element in its cycle.

# Core Definition

A permutation is written in cycle notation by the following procedure (Armstrong, p. 33): "Open a pair of brackets, then write down the smallest integer which is moved by the given permutation. Now, list the image of this integer under the permutation, followed by its image and so on, eventually closing the brackets at the stage where we would come full circle to our starting point. Open a new pair of brackets, list the smallest integer which has so far not been mentioned and which is moved by the permutation, etc." Integers fixed by the permutation need not be mentioned.

# Prerequisites

- **Permutation** — Cycle notation represents permutations
- **Symmetric group** — Cycle notation is used for elements of $S_n$

# Key Properties

1. Inside each pair of brackets, an integer is sent to the integer following it
2. The final integer in a cycle is sent to the first integer
3. Integers left fixed by the permutation are not mentioned
4. The decomposition into disjoint cycles is unique up to ordering of cycles
5. Disjoint cycles commute with one another

# Construction / Recognition

## To Convert from Two-Row Notation:
1. Start with the smallest integer moved by the permutation
2. Follow the chain of images until returning to the start; write as $(a_1 a_2 \ldots a_k)$
3. Find the next smallest integer not yet mentioned that is moved
4. Repeat until all moved integers are accounted for

## To Read Cycle Notation:
1. Within each cycle $(a_1 a_2 \ldots a_k)$: $a_1 \mapsto a_2$, $a_2 \mapsto a_3$, ..., $a_k \mapsto a_1$
2. Any integer not appearing in any cycle is fixed

# Context & Application

Cycle notation is far more compact than two-row notation, especially for large $n$. It makes the cycle structure of a permutation immediately visible, which is essential for determining properties like order, sign, and conjugacy class.

# Examples

**Example** (p. 33): The permutation
$$\begin{bmatrix} 123456 \\ 543612 \end{bmatrix}$$
becomes $(15)(246)$ in cycle notation. The integer 3 is not mentioned because it is fixed.

**Example** (p. 34): The elements of $S_3$ in cycle notation are $\varepsilon$, $(12)$, $(13)$, $(23)$, $(123)$, $(132)$.

**Example** (p. 34): $(12)(23) = (123)$, whereas $(23)(12) = (132)$.

# Relationships

## Builds Upon
- **Permutation** — Cycle notation is a way of writing permutations

## Enables
- **Cyclic permutation** — A single cycle defines a cyclic permutation
- **Disjoint cycle decomposition** — Every permutation decomposes into disjoint cycles
- **Sign of a permutation** — Determined from the cycle structure

## Related
- **Transposition** — A 2-cycle in cycle notation

# Common Errors

- **Error**: Forgetting that the last element in a cycle maps back to the first.
  **Correction**: $(a_1 a_2 \ldots a_k)$ means $a_k \mapsto a_1$.

- **Error**: Multiplying cycles left-to-right when the convention is right-to-left.
  **Correction**: In Armstrong's convention, $\alpha\beta$ means apply $\beta$ first. So in $(12)(23)$, apply $(23)$ first.

# Common Confusions

- **Confusion**: Thinking the decomposition into transpositions is unique.
  **Clarification**: The decomposition into disjoint cycles is unique, but decomposition into transpositions is not (Theorem 6.1).

# Source Reference

Chapter 6: Permutations, pages 33-34 (pdf pp. 33-34). Algorithm for writing cycle notation described on p. 33.

# Verification Notes

- Definition: Direct quote of the procedure from p. 33
- Examples: Directly from source text
- Confidence: HIGH — explicit procedural description in source
