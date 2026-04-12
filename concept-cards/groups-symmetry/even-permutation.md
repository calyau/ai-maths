---
# === CORE IDENTIFICATION ===
concept: Even Permutation
slug: even-permutation

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
  - odd-permutation
  - alternating-group
contrasts_with:
  - odd-permutation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes even and odd permutations?"
  - "What is an even permutation?"
---

# Quick Definition

An even permutation is one that can be expressed as the product of an even number of transpositions, equivalently one with sign $+1$.

# Core Definition

"An element of $S_n$ which can be expressed as the product of an even number of transpositions is called an *even permutation*" (Armstrong, p. 36). The sign of an even permutation is $+1$. A cyclic permutation is even precisely when its length is odd.

# Prerequisites

- **Sign of a permutation** — An even permutation is defined as having sign $+1$
- **Transposition** — Even permutations are defined via transposition decomposition

# Key Properties

1. An even permutation has sign $+1$
2. The product of two even permutations is even
3. The inverse of an even permutation is even
4. The identity is even ($\varepsilon = (12)(12)$)
5. A $k$-cycle is even when $k$ is odd
6. Even permutations form the alternating group $A_n$

# Construction / Recognition

## To Recognize:
1. Write the permutation as a product of disjoint cycles
2. Count the number of even-length cycles
3. The permutation is even iff the number of even-length cycles is even

Alternatively:
1. Write the permutation as any product of transpositions
2. Count the transpositions; even count means even permutation

# Context & Application

The even permutations form the alternating group $A_n$, which has index 2 in $S_n$ and order $n!/2$. The alternating group plays a fundamental role in Galois theory and in the study of symmetry groups of Platonic solids (the rotational symmetry group of the dodecahedron is isomorphic to $A_5$).

# Examples

**Example** (p. 36): $(132)$ is even because its sign is $+1$.

**Example** (p. 37): The twelve even permutations in $A_4$ are: $\varepsilon$, $(12)(34)$, $(13)(24)$, $(14)(23)$, $(123)$, $(124)$, $(134)$, $(234)$, $(132)$, $(142)$, $(143)$, $(243)$.

# Relationships

## Builds Upon
- **Sign of a permutation** — Even permutations have sign $+1$

## Enables
- **Alternating group** — The set of even permutations forms $A_n$

## Contrasts With
- **Odd permutation** — Has sign $-1$

# Common Errors

- **Error**: Assuming a permutation written as a product of an even number of disjoint cycles is even.
  **Correction**: It is the total number of transpositions (not cycles) that matters. A product of two disjoint 2-cycles like $(12)(34)$ uses two transpositions, hence is even.

# Common Confusions

- **Confusion**: Thinking "even cycle" means the same as "even permutation."
  **Clarification**: An even-length cycle is an odd permutation. A $k$-cycle is even precisely when $k$ is odd.

# Source Reference

Chapter 6: Permutations, page 36 (pdf p. 36). Definition and relationship to cycle length.

# Verification Notes

- Definition: Direct quote from p. 36
- Confidence: HIGH — explicit definition
