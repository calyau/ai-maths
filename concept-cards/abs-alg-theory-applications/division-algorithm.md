---
# === CORE IDENTIFICATION ===
concept: Division Algorithm
slug: division-algorithm

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - well-ordering-principle
extends: []
related:
  - greatest-common-divisor
  - euclidean-algorithm
  - congruence-modulo-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Division Algorithm states that for integers $a$ and $b$ with $b > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that $a = bq + r$ where $0 \leq r < b$.

# Core Definition

**Theorem 2.9 (Division Algorithm)**: "Let $a$ and $b$ be integers, with $b > 0$. Then there exist unique integers $q$ and $r$ such that $a = bq + r$ where $0 \leq r < b$" (Judson, p. 33).

# Prerequisites

- **Well-Ordering Principle** — Used in the existence proof

# Key Properties

1. Both existence and uniqueness of $q$ and $r$ are guaranteed
2. The remainder $r$ satisfies $0 \leq r < b$
3. If $r = 0$, then $b$ divides $a$
4. The proof is an existence-and-uniqueness proof using Well-Ordering

# Construction / Recognition

## To Apply the Division Algorithm:
1. Given integers $a$ and $b > 0$
2. Divide $a$ by $b$
3. The quotient is $q = \lfloor a/b \rfloor$
4. The remainder is $r = a - bq$, satisfying $0 \leq r < b$

# Context & Application

The Division Algorithm is fundamental to the theory of integers and is used to prove the existence of the GCD, the Euclidean Algorithm, and the construction of $\mathbb{Z}_n$. It is also crucial in the proof that every subgroup of a cyclic group is cyclic (Theorem 4.10).

# Examples

**Example 1** (p. 34): Computing gcd(945, 2415) uses repeated application:
- $2415 = 945 \cdot 2 + 525$
- $945 = 525 \cdot 1 + 420$
- $525 = 420 \cdot 1 + 105$
- $420 = 105 \cdot 4 + 0$

# Relationships

## Builds Upon
- **well-ordering-principle** — Existence proof uses Well-Ordering

## Enables
- **greatest-common-divisor** — GCD computation relies on the Division Algorithm
- **euclidean-algorithm** — Based on repeated application of the Division Algorithm
- **congruence-modulo-n** — The remainder $r$ determines the equivalence class mod $b$

# Common Errors

- **Error**: Allowing negative remainders
  **Correction**: The remainder must satisfy $0 \leq r < b$

# Common Confusions

- **Confusion**: Thinking the Division Algorithm is just long division
  **Clarification**: The Division Algorithm is a theorem guaranteeing existence and uniqueness, not merely a computational procedure

# Source Reference

Chapter 2: The Integers, Section 2.2, Theorem 2.9, pages 33-34.

# Verification Notes

- Definition source: Direct quote from Theorem 2.9, p. 33
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
