---
concept: "Chebyshev's Inequality"
slug: chebyshevs-inequality
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 318
section: "11.4 Threshold functions and second moments"
extraction_confidence: high
aliases:
  - "concentration inequality"
prerequisites:
  - variance
  - markovs-inequality
extends:
  - markovs-inequality
related:
  - second-moment-method
contrasts_with:
  - markovs-inequality
answers_questions:
  - "What is Chebyshev's inequality?"
  - "What distinguishes the first moment method from the second moment method?"
---

# Quick Definition
Chebyshev's inequality states that P[|X - mu| >= lambda] <= sigma^2/lambda^2 for all lambda > 0. It bounds the probability that a random variable deviates significantly from its mean.

# Core Definition
**Lemma 11.4.1** (Chebyshev's Inequality): For all real lambda > 0, P[|X - mu| >= lambda] <= sigma^2/lambda^2 (Diestel, p. 318). The proof follows from Markov's inequality applied to (X - mu)^2.

# Prerequisites
- **Variance** — sigma^2 appears in the bound
- **Markov's inequality** — Chebyshev follows from Markov applied to (X-mu)^2

# Key Properties
1. Provides a two-sided bound (X can be too large or too small)
2. Stronger than Markov when X can take large values
3. If sigma^2/mu^2 -> 0, then X > 0 almost surely (Lemma 11.4.2)
4. The key tool for the second moment method

# Context & Application
Chebyshev's inequality is the foundation of the second moment method. While Markov's inequality suffices to show a property is unlikely (first moment), Chebyshev's inequality shows a property is likely by proving the random variable concentrates around its (positive) mean.

# Relationships
## Builds Upon
- **Markov's inequality** — Chebyshev's is derived from Markov's

## Enables
- **Second moment method** — The main application

## Contrasts With
- **Markov's inequality** — Markov gives one-sided bounds; Chebyshev gives concentration

# Source Reference
Chapter 11, Section 11.4, page 318 (Lemma 11.4.1).

# Verification Notes
- Statement from p. 318
- Confidence: HIGH — named lemma with proof
