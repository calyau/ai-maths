---
# === CORE IDENTIFICATION ===
concept: Sign of a Permutation
slug: sign-of-a-permutation

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
aliases:
  - "signature of a permutation"
  - "parity of a permutation"
  - "sgn"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
  - transposition
extends: []
related:
  - even-permutation
  - odd-permutation
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes even and odd permutations?"
  - "How is the sign of a permutation defined?"
  - "How do I determine the sign of a given permutation?"
---

# Quick Definition

The sign of a permutation $\alpha \in S_n$ is $+1$ if $\alpha$ can be written as a product of an even number of transpositions, and $-1$ if an odd number. It is well-defined regardless of which transposition decomposition is chosen.

# Core Definition

Armstrong defines the sign using the polynomial $P = \prod_{i < j} (x_i - x_j)$ (p. 35). For $\alpha \in S_n$, define $\alpha P$ to be the product of all factors $(x_{\alpha(i)} - x_{\alpha(j)})$ where $i < j$. "The effect of $\alpha$ is to permute the terms of $P$, while at the same time changing the sign of some of them. Therefore, $\alpha P$ is either $+P$ or $-P$, and this determines the so called *sign* of $\alpha$ to be $+1$ in the first instance and $-1$ in the second" (p. 35-36).

The sign is multiplicative: the sign of $\alpha\beta$ is the product of the signs of $\alpha$ and $\beta$ (p. 36).

# Prerequisites

- **Permutation** — The sign is a property of permutations
- **Transposition** — The sign is determined by transposition decomposition

# Key Properties

1. The sign of a permutation is either $+1$ or $-1$
2. The sign of the identity is $+1$
3. The sign of any transposition is $-1$ (p. 36)
4. The sign is multiplicative: $\operatorname{sgn}(\alpha\beta) = \operatorname{sgn}(\alpha) \cdot \operatorname{sgn}(\beta)$
5. If $\alpha$ is a product of an even number of transpositions, its sign is $+1$
6. If $\alpha$ is a product of an odd number of transpositions, its sign is $-1$
7. A $k$-cycle has sign $(-1)^{k-1}$, so it is even precisely when $k$ is odd

# Construction / Recognition

## To Determine the Sign:
1. Write the permutation as a product of disjoint cycles
2. Count the number of even-length cycles; call this $m$
3. The sign is $(-1)^m$

Alternatively:
1. Write the permutation as a product of transpositions
2. If the number of transpositions is even, the sign is $+1$; if odd, the sign is $-1$

# Context & Application

The sign function $\operatorname{sgn}: S_n \to \{+1, -1\}$ is a group homomorphism from $S_n$ to the multiplicative group $\{+1, -1\}$. Its kernel is the alternating group $A_n$. The sign is well-defined because although the transposition decomposition is not unique, the parity of the number of transpositions is invariant.

# Examples

**Example** (p. 36): For $n = 3$ and $\alpha = (132)$:
$$P = (x_1 - x_2)(x_1 - x_3)(x_2 - x_3)$$
$$\alpha P = (x_3 - x_1)(x_3 - x_2)(x_1 - x_2) = +P$$
So the sign of $(132)$ is $+1$.

**Example** (p. 36): The sign of $(1a)$ is $-1$ for all $a > 1$, since $(1a) = (2a)(12)(2a)$ and $(12)$ has sign $-1$.

# Relationships

## Builds Upon
- **Transposition** — The sign is defined via transposition decomposition

## Enables
- **Even permutation** — Permutations with sign $+1$
- **Odd permutation** — Permutations with sign $-1$
- **Alternating group** — The kernel of the sign function

## Related
- **Disjoint cycle decomposition** — The sign can be read from cycle lengths

# Common Errors

- **Error**: Thinking a 3-cycle is odd because 3 is odd.
  **Correction**: A $k$-cycle is even when $k$ is odd. The 3-cycle $(abc) = (ac)(ab)$ is a product of 2 transpositions, hence even.

# Common Confusions

- **Confusion**: Thinking the sign depends on which transposition decomposition is chosen.
  **Clarification**: While the decomposition is not unique, the parity is always the same. This is the content of the well-definedness proof using the polynomial $P$.

# Source Reference

Chapter 6: Permutations, pages 35-36 (pdf pp. 35-36). Definition via the polynomial $P$; multiplicativity and sign of transpositions proved on p. 36.

# Verification Notes

- Definition: Direct from pp. 35-36 using the polynomial $P$
- Multiplicativity: Stated explicitly on p. 36
- Confidence: HIGH — detailed treatment with worked example
