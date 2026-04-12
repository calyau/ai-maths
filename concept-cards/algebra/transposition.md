---
concept: Transposition
slug: transposition
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.5 Permutations"
extraction_confidence: high
aliases:
  - "2-cycle"
prerequisites:
  - permutation
extends:
  - permutation
related:
  - sign-of-a-permutation
  - symmetric-group
contrasts_with: []
answers_questions:
  - "What is a permutation?"
---

# Quick Definition

A transposition is a permutation that swaps exactly two elements and fixes all others. In cycle notation, it is a 2-cycle such as (25). Every permutation can be written as a product of transpositions.

# Core Definition

2-cycles are called transpositions (Artin, p. 30). A transposition (ij) swaps i and j while fixing all other indices. Every permutation can be written as a product of transpositions in many ways; if a permutation is a product of k transpositions, k is always even or always odd (Artin, p. 33).

# Prerequisites

- **Permutation** — A transposition is a special permutation

# Key Properties

1. A transposition has order 2: applying it twice gives the identity
2. Every transposition has sign -1 (odd permutation)
3. Every permutation is a product of transpositions
4. The permutation matrix of a transposition is a Type (ii) elementary matrix

# Construction / Recognition

## To Construct:
1. Choose two distinct indices i, j
2. The transposition (ij) swaps i and j, fixes everything else

## To Recognize:
1. A permutation with exactly one 2-cycle and all other elements fixed

# Context & Application

Transpositions are the generators of the symmetric group: every permutation decomposes into transpositions. They correspond to Type (ii) elementary matrices (row interchanges).

# Examples

**Example 1** (p. 30): In the permutation (341)(25), the cycle (25) is a transposition swapping 2 and 5.

# Relationships

## Builds Upon
- **Permutation** — A transposition is a 2-cycle

## Enables
- **Sign of a permutation** — Each transposition contributes a factor of -1
- **Symmetric group** — Transpositions generate S_n

# Common Errors

- **Error**: Thinking (12)(13) = (123)
  **Correction**: (12)(13) = (132); composition must be done carefully

# Common Confusions

- **Confusion**: Confusing "transposition" (swapping two elements) with "transpose" (reflecting a matrix)
  **Clarification**: These are completely different operations sharing a linguistic root

# Source Reference

Chapter 1: Matrices, Section 1.5, page 30.

# Verification Notes

- Definition source: Direct from p. 30
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
