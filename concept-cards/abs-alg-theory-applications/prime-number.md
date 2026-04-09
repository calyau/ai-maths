---
# === CORE IDENTIFICATION ===
concept: Prime Number
slug: prime-number

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
aliases:
  - prime

# === TYPED RELATIONSHIPS ===
prerequisites:
  - divisibility
extends: []
related:
  - fundamental-theorem-of-arithmetic
  - euclids-lemma
  - composite-number
contrasts_with:
  - composite-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A prime number is an integer $p > 1$ whose only positive divisors are 1 and $p$ itself.

# Core Definition

"Let $p$ be an integer such that $p > 1$. We say that $p$ is a prime number, or simply $p$ is prime, if the only positive numbers that divide $p$ are 1 and $p$ itself. An integer $n > 1$ that is not prime is said to be composite" (Judson, p. 35).

# Prerequisites

- **Divisibility** — Primes are defined by their divisibility properties

# Key Properties

1. A prime $p > 1$ has exactly two positive divisors: 1 and $p$
2. **Euclid's Lemma** (Lemma 2.13): If $p \mid ab$, then $p \mid a$ or $p \mid b$
3. There are infinitely many primes (Theorem 2.14, Euclid)
4. Every integer $n > 1$ is a product of primes (Fundamental Theorem of Arithmetic)

# Construction / Recognition

## To Test if $n$ is Prime:
1. Check if any integer from 2 to $\sqrt{n}$ divides $n$
2. If none do, $n$ is prime
3. If one does, $n$ is composite

# Context & Application

Primes are fundamental building blocks of the integers. In abstract algebra, prime numbers appear in the structure of cyclic groups (e.g., $\mathbb{Z}_p$ is a field when $p$ is prime), in determining the structure of finite abelian groups, and in applications to cryptography.

# Examples

**Example 1** (p. 36): Euler showed that $2^{2^5} + 1 = 4{,}294{,}967{,}297$ is composite, disproving Fermat's conjecture.

**Example 2** (p. 35): Euclid's proof of infinitely many primes: if $p_1, \ldots, p_n$ are all primes, then $P = p_1 p_2 \cdots p_n + 1$ cannot be divisible by any $p_i$, contradiction.

# Relationships

## Builds Upon
- **divisibility** — Primes defined by divisibility

## Enables
- **fundamental-theorem-of-arithmetic** — Every integer > 1 factors uniquely into primes
- **group-of-units** — When $p$ is prime, every nonzero element of $\mathbb{Z}_p$ has an inverse

## Contrasts With
- **composite-number** — An integer $> 1$ that is not prime

# Common Errors

- **Error**: Claiming 1 is prime
  **Correction**: By convention, primes must be greater than 1

# Common Confusions

- **Confusion**: Thinking there are finitely many primes
  **Clarification**: Euclid proved there are infinitely many primes (Theorem 2.14)

# Source Reference

Chapter 2: The Integers, Section 2.2, pages 35-36.

# Verification Notes

- Definition source: Direct quote from p. 35
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
