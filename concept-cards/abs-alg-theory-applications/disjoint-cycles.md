---
# === CORE IDENTIFICATION ===
concept: Disjoint Cycles
slug: disjoint-cycles

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
pdf_page: 75
section: "Cycle Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cycle
extends: []
related:
  - cycle-decomposition
  - cycle-notation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are disjoint cycles?"
  - "Do disjoint cycles commute?"
---

# Quick Definition

Two cycles $\sigma = (a_1, \ldots, a_k)$ and $\tau = (b_1, \ldots, b_l)$ are disjoint if they move completely different elements: $a_i \neq b_j$ for all $i$ and $j$. Disjoint cycles always commute.

# Core Definition

Two cycles in $S_X$, $\sigma = (a_1, a_2, \ldots, a_k)$ and $\tau = (b_1, b_2, \ldots, b_l)$, are **disjoint** if $a_i \neq b_j$ for all $i$ and $j$ (Judson, p. 75). The product of disjoint cycles cannot be simplified further, unlike the product of non-disjoint cycles.

# Prerequisites

- **Cycle** — Disjointness is a property of pairs of cycles

# Key Properties

1. Disjoint cycles commute: $\sigma\tau = \tau\sigma$ (Proposition 5.8, p. 75)
2. The product of disjoint cycles cannot be simplified
3. Every permutation can be written uniquely as a product of disjoint cycles (Theorem 5.9)
4. The order of a product of disjoint cycles is the lcm of their lengths

# Construction / Recognition

## To Recognize:
1. List the elements moved by each cycle
2. If no element appears in more than one cycle, the cycles are disjoint

# Context & Application

Disjoint cycle decomposition is the canonical form for permutations. Since disjoint cycles commute, their order in the product does not matter, and properties like the order of the permutation can be read directly from the cycle lengths.

# Examples

**Example 1** (p. 75): The cycles $(135)$ and $(27)$ are disjoint, so $(135)(27) = (27)(135)$.

**Example 2** (p. 75): The cycles $(135)$ and $(347)$ are not disjoint (they share element 3), and $(135)(347) = (13475)$.

# Relationships

## Builds Upon
- **Cycle** — Disjointness is defined for cycles

## Enables
- **Cycle Decomposition** — Every permutation decomposes into disjoint cycles

## Related
- **Cycle Notation** — Disjoint cycle decomposition is the standard representation

# Common Errors

- **Error**: Trying to simplify a product of disjoint cycles into a single cycle
  **Correction**: Disjoint cycles cannot be combined; they are already in simplest form

# Common Confusions

- **Confusion**: Thinking the order of disjoint cycles matters
  **Clarification**: Disjoint cycles commute, so their order in the product is irrelevant

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Proposition 5.8, pages 75-76.

# Verification Notes

- Definition source: Direct from p. 75
- Confidence rationale: Explicit definition and theorem
- Uncertainties: None
- Cross-reference status: Verified
