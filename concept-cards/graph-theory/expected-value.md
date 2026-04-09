---
concept: Expected Value
slug: expected-value
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 307
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases:
  - "mean"
  - "expectation"
  - "E(X)"
prerequisites:
  - random-variable-on-gnp
  - random-graph-gnp
extends: []
related:
  - linearity-of-expectation
  - markovs-inequality
  - variance
contrasts_with: []
answers_questions:
  - "What is the expected value of a random variable on G(n,p)?"
---

# Quick Definition
The expected value (or mean) of a random variable X on G(n,p) is E(X) = sum over G in G(n,p) of P({G}) * X(G). The expectation operator E is linear.

# Core Definition
The mean or *expected value* of a random variable X on G(n,p) is E(X) := sum_{G in G(n,p)} P({G}) * X(G). The operator E is *linear*: E(X+Y) = E(X) + E(Y) and E(lambda X) = lambda E(X) for any two random variables X, Y and lambda in R (Diestel, p. 307).

# Prerequisites
- **Random variable on G(n,p)** — Expected value is a property of random variables
- **Random graph G(n,p)** — The probability space

# Key Properties
1. Linearity: E(X+Y) = E(X) + E(Y), without requiring independence
2. If E(X) < a, then at least one graph G has X(G) < a
3. Can be computed by double counting: swap order of summation over graphs and subgraphs
4. The expected number of copies of H with l edges in G(n,p) involves p^l

# Context & Application
Computing expected values is the primary tool for the first moment method. If E(X) is small, then X(G) must be small for many G, enabling existence proofs. The linearity of expectation is particularly powerful because it does not require independence.

# Examples
**Example 1** (p. 308, Lemma 11.1.5): E(number of k-cycles) = (n)_k / (2k) * p^k.

# Relationships
## Enables
- **Markov's inequality** — P[X >= a] <= E(X)/a
- **First moment method** — If E(X) -> 0, then X = 0 almost surely

## Related
- **Variance** — E((X - mu)^2), the second moment

# Source Reference
Chapter 11, Section 11.1, page 307.

# Verification Notes
- Definition from p. 307
- Confidence: HIGH — standard definition given explicitly
