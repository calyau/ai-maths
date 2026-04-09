---
# === CORE IDENTIFICATION ===
concept: Zero Divisor
slug: zero-divisor

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 205
section: "16.1 Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "divisor of zero"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
extends: []
related:
  - integral-domain
  - unit-in-ring
contrasts_with:
  - unit-in-ring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a zero divisor?"
  - "How do zero divisors relate to integral domains?"
---

# Quick Definition

A zero divisor is a nonzero element $a$ in a ring $R$ such that there exists a nonzero element $b$ with $ab = 0$.

# Core Definition

"A nonzero element $a$ in a ring $R$ is called a zero divisor if there is a nonzero element $b$ in $R$ such that $ab = 0$" (Judson, p. 205). An integral domain is precisely a commutative ring with identity that has no zero divisors.

# Prerequisites

- **Ring** — Zero divisors are defined in the context of rings

# Key Properties

1. A zero divisor is nonzero by definition
2. If $a$ is a zero divisor, there exists nonzero $b$ with $ab = 0$
3. A ring has no zero divisors iff the cancellation law holds (Proposition 16.15)
4. A unit can never be a zero divisor
5. In $\mathbb{Z}_n$, the zero divisors are exactly the nonzero elements not coprime to $n$

# Construction / Recognition

## To Identify:
1. Find a nonzero element $a$ and a nonzero element $b$ such that $ab = 0$
2. Then both $a$ and $b$ are zero divisors

# Context & Application

Zero divisors are pathological elements that prevent a ring from behaving like the integers. Their absence characterizes integral domains. Understanding zero divisors is essential for determining when cancellation is valid and when quotient rings are integral domains.

# Examples

**Example 1** (p. 205): In $\mathbb{Z}_{12}$, $3 \cdot 4 \equiv 0 \pmod{12}$, so $3$ and $4$ are both zero divisors.

**Example 2** (p. 205): In $M_2(\mathbb{R})$, we can have $AB = 0$ with $A \neq 0$ and $B \neq 0$, so matrices can be zero divisors.

# Relationships

## Enables
- **Integral domain** — Defined as a commutative ring with identity having no zero divisors

## Contrasts With
- **Unit in ring** — A unit has a multiplicative inverse; a zero divisor does not. No element can be both.

# Common Errors

- **Error**: Calling $0$ a zero divisor
  **Correction**: By definition, a zero divisor must be nonzero

# Common Confusions

- **Confusion**: Thinking that if $ab = 0$ in any ring, then $a = 0$ or $b = 0$
  **Clarification**: This cancellation property only holds in integral domains; in general rings, nonzero elements can multiply to zero

# Source Reference

Chapter 16: Rings, Section 16.1, page 205, and Section 16.2, page 207.

# Verification Notes

- Definition source: Direct quote from p. 205
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
