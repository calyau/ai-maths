---
# === CORE IDENTIFICATION ===
concept: Fundamental Theorem of Arithmetic
slug: fundamental-theorem-of-arithmetic

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
pdf_page: 36
section: "Prime Numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - unique factorization theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prime-number
  - mathematical-induction
  - well-ordering-principle
extends: []
related:
  - euclids-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Fundamental Theorem of Arithmetic states that every integer $n > 1$ can be written uniquely as a product of prime numbers, up to the order of the factors.

# Core Definition

**Theorem 2.15 (Fundamental Theorem of Arithmetic)**: "Let $n$ be an integer such that $n > 1$. Then $n = p_1 p_2 \cdots p_k$ where $p_1, \ldots, p_k$ are primes (not necessarily distinct). Furthermore, this factorization is unique; that is, if $n = q_1 q_2 \cdots q_l$, then $k = l$ and the $q_i$'s are just the $p_i$'s rearranged" (Judson, p. 36).

# Prerequisites

- **Prime number** — Factorization is into primes
- **Mathematical induction** — Used in the uniqueness proof
- **Well-Ordering Principle** — Used in the existence proof

# Key Properties

1. Every integer $> 1$ has a prime factorization (**existence**)
2. This factorization is unique up to reordering (**uniqueness**)
3. Uniqueness proof uses Euclid's Lemma and strong induction
4. Existence proof uses the Well-Ordering Principle

# Construction / Recognition

## To Find the Prime Factorization:
1. Divide $n$ by the smallest prime that divides it
2. Repeat with the quotient until the quotient is 1
3. The collected primes give the factorization

# Context & Application

The Fundamental Theorem of Arithmetic is a cornerstone of number theory and underlies much of abstract algebra. It guarantees that the integers have a unique factorization domain structure, which is contrasted with more general algebraic structures where unique factorization may fail.

# Examples

**Example 1** (p. 36): The proof of uniqueness proceeds by induction on $n$. If $n = p_1 \cdots p_k = q_1 \cdots q_l$, then by Euclid's Lemma, $p_1 = q_i$ for some $i$. By the induction hypothesis, $n' = p_2 \cdots p_k = q_2 \cdots q_l$ has unique factorization, so $k = l$ and the factors match.

# Relationships

## Builds Upon
- **prime-number** — Factorization is into primes
- **euclids-lemma** — Used in uniqueness proof
- **mathematical-induction** — Proof technique for uniqueness

## Related
- **well-ordering-principle** — Used in existence proof

# Common Errors

- **Error**: Forgetting that the factorization allows repeated primes
  **Correction**: Primes need not be distinct; e.g., $12 = 2 \cdot 2 \cdot 3$

# Common Confusions

- **Confusion**: Thinking unique factorization holds in all number systems
  **Clarification**: Unique factorization fails in some algebraic structures; e.g., in $\mathbb{Z}[\sqrt{-5}]$, $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$

# Source Reference

Chapter 2: The Integers, Section 2.2, Theorem 2.15, pages 36-37.

# Verification Notes

- Definition source: Direct quote from Theorem 2.15, p. 36
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
