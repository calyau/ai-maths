---
# === CORE IDENTIFICATION ===
concept: Euclidean Algorithm
slug: euclidean-algorithm

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
pdf_page: 34
section: "The Euclidean Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - division-algorithm
  - greatest-common-divisor
extends: []
related:
  - bezouts-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Euclidean Algorithm computes the greatest common divisor of two integers by repeated application of the Division Algorithm, producing a decreasing sequence of remainders until reaching zero.

# Core Definition

"The algorithm that we have just used to find the greatest common divisor $d$ of two integers $a$ and $b$ and to write $d$ as the linear combination of $a$ and $b$ is known as the Euclidean algorithm" (Judson, p. 35). It proceeds by repeated divisions:

$$b = aq_1 + r_1, \quad a = r_1q_2 + r_2, \quad r_1 = r_2q_3 + r_3, \quad \ldots, \quad r_{n-1} = r_nq_{n+1}$$

yielding $\gcd(a, b) = r_n$, the last nonzero remainder.

# Prerequisites

- **Division Algorithm** — Each step applies the Division Algorithm
- **Greatest common divisor** — The algorithm computes the GCD

# Key Properties

1. Produces a decreasing sequence of positive remainders $r_1 > r_2 > \cdots > r_n$
2. Terminates because the remainders are positive and strictly decreasing
3. The last nonzero remainder is $\gcd(a, b)$
4. Can be run backward to express $\gcd(a, b) = ra + sb$ (Bezout's identity)

# Construction / Recognition

## To Compute $\gcd(a, b)$:
1. Divide $b$ by $a$: $b = aq_1 + r_1$
2. Divide $a$ by $r_1$: $a = r_1q_2 + r_2$
3. Continue dividing each remainder by the next: $r_{i-1} = r_iq_{i+1} + r_{i+1}$
4. Stop when the remainder is 0
5. The last nonzero remainder is $\gcd(a, b)$

# Context & Application

The Euclidean Algorithm is one of the oldest algorithms in mathematics and is still widely used in number theory, cryptography, and computer science. In algebra, it is used to find multiplicative inverses in $\mathbb{Z}_n$ and to determine generators of cyclic groups.

# Examples

**Example 1** (p. 34): Compute $\gcd(945, 2415)$:
- $2415 = 945 \cdot 2 + 525$
- $945 = 525 \cdot 1 + 420$
- $525 = 420 \cdot 1 + 105$
- $420 = 105 \cdot 4 + 0$

So $\gcd(945, 2415) = 105$. Running backward: $105 = 2 \cdot 2415 + (-5) \cdot 945$.

# Relationships

## Builds Upon
- **division-algorithm** — Each step is an application of the Division Algorithm

## Enables
- **bezouts-identity** — Backward substitution yields the linear combination
- **group-of-units** — Finding inverses in $\mathbb{Z}_n$

# Common Errors

- **Error**: Stopping at the wrong remainder (not the last nonzero one)
  **Correction**: Continue until the remainder is exactly 0; the previous remainder is the GCD

# Common Confusions

- **Confusion**: Thinking the Euclidean Algorithm only finds the GCD
  **Clarification**: It also provides a way to express the GCD as a linear combination $\gcd(a,b) = ra + sb$

# Source Reference

Chapter 2: The Integers, Section 2.2, pages 34-35.

# Verification Notes

- Definition source: Direct from p. 35
- Confidence: HIGH — explicit algorithm with worked example
- Cross-reference status: Verified
- Uncertainties: None
