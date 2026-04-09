---
# === CORE IDENTIFICATION ===
concept: Cancellation Law for Integral Domains
slug: cancellation-law-integral-domains

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
pdf_page: 208
section: "16.2 Integral Domains and Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - integral-domain
extends: []
related:
  - zero-divisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When can you cancel in a ring?"
  - "What is the cancellation law for integral domains?"
---

# Quick Definition

In an integral domain, if $a \neq 0$ and $ab = ac$, then $b = c$. This cancellation property is equivalent to having no zero divisors.

# Core Definition

"Let $D$ be a commutative ring with identity. Then $D$ is an integral domain if and only if for all nonzero elements $a \in D$ with $ab = ac$, we have $b = c$" (Judson, Proposition 16.15, p. 208).

# Prerequisites

- **Integral domain** — The cancellation law characterizes integral domains

# Key Properties

1. $ab = ac$ with $a \neq 0$ implies $b = c$
2. Equivalent to having no zero divisors
3. Does not hold in rings with zero divisors (e.g., $\mathbb{Z}_{12}$)

# Construction / Recognition

## To Apply:
1. Verify the ring is an integral domain
2. Given $ab = ac$ with $a \neq 0$, conclude $b = c$

# Context & Application

The cancellation law is the ring-theoretic analog of the familiar cancellation from arithmetic. It is essential for factorization arguments and is used in the proof that finite integral domains are fields.

# Examples

**Example 1** (p. 208): In $\mathbb{Z}$, if $3 \cdot 5 = 3 \cdot b$, then $b = 5$.

**Example 2**: In $\mathbb{Z}_{12}$, $3 \cdot 4 = 0 = 3 \cdot 0$ but $4 \neq 0$, so cancellation fails.

# Relationships

## Related
- **Zero divisor** — No zero divisors $\Leftrightarrow$ cancellation holds
- **Integral domain** — Alternative characterization

# Common Errors

- **Error**: Cancelling in a ring without verifying it is an integral domain
  **Correction**: Cancellation is only valid in rings without zero divisors

# Common Confusions

- **Confusion**: Thinking cancellation requires multiplicative inverses
  **Clarification**: Cancellation in integral domains works without inverses; it follows from $a(b-c) = 0$ with $a \neq 0$ implying $b - c = 0$

# Source Reference

Chapter 16: Rings, Section 16.2, Proposition 16.15, page 208.

# Verification Notes

- Definition source: Direct from Proposition 16.15
- Confidence: HIGH — explicit proposition
- Cross-reference status: Verified
- Uncertainties: None
