---
# === CORE IDENTIFICATION ===
concept: Disjoint Cycle Decomposition
slug: disjoint-cycle-decomposition

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
  - "decomposition into disjoint cycles"
  - "cycle decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cyclic-permutation
  - cycle-notation
extends: []
related:
  - transposition
  - sign-of-a-permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a permutation into disjoint cycles?"
  - "Is the disjoint cycle decomposition unique?"
  - "Why do disjoint cycles commute?"
---

# Quick Definition

Every element of $S_n$ can be written uniquely (up to ordering) as a product of disjoint cyclic permutations. Disjoint cycles commute with each other.

# Core Definition

Armstrong shows that "every element of $S_n$ may be written as a product of disjoint cyclic permutations, disjoint in the sense that no integer is moved by more than one of them" (p. 34). The decomposition is obtained by following the cycle notation algorithm. Furthermore, "the decomposition of an element of $S_n$ as a product of disjoint cyclic permutations is unique up to the order in which we write down these cyclic permutations" (p. 34).

# Prerequisites

- **Cyclic permutation** — The decomposition expresses a permutation as a product of cyclic permutations
- **Cycle notation** — The procedure for obtaining the decomposition

# Key Properties

1. Every permutation decomposes into disjoint cyclic permutations
2. Two cycles are disjoint if no integer is moved by both
3. Disjoint cycles commute: if $\alpha$ and $\beta$ are disjoint then $\alpha\beta = \beta\alpha$ (p. 34)
4. The decomposition is unique up to the order of the cycles
5. The order of the permutation is the lcm of the cycle lengths (Exercise 6.12)

# Construction / Recognition

## To Decompose a Permutation:
1. Start with the smallest integer moved by the permutation
2. Follow its orbit: write its image, the image of that, etc., until returning to the start
3. This gives the first cycle
4. Find the next smallest moved integer not yet used
5. Repeat until all moved integers are accounted for
6. The product of these cycles is the disjoint cycle decomposition

# Context & Application

Disjoint cycle decomposition is the canonical form for elements of $S_n$. It reveals the cycle type of a permutation at a glance, from which one can immediately read off the order (lcm of cycle lengths), the sign (even iff the number of even-length cycles is even), and the conjugacy class.

# Examples

**Example** (p. 33): The permutation
$$\begin{bmatrix} 123456 \\ 543612 \end{bmatrix}$$
decomposes as $(15)(246)$, with 3 fixed.

**Example** (p. 34): The permutation $(2856)(394)$ consists of two disjoint cycles: $(2856)$ affects only 2, 5, 6, 8 and $(394)$ moves only 3, 4, 9.

# Relationships

## Builds Upon
- **Cyclic permutation** — Each factor in the decomposition is a cyclic permutation
- **Cycle notation** — The notation directly produces the decomposition

## Enables
- **Sign of a permutation** — Computed from the cycle structure
- **Order of a permutation** — The lcm of cycle lengths

## Contrasts With
- **Transposition decomposition** — Decomposition into transpositions is not unique and transpositions need not be disjoint

# Common Errors

- **Error**: Including fixed elements as 1-cycles in the decomposition.
  **Correction**: By convention, fixed elements are omitted from cycle notation. Armstrong's algorithm only lists elements that are moved.

# Common Confusions

- **Confusion**: Confusing disjoint cycle decomposition (unique) with transposition decomposition (not unique).
  **Clarification**: The disjoint cycle decomposition is canonical and unique up to cycle order. The decomposition into transpositions is neither unique nor uses disjoint factors.

# Source Reference

Chapter 6: Permutations, page 34 (pdf p. 34). Uniqueness and commutativity stated in the paragraph following the examples.

# Verification Notes

- Definition: Synthesized from pp. 33-34
- Uniqueness and commutativity: Explicit on p. 34
- Confidence: HIGH — clearly described with examples
