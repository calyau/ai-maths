---
# === CORE IDENTIFICATION ===
concept: Binomial Theorem
slug: binomial-theorem

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
pdf_page: 31
section: "Mathematical Induction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-induction
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The Binomial Theorem states that $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$ for real numbers $a, b$ and positive integer $n$.

# Core Definition

**Example 2.4**: "We will prove the binomial theorem using mathematical induction; that is, $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$, where $a$ and $b$ are real numbers, $n \in \mathbb{N}$, and $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient" (Judson, p. 31).

# Prerequisites

- **Mathematical induction** — Proof uses induction

# Key Properties

1. $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ (binomial coefficient)
2. Pascal's identity: $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$
3. Proved by induction on $n$
4. Special cases: $(a+b)^2 = a^2 + 2ab + b^2$

# Context & Application

The Binomial Theorem is used as an example of proof by induction and appears in various algebraic arguments. It also connects to the binomial coefficients which have combinatorial significance.

# Examples

**Example 1** (p. 31-32): The proof proceeds by induction, using Pascal's identity to combine terms in the inductive step.

# Relationships

## Builds Upon
- **mathematical-induction** — Proved by induction

# Source Reference

Chapter 2: The Integers, Section 2.1, Example 2.4, pages 31-32.

# Verification Notes

- Definition source: Direct from Example 2.4, p. 31
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
