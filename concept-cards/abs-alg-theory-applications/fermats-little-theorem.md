---
# === CORE IDENTIFICATION ===
concept: Fermat's Little Theorem
slug: fermats-little-theorem

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
pdf_page: 91
section: "6.3 Fermat's and Euler's Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eulers-theorem
extends:
  - eulers-theorem
related:
  - rsa-cryptosystem
  - pseudoprime
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Fermat's Little Theorem?"
  - "How does Fermat's Little Theorem relate to Euler's Theorem?"
---

# Quick Definition

Fermat's Little Theorem states that if $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod{p}$. Furthermore, for any integer $b$, $b^p \equiv b \pmod{p}$.

# Core Definition

**Theorem 6.19 (Fermat's Little Theorem):** "Let $p$ be any prime number and suppose that $p \nmid a$. Then $a^{p-1} \equiv 1 \pmod{p}$. Furthermore, for any integer $b$, $b^p \equiv b \pmod{p}$" (Judson, p. 91). This is the special case of Euler's Theorem with $n = p$ prime, since $\phi(p) = p - 1$.

# Prerequisites

- **Euler's Theorem** — Fermat's Little Theorem is a special case

# Key Properties

1. $a^{p-1} \equiv 1 \pmod{p}$ when $p$ is prime and $\gcd(a, p) = 1$
2. Equivalently, $b^p \equiv b \pmod{p}$ for all integers $b$
3. Special case of Euler's Theorem with $\phi(p) = p - 1$
4. The converse is false: pseudoprimes satisfy $2^{n-1} \equiv 1 \pmod{n}$ without being prime

# Construction / Recognition

## To Apply:
1. Verify $p$ is prime
2. Verify $p \nmid a$
3. Conclude $a^{p-1} \equiv 1 \pmod{p}$

# Context & Application

Fermat's Little Theorem is used in primality testing (the Fermat test) and in simplifying computations in modular arithmetic. It underpins the RSA cryptosystem.

# Examples

**Example 1** (p. 102): $2^{16} \equiv 1 \pmod{17}$, confirming 17 is a potential prime. But $2^{14} \equiv 4 \pmod{15}$, showing 15 is not prime.

# Relationships

## Builds Upon
- **Euler's Theorem** — Fermat's Little Theorem is the prime case

## Enables
- **RSA Cryptosystem** — Used in the correctness proof
- **Pseudoprime** — Fermat's test for primality

# Common Errors

- **Error**: Applying the theorem when $p$ divides $a$
  **Correction**: Must have $\gcd(a, p) = 1$; use the second form $b^p \equiv b$ if $p | b$

# Common Confusions

- **Confusion**: Thinking the converse holds (that $a^{n-1} \equiv 1$ implies $n$ is prime)
  **Clarification**: There exist pseudoprimes (e.g., 341) where this holds but $n$ is composite

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.3, Theorem 6.19, page 91.

# Verification Notes

- Definition source: Direct from Theorem 6.19
- Confidence rationale: Explicit named theorem
- Uncertainties: None
- Cross-reference status: Verified
