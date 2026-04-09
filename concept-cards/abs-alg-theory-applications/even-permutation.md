---
# === CORE IDENTIFICATION ===
concept: Even Permutation
slug: even-permutation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 77
section: "Transpositions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transposition
extends: []
related:
  - alternating-group
contrasts_with:
  - odd-permutation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an even permutation?"
  - "How do I determine the parity of a permutation?"
---

# Quick Definition

A permutation is even if it can be expressed as the product of an even number of transpositions. The parity is well-defined: a permutation cannot be written as both an even and odd number of transpositions.

# Core Definition

"We define a permutation to be *even* if it can be expressed as an even number of transpositions" (Judson, p. 77). This is well-defined by Theorem 5.15: if a permutation can be expressed as an even number of transpositions, then any other product of transpositions equaling it must also contain an even number.

# Prerequisites

- **Transposition** — Even permutations are defined via transpositions

# Key Properties

1. The product of two even permutations is even
2. The inverse of an even permutation is even
3. The identity is an even permutation
4. A $k$-cycle is even if and only if $k$ is odd
5. The set of even permutations forms a subgroup (the alternating group)

# Construction / Recognition

## To Determine Parity:
1. Write the permutation as a product of transpositions (any decomposition)
2. Count the number of transpositions
3. If even, the permutation is even

## Alternative Method:
1. Write the permutation in disjoint cycle notation
2. A $k$-cycle requires $k-1$ transpositions
3. Sum $(k_i - 1)$ over all cycles; if the sum is even, the permutation is even

# Context & Application

The even/odd classification partitions $S_n$ into two equal halves and defines the alternating group $A_n$. Parity is preserved under composition and taking inverses.

# Examples

**Example 1** (p. 78): The even permutations in $S_4$ forming $A_4$ are: $(1)$, $(12)(34)$, $(13)(24)$, $(14)(23)$, $(123)$, $(132)$, $(124)$, $(142)$, $(134)$, $(143)$, $(234)$, $(243)$.

# Relationships

## Builds Upon
- **Transposition** — Even permutations are defined as products of an even number of transpositions

## Enables
- **Alternating Group** — $A_n$ consists of all even permutations

## Contrasts With
- **Odd Permutation** — An odd permutation requires an odd number of transpositions

# Common Errors

- **Error**: Thinking a 3-cycle is odd because 3 is odd
  **Correction**: A 3-cycle requires 2 transpositions, so it is even (a $k$-cycle is even when $k$ is odd)

# Common Confusions

- **Confusion**: Believing the specific transposition decomposition determines parity
  **Clarification**: Any decomposition gives the same parity (Theorem 5.15)

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Theorem 5.15, Lemma 5.14, pages 76-78.

# Verification Notes

- Definition source: Direct from p. 77
- Confidence rationale: Explicit definition with supporting theorem
- Uncertainties: None
- Cross-reference status: Verified
