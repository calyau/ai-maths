---
# === CORE IDENTIFICATION ===
concept: Greatest Common Divisor
slug: greatest-common-divisor

# === CLASSIFICATION ===
category: foundations
subcategory: number-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Integers"
chapter_number: 2
pdf_page: 33
section: "The Division Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - GCD
  - gcd

# === TYPED RELATIONSHIPS ===
prerequisites:
  - divisibility
extends: []
related:
  - relatively-prime
  - euclidean-algorithm
  - bezouts-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The greatest common divisor of integers $a$ and $b$ is the largest positive integer $d$ that divides both $a$ and $b$, and every other common divisor of $a$ and $b$ divides $d$. It is written $d = \gcd(a, b)$.

# Core Definition

"An integer $d$ is called a common divisor of $a$ and $b$ if $d \mid a$ and $d \mid b$. The greatest common divisor of integers $a$ and $b$ is a positive integer $d$ such that $d$ is a common divisor of $a$ and $b$ and if $d'$ is any other common divisor of $a$ and $b$, then $d' \mid d$. We write $d = \gcd(a, b)$" (Judson, p. 33).

**Theorem 2.10 (Bezout's Identity)**: For nonzero integers $a$ and $b$, there exist integers $r$ and $s$ such that $\gcd(a, b) = ar + bs$. Furthermore, the GCD is unique.

# Prerequisites

- **Divisibility** — GCD is defined in terms of divisibility

# Key Properties

1. $\gcd(a, b)$ is unique
2. $\gcd(a, b) = ar + bs$ for some integers $r, s$ (Bezout's identity)
3. $\gcd(a, b) = \gcd(b, a)$
4. $\gcd(a, 0) = |a|$
5. $\gcd(a, b) = 1$ if and only if $a$ and $b$ are relatively prime

# Construction / Recognition

## To Compute $\gcd(a, b)$ via the Euclidean Algorithm:
1. Apply the Division Algorithm repeatedly
2. The last nonzero remainder is $\gcd(a, b)$

# Context & Application

The GCD is fundamental for determining when elements have multiplicative inverses in $\mathbb{Z}_n$ (namely when $\gcd(a, n) = 1$), for finding generators of cyclic groups, and for the order formula in cyclic groups (Theorem 4.13).

# Examples

**Example 1** (p. 33): $\gcd(24, 36) = 12$ and $\gcd(120, 102) = 6$.

**Example 2** (p. 34): $\gcd(945, 2415) = 105$, computed by repeated division, and $105 = 2 \cdot 2415 + (-5) \cdot 945$ (so $r = -5$, $s = 2$).

# Relationships

## Builds Upon
- **divisibility** — GCD is defined via common divisors

## Enables
- **relatively-prime** — Defined as $\gcd(a, b) = 1$
- **euclidean-algorithm** — Computes the GCD
- **group-of-units** — Elements with $\gcd(a, n) = 1$ form $U(n)$

## Related
- **bezouts-identity** — GCD is a linear combination of $a$ and $b$

# Common Errors

- **Error**: Computing the GCD by listing all common divisors for large numbers
  **Correction**: Use the Euclidean Algorithm for efficiency

# Common Confusions

- **Confusion**: Thinking the GCD definition requires $d$ to simply be the largest common divisor
  **Clarification**: The definition also requires every other common divisor to divide $d$; for positive integers these conditions are equivalent

# Source Reference

Chapter 2: The Integers, Section 2.2, pages 33-35. Theorem 2.10.

# Verification Notes

- Definition source: Direct quote from p. 33
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
