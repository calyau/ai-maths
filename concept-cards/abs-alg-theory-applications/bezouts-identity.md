---
# === CORE IDENTIFICATION ===
concept: Bezout's Identity
slug: bezouts-identity

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
  - "Bezout's theorem"
  - "GCD as linear combination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - greatest-common-divisor
  - well-ordering-principle
extends: []
related:
  - euclidean-algorithm
  - relatively-prime
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Bezout's Identity states that for any nonzero integers $a$ and $b$, there exist integers $r$ and $s$ such that $\gcd(a, b) = ar + bs$.

# Core Definition

**Theorem 2.10**: "Let $a$ and $b$ be nonzero integers. Then there exist integers $r$ and $s$ such that $\gcd(a, b) = ar + bs$. Furthermore, the greatest common divisor of $a$ and $b$ is unique" (Judson, p. 33).

**Corollary 2.11**: If $a$ and $b$ are relatively prime, then $ar + bs = 1$ for some integers $r$ and $s$.

# Prerequisites

- **Greatest common divisor** — The identity expresses the GCD as a linear combination
- **Well-Ordering Principle** — Used in the proof

# Key Properties

1. The GCD can always be expressed as an integer linear combination of $a$ and $b$
2. The coefficients $r$ and $s$ are not unique
3. When $\gcd(a, b) = 1$, gives $ar + bs = 1$
4. The Euclidean Algorithm provides a constructive way to find $r$ and $s$

# Construction / Recognition

## To Find $r$ and $s$:
1. Run the Euclidean Algorithm to find $\gcd(a, b)$
2. Back-substitute through the chain of equations
3. Express the GCD as a combination of $a$ and $b$

# Context & Application

Bezout's Identity is used to prove Euclid's Lemma, to find multiplicative inverses in $\mathbb{Z}_n$, and in the proof that the GCD is unique. It establishes that the GCD is the smallest positive linear combination of $a$ and $b$.

# Examples

**Example 1** (p. 34-35): For $\gcd(945, 2415) = 105$:
- $105 = 525 + (-1) \cdot 420 = 2 \cdot 525 + (-1) \cdot 945 = 2 \cdot 2415 + (-5) \cdot 945$
- So $r = -5$ and $s = 2$ (not unique; $r = 41$ and $s = -16$ also work).

# Relationships

## Builds Upon
- **greatest-common-divisor** — Expresses the GCD

## Enables
- **euclids-lemma** — Proof uses Bezout's Identity
- **relatively-prime** — Corollary gives $ar + bs = 1$ when $\gcd(a,b) = 1$
- **group-of-units** — Finding multiplicative inverses in $\mathbb{Z}_n$

# Common Errors

- **Error**: Assuming $r$ and $s$ are unique
  **Correction**: There are infinitely many pairs $(r, s)$ satisfying $\gcd(a,b) = ar + bs$

# Common Confusions

- **Confusion**: Thinking Bezout's Identity requires $a$ and $b$ to be coprime
  **Clarification**: The identity holds for ANY nonzero integers; when coprime, the RHS is 1

# Source Reference

Chapter 2: The Integers, Section 2.2, Theorem 2.10, pages 33-34. Corollary 2.11.

# Verification Notes

- Definition source: Direct quote from Theorem 2.10, p. 33
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
