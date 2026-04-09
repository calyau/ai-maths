---
# === CORE IDENTIFICATION ===
concept: Cycle Decomposition
slug: cycle-decomposition

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
aliases:
  - disjoint cycle decomposition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cycle
  - disjoint-cycles
extends: []
related:
  - cycle-notation
  - even-permutation
  - odd-permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a permutation into disjoint cycles?"
  - "Can every permutation be written as a product of disjoint cycles?"
---

# Quick Definition

Every permutation in $S_n$ can be written uniquely as a product of disjoint cycles. This decomposition reveals the structure of the permutation and determines its order.

# Core Definition

"Every permutation in $S_n$ can be written as the product of disjoint cycles" (Judson, Theorem 5.9, p. 75). The decomposition is obtained by tracing orbits: start with element 1, follow $\sigma(1), \sigma^2(1), \ldots$ until returning, forming the first cycle; then proceed with the next unvisited element.

# Prerequisites

- **Cycle** — Decomposition produces cycles
- **Disjoint Cycles** — The resulting cycles are disjoint

# Key Properties

1. Every permutation has a unique disjoint cycle decomposition (up to order of cycles and cyclic reordering within each cycle)
2. The order of a permutation equals the lcm of its cycle lengths
3. Fixed points correspond to 1-cycles (usually omitted from notation)

# Construction / Recognition

## To Decompose a Permutation $\sigma$:
1. Start with element 1; compute $\sigma(1), \sigma^2(1), \ldots$ until returning to 1 — this gives the first cycle
2. Take the smallest element not yet in any cycle; trace its orbit to form the next cycle
3. Repeat until all elements are accounted for
4. Write the permutation as the product of these disjoint cycles

# Context & Application

The cycle decomposition is the standard canonical form for permutations. It immediately reveals the permutation's order (lcm of cycle lengths), parity (sum of cycle lengths minus number of cycles), and conjugacy class.

# Examples

**Example 1** (p. 76): $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 6 & 4 & 3 & 1 & 5 & 2 \end{pmatrix} = (1624)$ and $\tau = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 3 & 2 & 1 & 5 & 6 & 4 \end{pmatrix} = (13)(456)$.

# Relationships

## Builds Upon
- **Cycle** — The decomposition is into cycles
- **Disjoint Cycles** — The cycles in the decomposition are disjoint

## Enables
- **Even Permutation** — Parity is determined from cycle decomposition
- **Odd Permutation** — Parity is determined from cycle decomposition

# Common Errors

- **Error**: Including fixed points as separate 1-cycles in the notation
  **Correction**: By convention, 1-cycles are omitted (though including them is not wrong, just verbose)

# Common Confusions

- **Confusion**: Thinking the order of cycles in the product matters
  **Clarification**: Since the cycles are disjoint, they commute, so order is irrelevant

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Theorem 5.9, Example 5.10, pages 75-76.

# Verification Notes

- Definition source: Direct from Theorem 5.9, p. 75
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
