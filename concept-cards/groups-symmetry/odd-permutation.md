---
# === CORE IDENTIFICATION ===
concept: Odd Permutation
slug: odd-permutation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: sign
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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sign-of-a-permutation
  - transposition
extends: []
related:
  - even-permutation
  - alternating-group
contrasts_with:
  - even-permutation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes even and odd permutations?"
  - "What is an odd permutation?"
---

# Quick Definition

An odd permutation is one that can only be expressed as the product of an odd number of transpositions, equivalently one with sign $-1$.

# Core Definition

The permutations that are not even are called *odd permutations* (Armstrong, p. 36). An odd permutation has sign $-1$ and can be expressed as the product of an odd number of transpositions. A cyclic permutation is odd precisely when its length is even. Every odd permutation can be written as an even permutation followed by the transposition $(12)$ (p. 37).

# Prerequisites

- **Sign of a permutation** — An odd permutation is defined as having sign $-1$
- **Transposition** — Odd permutations require an odd number of transpositions

# Key Properties

1. An odd permutation has sign $-1$
2. The product of two odd permutations is even
3. The product of an even and an odd permutation is odd
4. Every transposition is odd
5. A $k$-cycle is odd when $k$ is even
6. Exactly half of the elements of $S_n$ are odd (for $n \ge 2$)

# Construction / Recognition

## To Recognize:
1. Write the permutation in disjoint cycle form
2. Count the number of even-length cycles
3. The permutation is odd iff the number of even-length cycles is odd

# Context & Application

The odd permutations form a coset of $A_n$ in $S_n$ but do not form a subgroup (the product of two odd permutations is even, violating closure). The pairing between even and odd permutations via multiplication by $(12)$ shows that exactly half the elements of $S_n$ are odd.

# Examples

**Example** (p. 37): The twelve odd permutations in $S_4$ include all six transpositions $(12)$, $(13)$, $(14)$, $(23)$, $(24)$, $(34)$ and all six 4-cycles.

**Example**: The transposition $(12)$ is odd since it is the product of one transposition.

# Relationships

## Builds Upon
- **Sign of a permutation** — Odd permutations have sign $-1$

## Contrasts With
- **Even permutation** — Has sign $+1$

## Related
- **Alternating group** — $A_n$ is the complement of odd permutations in $S_n$

# Common Errors

- **Error**: Assuming the set of odd permutations forms a subgroup.
  **Correction**: Odd permutations do not form a subgroup because the product of two odd permutations is even, and the identity is even.

# Common Confusions

- **Confusion**: Thinking an odd-length cycle is an odd permutation.
  **Clarification**: An odd-length cycle is actually an even permutation. A $k$-cycle is odd when $k$ is even.

# Source Reference

Chapter 6: Permutations, pages 36-37 (pdf pp. 36-37).

# Verification Notes

- Definition: From p. 36
- Count: The pairing argument on p. 37 shows exactly half of $S_n$ is odd
- Confidence: HIGH — explicit in source
