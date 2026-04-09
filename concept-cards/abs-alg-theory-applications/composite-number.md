---
# === CORE IDENTIFICATION ===
concept: Composite Number
slug: composite-number

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
  - divisibility
extends: []
related:
  - fundamental-theorem-of-arithmetic
contrasts_with:
  - prime-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A composite number is an integer $n > 1$ that is not prime; that is, it has a positive divisor other than 1 and itself.

# Core Definition

"An integer $n > 1$ that is not prime is said to be composite" (Judson, p. 35).

# Prerequisites

- **Divisibility** — Composite numbers are defined by their divisors

# Key Properties

1. Has at least one divisor $d$ with $1 < d < n$
2. Can be written as a product $n = ab$ where $1 < a, b < n$
3. By the Fundamental Theorem of Arithmetic, every composite factors into primes

# Examples

**Example 1** (p. 36): $2^{2^5} + 1 = 4{,}294{,}967{,}297$ is composite (shown by Euler), disproving Fermat's conjecture.

**Example 2**: $12 = 2 \cdot 2 \cdot 3$ is composite with divisors 2, 3, 4, 6.

# Relationships

## Builds Upon
- **divisibility** — Defined by divisibility properties

## Related
- **fundamental-theorem-of-arithmetic** — Every composite factors uniquely into primes

## Contrasts With
- **prime-number** — Composites have more than two positive divisors

# Source Reference

Chapter 2: The Integers, Section 2.2, page 35.

# Verification Notes

- Definition source: Direct quote from p. 35
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
