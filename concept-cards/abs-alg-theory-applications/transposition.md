---
# === CORE IDENTIFICATION ===
concept: Transposition
slug: transposition

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
pdf_page: 76
section: "Transpositions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - 2-cycle

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cycle
extends:
  - cycle
related:
  - even-permutation
  - odd-permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a transposition?"
  - "Can every permutation be written as a product of transpositions?"
---

# Quick Definition

A transposition is a cycle of length 2, i.e., a permutation that swaps exactly two elements and fixes all others. Every permutation can be written as a product of transpositions.

# Core Definition

"The simplest permutation is a cycle of length 2. Such cycles are called *transpositions*" (Judson, p. 76). Any cycle can be written as a product of transpositions: $(a_1, a_2, \ldots, a_n) = (a_1 a_n)(a_1 a_{n-1}) \cdots (a_1 a_3)(a_1 a_2)$.

# Prerequisites

- **Cycle** — A transposition is a special case of a cycle

# Key Properties

1. A transposition $(a\, b)$ swaps $a$ and $b$ and fixes everything else
2. A transposition is its own inverse: $(a\, b)^2 = \text{id}$
3. Every permutation can be written as a product of transpositions (Proposition 5.12)
4. The representation as a product of transpositions is not unique
5. However, the parity (even or odd number of transpositions) is an invariant

# Construction / Recognition

## To Express a Cycle as Transpositions:
1. $(a_1, a_2, \ldots, a_n) = (a_1\, a_n)(a_1\, a_{n-1}) \cdots (a_1\, a_2)$

## To Recognize:
1. The permutation swaps exactly two elements and fixes all others

# Context & Application

Transpositions are the generators of $S_n$: every permutation can be expressed as a product of transpositions. The number of transpositions needed (even vs. odd) determines the parity of the permutation, which is fundamental for defining the alternating group.

# Examples

**Example 1** (p. 76): $(16)(253) = (16)(23)(25) = (16)(45)(23)(45)(25)$. There is no unique way to represent a permutation as a product of transpositions.

**Example 2** (p. 76): The identity can be written as $(12)(12)$ or $(13)(24)(13)(24)$, always requiring an even number of transpositions.

# Relationships

## Builds Upon
- **Cycle** — A transposition is a 2-cycle

## Enables
- **Even Permutation** — Defined via even number of transpositions
- **Odd Permutation** — Defined via odd number of transpositions
- **Alternating Group** — The subgroup of even permutations

# Common Errors

- **Error**: Assuming the decomposition into transpositions is unique
  **Correction**: There are many ways to express a permutation as transpositions, but parity is always preserved

# Common Confusions

- **Confusion**: Thinking a transposition moves more than two elements
  **Clarification**: A transposition swaps exactly two elements; all others are fixed

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, "Transpositions," Proposition 5.12, pages 76-77.

# Verification Notes

- Definition source: Direct from p. 76
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
