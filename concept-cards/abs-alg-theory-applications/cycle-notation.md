---
# === CORE IDENTIFICATION ===
concept: Cycle Notation
slug: cycle-notation

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
pdf_page: 74
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
  - disjoint-cycles
  - cycle-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you write a permutation in cycle notation?"
  - "How do you multiply permutations in cycle notation?"
---

# Quick Definition

Cycle notation is a compact method for writing permutations as products of cycles, replacing the cumbersome two-row array notation. The identity permutation is denoted $(1)$.

# Core Definition

Cycle notation writes a permutation by listing its cycles. A cycle $(a_1, a_2, \ldots, a_k)$ means $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_k \mapsto a_1$. A permutation is written as a product of its disjoint cycles. "From this point forward we will find it convenient to use cycle notation to represent permutations. When using cycle notation, we often denote the identity permutation by $(1)$" (Judson, Remark 5.11, p. 76).

# Prerequisites

- **Cycle** — Cycle notation is built from cycles

# Key Properties

1. Every permutation can be written as a product of disjoint cycles
2. The identity permutation is written $(1)$
3. Fixed points are typically omitted from cycle notation
4. Products of cycles are computed right to left (following composition convention)
5. The representation as disjoint cycles is unique up to ordering of cycles and cyclic reordering within each cycle

# Construction / Recognition

## To Convert from Array to Cycle Notation:
1. Start with the first element; trace where it maps to, then where that maps to, etc., until returning to the start
2. Write these elements as a cycle
3. Pick the next element not yet accounted for and repeat
4. Continue until all elements are covered

# Context & Application

Cycle notation is far more compact and practical than array notation. It makes multiplication, computing inverses, and determining properties (like order and parity) much easier.

# Examples

**Example 1** (p. 74-76): The permutation $\begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 6 & 4 & 3 & 1 & 5 & 2 \end{pmatrix}$ is written as $(1624)$ in cycle notation (3 and 5 are fixed and omitted).

**Example 2** (p. 75): Computing products: if $\sigma = (1352)$ and $\tau = (256)$, then $\sigma\tau = (1356)$.

# Relationships

## Builds Upon
- **Cycle** — Notation is based on cycles

## Enables
- **Disjoint Cycles** — Permutations are expressed as products of disjoint cycles
- **Transposition** — A transposition is simply a 2-cycle

## Related
- **Permutation Composition** — Cycle notation simplifies computing products

# Common Errors

- **Error**: Applying cycles left to right instead of right to left
  **Correction**: Follow the right-to-left convention: in $\sigma\tau$, apply $\tau$ first

# Common Confusions

- **Confusion**: Thinking different cycle notations represent different permutations
  **Clarification**: $(1,2,3)$ and $(2,3,1)$ are the same cycle; also, the order of disjoint cycles does not matter

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, "Cycle Notation," pages 74-76, Remark 5.11.

# Verification Notes

- Definition source: Synthesized from pp. 74-76
- Confidence rationale: Extensively discussed with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
