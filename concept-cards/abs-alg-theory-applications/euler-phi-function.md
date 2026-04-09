---
# === CORE IDENTIFICATION ===
concept: Euler Phi-Function
slug: euler-phi-function

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
section: "6.3 Fermat's and Euler's Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Euler totient function
  - "$\\phi(n)$"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - eulers-theorem
  - fermats-little-theorem
  - rsa-cryptosystem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Euler phi-function?"
  - "How do I compute $\\phi(n)$?"
---

# Quick Definition

The Euler $\phi$-function maps $n \in \mathbb{N}$ to the number of positive integers $m$ with $1 \leq m < n$ and $\gcd(m, n) = 1$. It equals the order of the group of units $U(n)$.

# Core Definition

"The Euler $\phi$-function is the map $\phi : \mathbb{N} \to \mathbb{N}$ defined by $\phi(n) = 1$ for $n = 1$, and, for $n > 1$, $\phi(n)$ is the number of positive integers $m$ with $1 \leq m < n$ and $\gcd(m, n) = 1$" (Judson, p. 90). By Theorem 6.17, $|U(n)| = \phi(n)$.

# Prerequisites

This is a foundational number-theoretic concept. No group theory prerequisites within this source.

# Key Properties

1. $\phi(p) = p - 1$ for any prime $p$
2. $|U(n)| = \phi(n)$ (Theorem 6.17)
3. $\phi(n) = n\prod_{p|n}(1 - 1/p)$ for $n = p_1^{e_1} \cdots p_k^{e_k}$
4. $\sum_{d|n} \phi(d) = n$

# Construction / Recognition

## To Compute $\phi(n)$:
1. Factor $n = p_1^{e_1} \cdots p_k^{e_k}$
2. Apply $\phi(n) = n(1 - 1/p_1)(1 - 1/p_2) \cdots (1 - 1/p_k)$
3. Alternatively, count integers from 1 to $n-1$ that are coprime to $n$

# Context & Application

The Euler $\phi$-function is essential for Euler's Theorem, Fermat's Little Theorem, and the RSA cryptosystem. It connects number theory to group theory through $|U(n)| = \phi(n)$.

# Examples

**Example 1** (p. 90): $|U(12)| = \phi(12) = 4$ since the numbers relatively prime to 12 are 1, 5, 7, and 11.

**Example 2** (p. 90): For any prime $p$, $\phi(p) = p - 1$.

# Relationships

## Enables
- **Euler's Theorem** — Uses $\phi(n)$ as the exponent
- **Fermat's Little Theorem** — Special case where $n = p$
- **RSA Cryptosystem** — Key generation uses $\phi(n)$

# Common Errors

- **Error**: Computing $\phi(12) = 6$ (counting all numbers less than 12 that are odd)
  **Correction**: $\phi(12) = 4$; must exclude numbers sharing factors with 12 (not just even numbers, but also 3, 9)

# Common Confusions

- **Confusion**: Confusing $\phi(n)$ with $n - 1$
  **Clarification**: $\phi(n) = n - 1$ only when $n$ is prime

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.3, page 90.

# Verification Notes

- Definition source: Direct from p. 90
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
