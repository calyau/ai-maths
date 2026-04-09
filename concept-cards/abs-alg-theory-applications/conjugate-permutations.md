---
# === CORE IDENTIFICATION ===
concept: Conjugate Permutations
slug: conjugate-permutations

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 90
section: "6.2 Lagrange's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - conjugation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cycle
  - symmetric-group
extends: []
related:
  - lagranges-theorem
  - inner-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two permutations conjugate?"
  - "What is the relationship between conjugate cycles?"
---

# Quick Definition

Two cycles $\tau$ and $\mu$ in $S_n$ have the same length if and only if there exists $\sigma \in S_n$ such that $\mu = \sigma\tau\sigma^{-1}$. Permutations related this way are called conjugate.

# Core Definition

**Theorem 6.16:** "Two cycles $\tau$ and $\mu$ in $S_n$ have the same length if and only if there exists a $\sigma \in S_n$ such that $\mu = \sigma\tau\sigma^{-1}$" (Judson, p. 90). If $\tau = (a_1, a_2, \ldots, a_k)$, then $\sigma\tau\sigma^{-1} = (\sigma(a_1), \sigma(a_2), \ldots, \sigma(a_k))$.

# Prerequisites

- **Cycle** — Conjugation is defined for cycles
- **Symmetric Group** — Conjugation occurs within $S_n$

# Key Properties

1. $\sigma(a_1, a_2, \ldots, a_k)\sigma^{-1} = (\sigma(a_1), \sigma(a_2), \ldots, \sigma(a_k))$
2. Conjugate cycles have the same length
3. Conjugation preserves cycle structure
4. Conjugation defines an equivalence relation on $S_n$

# Construction / Recognition

## To Compute $\sigma\tau\sigma^{-1}$ for a cycle $\tau = (a_1, \ldots, a_k)$:
1. Apply $\sigma$ to each element in the cycle
2. The result is $(\sigma(a_1), \sigma(a_2), \ldots, \sigma(a_k))$

# Context & Application

Conjugation is central to understanding the structure of permutation groups. Two permutations are conjugate if and only if they have the same cycle structure, which means conjugacy classes in $S_n$ are determined by cycle type.

# Examples

**Example 1** (p. 90): If $\tau = (a_1, \ldots, a_k)$ and $\mu = (b_1, \ldots, b_k)$, define $\sigma(a_i) = b_i$. Then $\mu = \sigma\tau\sigma^{-1}$.

# Relationships

## Builds Upon
- **Cycle** — Conjugation acts on cycles
- **Symmetric Group** — Setting for conjugation

## Enables
- **Inner Automorphism** — Conjugation by $g$ defines an inner automorphism (Chapter 9)

# Common Errors

- **Error**: Computing $\sigma\tau\sigma^{-1}$ by matrix multiplication instead of applying the cycle formula
  **Correction**: Use the shortcut: $\sigma(a_1, \ldots, a_k)\sigma^{-1} = (\sigma(a_1), \ldots, \sigma(a_k))$

# Common Confusions

- **Confusion**: Thinking conjugation changes the cycle structure
  **Clarification**: Conjugation preserves cycle structure; it only relabels elements

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.2, Theorem 6.16, page 90.

# Verification Notes

- Definition source: Direct from Theorem 6.16
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
