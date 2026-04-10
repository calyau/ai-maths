---
# === CORE IDENTIFICATION ===
concept: Chebyshev's Inequality
slug: chebyshevs-inequality

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
  - second moment inequality
  - Chebyshev bound

# === TYPED RELATIONSHIPS ===
prerequisites:
  - markovs-inequality
extends:
  - markovs-inequality
related:
  - variance-method
contrasts_with:
  - markovs-inequality

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I show a random variable is concentrated near its mean?"
  - "What must I know before understanding random graph phase transitions?"
---

# Quick Definition

Chebyshev's inequality states $\mathbb{P}(|X - \mu| \ge a) \le \sigma^2/a^2$ for any $a > 0$, where $\mu = \mathbb{E}(X)$ and $\sigma^2 = \text{Var}(X)$. In particular, $\mathbb{P}(X = 0) \le \sigma^2/\mu^2$.

# Core Definition

If $\mu = \mathbb{E}(X)$ is the expectation and $\sigma^2 = \mathbb{E}((X-\mu)^2) = \mathbb{E}(X^2) - \mu^2$ is the variance, then Chebyshev's inequality (Markov's inequality applied to $(X-\mu)^2$) states: for $a > 0$, $\mathbb{P}(|X - \mu| \ge a) \le \sigma^2/a^2$. In particular, $\mathbb{P}(X = 0) \le \mathbb{P}(|X - \mu| \ge \mu) \le \sigma^2/\mu^2$ (inequality (13), Bollobás, p. 238).

# Prerequisites

- **Markov's inequality** -- Chebyshev is Markov applied to $(X-\mu)^2$

# Key Properties

1. Gives two-sided concentration: $X$ is close to $\mu$ with high probability if $\sigma^2/\mu^2 \to 0$
2. In particular, $\mathbb{P}(X = 0) \le \sigma^2/\mu^2$, so if $\sigma = o(\mu)$, then $\mathbb{P}(X > 0) \to 1$
3. The key computation is bounding $\mathbb{E}(X^2) = \sum_{i,j} \mathbb{E}(Y_i Y_j)$

# Construction / Recognition

## To Apply Chebyshev for $\mathbb{P}(X > 0) \to 1$
1. Compute $\mu = \mathbb{E}(X) = \sum_i \mathbb{E}(Y_i)$
2. Compute $\mathbb{E}(X^2) = \sum_{i,j} \mathbb{P}(G \supset F_i \cup F_j)$
3. Verify $\sigma^2/\mu^2 = \mathbb{E}(X^2)/\mu^2 - 1 \to 0$
4. Conclude $\mathbb{P}(X = 0) \to 0$

# Context & Application

Chebyshev's inequality is the main tool in the "second moment method" or "variance method." It enables proving that random variables are concentrated near their means, and in particular that $X > 0$ almost surely when the expectation is large and the variance is small relative to the square of the mean.

# Examples

**Example** (p. 239): For balanced graphs $F$ with $k$ vertices and $\ell$ edges, $\mathbb{P}(X = 0) \le c_4\gamma^{-1} \to 0$ as $\gamma = p \cdot n^{k/\ell} \to \infty$, proving a.e. $G_{n,p}$ contains $F$.

# Relationships

## Builds Upon
- **Markov's inequality** -- Chebyshev is a consequence

## Enables
- **Variance method** -- The general technique based on Chebyshev
- **Balanced graph threshold** -- Uses Chebyshev to prove a.e. containment
- **Clique number of random graph** -- Concentration via second moment

## Related
- **Variance method** -- Synonymous application

## Contrasts With
- **Markov's inequality** -- Markov only gives one-sided bounds; Chebyshev gives concentration

# Common Errors

- **Error**: Applying Chebyshev with $\mu \to 0$
  **Correction**: Chebyshev is useful when $\mu \to \infty$; for $\mu \to 0$, use Markov directly

# Common Confusions

- **Confusion**: Thinking Chebyshev requires independence of the $Y_i$
  **Clarification**: Chebyshev applies to any random variable; independence simplifies variance computation but is not required

# Source Reference

Chapter VII: Random Graphs, Section VII.3, inequality (13), page 238.

# Verification Notes

- Definition source: Direct from p. 238, inequality (13)
- Confidence rationale: Explicit statement with derivation
- Uncertainties: None
- Cross-reference status: Verified
