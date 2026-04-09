---
# === CORE IDENTIFICATION ===
concept: Odd Permutation
slug: odd-permutation

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
  - even-permutation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an odd permutation?"
---

# Quick Definition

A permutation is odd if it can be expressed as the product of an odd number of transpositions. An odd permutation is not in the alternating group.

# Core Definition

A permutation is *odd* "if it can be expressed as an odd number of transpositions" (Judson, p. 77). By Theorem 5.15, if a permutation can be expressed as an odd number of transpositions, then any other transposition decomposition of it also has an odd number of transpositions.

# Prerequisites

- **Transposition** — Odd permutations are defined via transpositions

# Key Properties

1. The product of two odd permutations is even
2. The product of an even and an odd permutation is odd
3. The inverse of an odd permutation is odd
4. A $k$-cycle is odd if and only if $k$ is even
5. In $S_n$ ($n \geq 2$), exactly half the permutations are odd (Proposition 5.17)

# Construction / Recognition

## To Determine:
1. Decompose the permutation into transpositions
2. If the count is odd, the permutation is odd

# Context & Application

Odd permutations form a coset of $A_n$ in $S_n$. They do not form a subgroup (the product of two odd permutations is even).

# Examples

**Example 1** (p. 76): The transposition $(16)$ is an odd permutation (it is itself a single transposition).

**Example 2**: Any 2-cycle, 4-cycle, or 6-cycle is an odd permutation.

# Relationships

## Builds Upon
- **Transposition** — Odd permutations are products of an odd number of transpositions

## Contrasts With
- **Even Permutation** — Even permutations use an even number of transpositions

## Related
- **Alternating Group** — $A_n$ excludes odd permutations

# Common Errors

- **Error**: Thinking a 4-cycle is even because 4 is even
  **Correction**: A 4-cycle requires 3 transpositions and is odd

# Common Confusions

- **Confusion**: Believing odd permutations form a subgroup
  **Clarification**: Odd permutations do not form a subgroup since their product is even

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Theorem 5.15, page 77.

# Verification Notes

- Definition source: Direct from p. 77
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
