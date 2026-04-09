---
# === CORE IDENTIFICATION ===
concept: Chinese Remainder Theorem
slug: chinese-remainder-theorem

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 214
section: "16.5 An Application to Software Design"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "CRT"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
  - factor-ring
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Chinese Remainder Theorem?"
  - "How can systems of congruences be solved?"
---

# Quick Definition

The Chinese Remainder Theorem states that a system of simultaneous congruences $x \equiv a_i \pmod{n_i}$ has a solution when the moduli $n_i$ are pairwise coprime, and the solution is unique modulo $n_1 n_2 \cdots n_k$.

# Core Definition

"Let $n_1, n_2, \ldots, n_k$ be positive integers such that $\gcd(n_i, n_j) = 1$ for $i \neq j$. Then for any integers $a_1, \ldots, a_k$, the system $x \equiv a_1 \pmod{n_1}, \ldots, x \equiv a_k \pmod{n_k}$ has a solution. Furthermore, any two solutions of the system are congruent modulo $n_1 n_2 \cdots n_k$" (Judson, Theorem 16.43, p. 215).

# Prerequisites

- **Ring** — The theorem concerns the ring $\mathbb{Z}$
- **Factor ring** — Relates to quotient rings $\mathbb{Z}/n_i\mathbb{Z}$

# Key Properties

1. Requires pairwise coprime moduli: $\gcd(n_i, n_j) = 1$ for $i \neq j$
2. Existence and uniqueness (mod $n_1 \cdots n_k$)
3. Can be applied iteratively: solve pairs and combine

# Construction / Recognition

## To Solve:
1. Start with two congruences and use the extended Euclidean algorithm
2. Combine the solution with the next congruence
3. Repeat until all congruences are resolved

# Context & Application

The CRT has applications in computer science for parallel computation with large integers, cryptography (RSA), and number theory. By breaking large integer computations into smaller modular ones, parallel processors can work on parts simultaneously (Judson, pp. 216-217).

# Examples

**Example 1** (p. 215): Solve $x \equiv 3 \pmod{4}$ and $x \equiv 4 \pmod{5}$. Solution: $x = 19 \pmod{20}$.

**Example 2** (p. 216): Solve $x \equiv 3 \pmod{4}$, $x \equiv 4 \pmod{5}$, $x \equiv 1 \pmod{9}$, $x \equiv 5 \pmod{7}$. Solution: $x = 19 \pmod{1260}$.

# Relationships

## Related
- **Parallel computing** — CRT enables distributing large integer arithmetic across processors

# Common Errors

- **Error**: Applying CRT when moduli are not pairwise coprime
  **Correction**: CRT requires $\gcd(n_i, n_j) = 1$ for all $i \neq j$

# Common Confusions

- **Confusion**: Thinking the CRT gives an explicit formula for the solution
  **Clarification**: The theorem guarantees existence and uniqueness; finding the solution typically requires the extended Euclidean algorithm

# Source Reference

Chapter 16: Rings, Section 16.5, Theorem 16.43, pages 214-217.

# Verification Notes

- Definition source: Direct from Theorem 16.43
- Confidence: HIGH — explicit theorem with worked examples
- Cross-reference status: Verified
- Uncertainties: None
