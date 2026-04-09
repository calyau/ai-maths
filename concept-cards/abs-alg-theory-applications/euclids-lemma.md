---
# === CORE IDENTIFICATION ===
concept: Euclid's Lemma
slug: euclids-lemma

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
pdf_page: 35
section: "Prime Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prime-number
  - relatively-prime
  - bezouts-identity
extends: []
related:
  - fundamental-theorem-of-arithmetic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Euclid's Lemma states that if a prime $p$ divides a product $ab$, then $p$ divides $a$ or $p$ divides $b$.

# Core Definition

**Lemma 2.13 (Euclid)**: "Let $a$ and $b$ be integers and $p$ be a prime number. If $p \mid ab$, then either $p \mid a$ or $p \mid b$" (Judson, p. 35).

# Prerequisites

- **Prime number** — The lemma is about prime divisors
- **Relatively prime** — If $p \nmid a$, then $\gcd(a, p) = 1$
- **Bezout's identity** — Used in the proof

# Key Properties

1. Only holds for prime divisors, not arbitrary divisors
2. Extends to products of more than two factors
3. Key ingredient in the uniqueness proof of the Fundamental Theorem of Arithmetic

# Construction / Recognition

## Proof Outline:
1. Suppose $p \nmid a$
2. Since $p$ is prime, $\gcd(a, p) = 1$
3. By Bezout's identity, $ar + ps = 1$ for some integers $r, s$
4. Then $b = b(ar + ps) = (ab)r + p(bs)$
5. Since $p \mid ab$ and $p \mid p$, we get $p \mid b$

# Context & Application

Euclid's Lemma is essential for proving the uniqueness of prime factorization. It generalizes to prime ideals in ring theory.

# Examples

**Example 1** (p. 35): If $7 \mid 42$ and $42 = 6 \cdot 7$, then $7 \mid 6$ or $7 \mid 7$. Indeed $7 \mid 7$.

**Example 2**: $5 \mid 30 = 6 \cdot 5$, and indeed $5 \mid 5$. Also $3 \mid 12 = 4 \cdot 3$, and $3 \mid 3$.

# Relationships

## Builds Upon
- **prime-number** — Applies specifically to primes
- **bezouts-identity** — Used in the proof

## Enables
- **fundamental-theorem-of-arithmetic** — Uniqueness proof depends on this lemma

# Common Errors

- **Error**: Applying the lemma to composite divisors
  **Correction**: The lemma is false for composites: $6 \mid 12 = 4 \cdot 3$ but $6 \nmid 4$ and $6 \nmid 3$

# Common Confusions

- **Confusion**: Thinking the converse holds (if $d \mid a$ or $d \mid b$, then $d \mid ab$)
  **Clarification**: The converse is trivially true for all divisors, not just primes

# Source Reference

Chapter 2: The Integers, Section 2.2, Lemma 2.13, page 35.

# Verification Notes

- Definition source: Direct quote from Lemma 2.13, p. 35
- Confidence: HIGH — explicit lemma with proof
- Cross-reference status: Verified
- Uncertainties: None
