---
concept: Parity of a Permutation
slug: parity-of-a-permutation
category: permutation-groups
subcategory: null
tier: foundational
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 77
section: "Transpositions"
extraction_confidence: high
aliases:
  - sign of a permutation
prerequisites:
  - transposition
  - even-permutation
  - odd-permutation
extends: []
related:
  - alternating-group
contrasts_with: []
answers_questions:
  - "How do I determine the parity of a permutation?"
  - "Is parity well-defined?"
---

# Quick Definition

The parity of a permutation is either even or odd, depending on whether it can be written as a product of an even or odd number of transpositions. This is well-defined: the parity is invariant regardless of which transposition decomposition is used.

# Core Definition

**Theorem 5.15:** "If a permutation $\sigma$ can be expressed as the product of an even number of transpositions, then any other product of transpositions equaling $\sigma$ must also contain an even number of transpositions. Similarly, if $\sigma$ can be expressed as the product of an odd number of transpositions, then any other product of transpositions equaling $\sigma$ must also contain an odd number of transpositions" (Judson, p. 77).

# Prerequisites

- **Transposition** — Parity counts transpositions
- **Even Permutation** — One of the two parities
- **Odd Permutation** — The other parity

# Key Properties

1. Well-defined: independent of the specific transposition decomposition (Theorem 5.15)
2. Proved via Lemma 5.14 (identity requires an even number of transpositions)
3. Product of two permutations of the same parity is even
4. Product of two permutations of different parity is odd
5. A $k$-cycle has parity $(k-1) \bmod 2$

# Construction / Recognition

## To Determine Parity:
1. Write $\sigma$ in disjoint cycle notation
2. For each $k$-cycle, it contributes $k - 1$ transpositions
3. Sum all contributions; if the total is even, $\sigma$ is even; otherwise odd

# Context & Application

The well-definedness of parity is a non-trivial result that enables the definition of the alternating group and the sign homomorphism $\text{sgn} : S_n \to \{+1, -1\}$.

# Examples

**Example 1** (p. 76): $(16)$ can be written as $(23)(16)(23)$ (3 transpositions, odd) or $(35)(16)(13)(16)(13)(35)(56)$ (7 transpositions, odd). The parity is always odd.

# Relationships

## Builds Upon
- **Transposition** — Parity counts transpositions
- **Even Permutation** / **Odd Permutation** — The two values

## Enables
- **Alternating Group** — Defined using parity

# Common Errors

- **Error**: Thinking a different decomposition could change the parity
  **Correction**: Theorem 5.15 guarantees parity is invariant

# Common Confusions

- **Confusion**: Confusing the parity of the cycle length with the parity of the permutation
  **Clarification**: A $k$-cycle has parity opposite to $k$: a 3-cycle is even, a 4-cycle is odd

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Lemma 5.14, Theorem 5.15, pages 76-77.

# Verification Notes

- Definition source: Direct from Theorem 5.15
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
