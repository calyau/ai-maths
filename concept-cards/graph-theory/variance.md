---
concept: Variance
slug: variance
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
  - "second moment"
  - "sigma^2"
prerequisites:
  - expected-value
  - random-variable-on-gnp
extends:
  - expected-value
related:
  - chebyshevs-inequality
  - second-moment-method
contrasts_with: []
answers_questions:
  - "What is the variance of a random variable on G(n,p)?"
---

# Quick Definition
The variance sigma^2 of a random variable X is E((X - mu)^2) = E(X^2) - mu^2, where mu = E(X). It measures how much X deviates from its mean.

# Core Definition
Given a random variable X on G(n,p) with mean mu = E(X), the *variance* (or *second moment*) of X is sigma^2 := E((X - mu)^2). By linearity, sigma^2 = E(X^2) - mu^2. Both mu and sigma^2 are functions of n (Diestel, p. 318).

# Prerequisites
- **Expected value** — Variance is defined in terms of expectation
- **Random variable on G(n,p)** — Variance is a property of random variables

# Key Properties
1. sigma^2 >= 0 always
2. sigma^2 = 0 iff X is constant
3. sigma^2 = E(X^2) - (E(X))^2
4. Small variance relative to the mean implies concentration around the mean

# Relationships
## Enables
- **Chebyshev's inequality** — P[|X - mu| >= lambda] <= sigma^2/lambda^2
- **Second moment method** — If sigma^2/mu^2 -> 0, then X > 0 almost surely

# Source Reference
Chapter 11, Section 11.4, page 318.

# Verification Notes
- Definition from p. 318
- Confidence: HIGH — standard definition
