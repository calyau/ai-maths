---
# === CORE IDENTIFICATION ===
concept: Stirling's Formula
slug: stirlings-formula

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: analytic-tools
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 221
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Stirling's approximation

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erdos-lower-bound-ramsey
  - subgraph-count-expectation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What approximation is used for factorials in random graph calculations?"
---

# Quick Definition

Stirling's formula approximates $s!$ as $\sqrt{2\pi s}(s/e)^s$, enabling estimation of binomial coefficients in random graph calculations.

# Core Definition

Bollobás states the version used throughout the chapter: $\sqrt{2\pi s}(s/e)^s \le s! \le e^{1/12s}\sqrt{2\pi s}(s/e)^s$ (inequality (1), p. 221). In most cases, the weaker bound $s! \ge 2\sqrt{s}(s/e)^s \ge (s/e)^s$ suffices, yielding $\binom{n}{k} \le (en/k)^k$ (inequality (2), p. 222).

# Prerequisites

This is a foundational analytic tool with no prerequisites within this source.

# Key Properties

1. Lower bound: $s! \ge \sqrt{2\pi s}(s/e)^s$
2. Upper bound: $s! \le e^{1/12s}\sqrt{2\pi s}(s/e)^s$
3. Corollary: $\binom{n}{k} \le (en/k)^k$
4. Also used: $1 - x \le e^{-x}$, so $(1-x)^k \le e^{-kx}$ for $x < 1$, $k \ge 0$

# Construction / Recognition

Not applicable -- this is an analytic inequality.

# Context & Application

Stirling's formula is an essential tool in random graph estimates. It is used to bound binomial coefficients, which appear in every subgraph count computation. The inequality $(1-x)^k \le e^{-kx}$ (inequality (3)) is equally fundamental for converting probabilities involving $(1-p)$ into exponential form.

# Examples

**Example** (p. 225): In proving $R(s,s) > \frac{s}{e\sqrt{2}} 2^{s/2}$, Stirling's formula is used to verify that $\binom{n}{s}2^{-\binom{s}{2}+1} < 1$ for $n = \lfloor s 2^{s/2}/(e\sqrt{2})\rfloor$.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Erdos lower bound for Ramsey numbers** -- Uses Stirling to estimate binomials
- **Subgraph count expectation** -- Requires factorial estimates

## Related
- All random graph estimates involving binomial coefficients

## Contrasts With
- None

# Common Errors

- **Error**: Using the asymptotic form $s! \sim \sqrt{2\pi s}(s/e)^s$ when a bound is needed
  **Correction**: For proofs, use the explicit two-sided inequality, not the asymptotic equivalence

# Common Confusions

- **Confusion**: Thinking the approximation is only useful for large $s$
  **Clarification**: The bounds are valid for all positive integers $s$, though the relative error decreases with $s$

# Source Reference

Chapter VII: Random Graphs, inequality (1), page 221.

# Verification Notes

- Definition source: Direct from p. 221, inequality (1)
- Confidence rationale: Explicit inequality stated as preliminary
- Uncertainties: None
- Cross-reference status: Verified
