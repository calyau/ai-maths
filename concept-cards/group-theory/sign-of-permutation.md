---
# === CORE IDENTIFICATION ===
concept: Sign of a Permutation
slug: sign-of-permutation

# === CLASSIFICATION ===
category: group-actions
subcategory: permutation-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 64
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - signature
  - parity of a permutation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation-group
  - transposition
extends: []
related:
  - alternating-group
  - cycle-notation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the sign (parity) of a permutation?"
  - "How do I determine if a permutation is even or odd?"
---

# Quick Definition

The sign (or signature) of a permutation $\sigma$ is $+1$ if $\sigma$ is a product of an even number of transpositions, and $-1$ if odd.

# Core Definition

"The ordered pairs $(i, j)$ with $i < j$ and $\sigma(i) > \sigma(j)$ are called the inversions of $\sigma$, and $\sigma$ is said to be even or odd according as the number of its inversions is even or odd. The signature, $\operatorname{sign}(\sigma)$, of $\sigma$ is $+1$ or $-1$ according as $\sigma$ is even or odd" (Milne, p. 64).

# Prerequisites

- **Permutation group** — Sign is defined for permutations
- **Transposition** — Sign counts parity of transposition decompositions

# Key Properties

1. $\operatorname{sign}: S_n \to \{\pm 1\}$ is a surjective homomorphism (for $n \geq 2$)
2. $\operatorname{sign}(\sigma\tau) = \operatorname{sign}(\sigma) \cdot \operatorname{sign}(\tau)$
3. $\operatorname{sign}(\text{transposition}) = -1$
4. An $r$-cycle has sign $(-1)^{r-1}$ (even iff $r$ is odd)
5. The sign is well-defined: independent of the transposition decomposition chosen
6. Visual method: count crossings when connecting $i$ in top row to $i$ in bottom row (Remark 4.24)

# Construction / Recognition

## To compute $\operatorname{sign}(\sigma)$:
1. Decompose $\sigma$ into disjoint cycles
2. Each $r$-cycle contributes $(-1)^{r-1}$
3. Multiply the contributions
4. Alternatively: count inversions; sign is $(-1)^{\text{number of inversions}}$

# Context & Application

The sign homomorphism defines the alternating group $A_n = \ker(\operatorname{sign})$. It is the unique homomorphism $S_n \to \{\pm 1\}$ sending every transposition to $-1$.

# Examples

**Example 1** (p. 64): The permutation $\begin{pmatrix} 1&2&3&4&5&6&7 \\ 2&5&7&4&3&1&6 \end{pmatrix}$ has 6 crossings, hence is even.

**Example 2** (p. 68): In $S_4$, permutations of type $(ab)$ and $(abcd)$ are odd; types $1$, $(abc)$, $(ab)(cd)$ are even.

# Relationships

## Builds Upon
- **permutation-group**, **transposition**

## Enables
- **alternating-group** — $A_n = \ker(\operatorname{sign})$

# Common Errors

- **Error**: Thinking the sign depends on which transposition decomposition you choose
  **Correction**: The parity is well-defined; different decompositions always give the same parity

# Source Reference

Chapter 4: Groups Acting on Sets, "Permutation groups", pages 64-65.

# Verification Notes

- Definition source: Direct from p. 64
- Confidence: HIGH — explicit definition
- Uncertainties: None
