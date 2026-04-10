---
# === CORE IDENTIFICATION ===
concept: Markov's Inequality
slug: markovs-inequality

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: concentration-inequalities
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 238
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - first moment inequality

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - chebyshevs-inequality
  - expectation-method
contrasts_with:
  - chebyshevs-inequality

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding random graph phase transitions?"
---

# Quick Definition

For a non-negative random variable $X$ with expectation $\mu$, Markov's inequality states $\mathbb{P}(X \ge c\mu) \le 1/c$ for $c > 1$.

# Core Definition

If $X$ is a non-negative variable on $\mathcal{G}(n, M)$ or $\mathcal{G}(n, p)$ with $\mathbb{E}(X) = \mu$, then for $c > 1$: $\mathbb{P}(X \ge c\mu) \le 1/c$ and $\mathbb{P}(X \le c\mu) \ge (c-1)/c$, since $\mu = \mathbb{E}(X) \ge \mathbb{P}(X \ge c\mu) \cdot c\mu$ (Bollobás, p. 238).

# Prerequisites

This is a foundational probabilistic tool with no prerequisites within this source.

# Key Properties

1. If $\mathbb{E}(X)$ is very small, then $X$ is small for most graphs
2. Only gives upper bounds on tail probabilities
3. Cannot be used alone to show $X > 0$ for most graphs
4. Used "over and over again" in Section VII.1

# Construction / Recognition

Not applicable -- this is a probability inequality.

# Context & Application

Markov's inequality is the formal basis of the expectation method. While simple, it suffices for many existence proofs. Its limitation is that it cannot show that $X$ is large for most graphs; the variance method (Chebyshev's inequality) is needed for that.

# Examples

**Example** (p. 238): If $X$ counts copies of $K_s$ and $\mathbb{E}(X) < 1$, then $\mathbb{P}(X \ge 1) < 1$, so $\mathbb{P}(X = 0) > 0$.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Expectation method** -- Formal justification for the first moment method

## Related
- **Chebyshev's inequality** -- The second moment analogue

## Contrasts With
- **Chebyshev's inequality** -- Uses variance for tighter two-sided bounds

# Common Errors

- **Error**: Using Markov's inequality to prove $\mathbb{P}(X > 0) \to 1$
  **Correction**: Markov only shows $\mathbb{P}(X \ge c\mu) \le 1/c$; for $\mathbb{P}(X > 0) \to 1$, use Chebyshev

# Common Confusions

- **Confusion**: Thinking Markov's inequality is only useful for discrete variables
  **Clarification**: It applies to any non-negative random variable

# Source Reference

Chapter VII: Random Graphs, Section VII.3, page 238.

# Verification Notes

- Definition source: Direct from p. 238
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
