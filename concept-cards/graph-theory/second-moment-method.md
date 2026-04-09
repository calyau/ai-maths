---
concept: Second Moment Method
slug: second-moment-method
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 317
section: "11.4 Threshold functions and second moments"
extraction_confidence: high
aliases: []
prerequisites:
  - chebyshevs-inequality
  - variance
  - expected-value
extends:
  - probabilistic-method
related:
  - first-moment-method
  - threshold-function
  - erdos-renyi-threshold-theorem
contrasts_with:
  - first-moment-method
answers_questions:
  - "What is the second moment method?"
  - "What distinguishes the first moment method from the second moment method?"
---

# Quick Definition
The second moment method uses Chebyshev's inequality to show that a random variable X is positive almost surely: if mu > 0 and sigma^2/mu^2 -> 0, then P[X > 0] -> 1.

# Core Definition
The second moment method proves that X(G) >= 1 for almost all G in G(n,p). By Chebyshev's inequality with lambda = mu: P[X = 0] <= sigma^2/mu^2. If mu > 0 for large n and sigma^2/mu^2 -> 0, then X > 0 almost surely (Lemma 11.4.2, Diestel, p. 318).

# Prerequisites
- **Chebyshev's inequality** — The key inequality
- **Variance** — Must compute sigma^2 = E(X^2) - mu^2
- **Expected value** — Must compute mu = E(X)

# Key Properties
1. The main challenge is bounding E(X^2): this requires analyzing correlations between pairs of substructures
2. E(X^2) = sum of P[H' union H'' subset G] over all pairs (H', H'')
3. The sum is partitioned by |H' cap H''| = i for i = 0, ..., k
4. For i = 0 (disjoint): contributes at most mu^2
5. For i >= 1: contributes A_i which must be shown o(mu^2)

# Context & Application
The second moment method complements the first moment method. Together they prove threshold functions: first moment shows the property fails below the threshold; second moment shows it holds above. Computing E(X^2) is the hard part, requiring careful analysis of how subgraph copies overlap.

# Examples
**Example 1** (pp. 319-322, Theorem 11.4.3): Complete proof that t(n) = n^{-k/l} is a threshold for containing a balanced graph H with k vertices and l edges.

# Relationships
## Builds Upon
- **Chebyshev's inequality** — The core tool

## Enables
- **Erdős-Rényi threshold theorem** — Threshold functions via second moments

## Contrasts With
- **First moment method** — First moment shows property fails; second moment shows it holds

# Common Confusions
- **Confusion**: Thinking large E(X) implies X > 0 for most G
  **Clarification**: E(X) can be large because X is enormous on a few G; must also bound sigma^2

# Source Reference
Chapter 11, Section 11.4, pages 317-322.

# Verification Notes
- Method described on pp. 317-318, applied in Theorem 11.4.3
- Confidence: HIGH — full exposition with worked example
