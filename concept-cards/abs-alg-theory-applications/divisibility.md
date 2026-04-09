---
# === CORE IDENTIFICATION ===
concept: Divisibility
slug: divisibility

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
  - divides

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - greatest-common-divisor
  - prime-number
  - congruence-modulo-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

An integer $a$ divides an integer $b$, written $a \mid b$, if $b = ak$ for some integer $k$.

# Core Definition

"Let $a$ and $b$ be integers. If $b = ak$ for some integer $k$, we write $a \mid b$" (Judson, p. 33).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. $a \mid 0$ for all integers $a$
2. $1 \mid b$ for all integers $b$
3. If $a \mid b$ and $b \mid c$, then $a \mid c$ (transitivity)
4. If $a \mid b$ and $a \mid c$, then $a \mid (bx + cy)$ for all integers $x, y$
5. $a \mid b$ and $b \mid a$ implies $a = \pm b$

# Construction / Recognition

## To Check if $a \mid b$:
1. Compute $b / a$
2. If the result is an integer, then $a \mid b$
3. Equivalently, check if $b \mod a = 0$

# Context & Application

Divisibility is the foundational concept for the GCD, prime numbers, and the Fundamental Theorem of Arithmetic. It also underlies congruence modulo $n$.

# Examples

**Example 1** (p. 33): In the Division Algorithm, if the remainder $r = 0$, then $b$ divides $a$.

**Example 2** (p. 33): An integer $d$ is a common divisor of $a$ and $b$ if $d \mid a$ and $d \mid b$.

# Relationships

## Enables
- **greatest-common-divisor** — Defined in terms of divisibility
- **prime-number** — Primes are defined by their divisibility properties
- **congruence-modulo-n** — $r \equiv s \pmod{n}$ means $n \mid (r - s)$

# Common Errors

- **Error**: Writing $a \mid b$ when meaning $a / b$ (division)
  **Correction**: $a \mid b$ is a relation (true/false), not an operation that produces a quotient

# Common Confusions

- **Confusion**: Confusing "divides" with "is divided by"
  **Clarification**: $a \mid b$ means "$a$ divides $b$" or "$b$ is divisible by $a$"; the divisor is on the left

# Source Reference

Chapter 2: The Integers, Section 2.2, page 33.

# Verification Notes

- Definition source: Direct from p. 33
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
