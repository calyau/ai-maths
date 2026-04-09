---
concept: First Moment Method
slug: first-moment-method
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
aliases:
  - "Markov method"
prerequisites:
  - markovs-inequality
  - expected-value
extends:
  - probabilistic-method
related:
  - second-moment-method
contrasts_with:
  - second-moment-method
answers_questions:
  - "What is the first moment method?"
  - "What distinguishes the first moment method from the second moment method?"
---

# Quick Definition
The first moment method uses Markov's inequality to show that if E(X) -> 0, then X = 0 almost surely. It proves properties are unlikely by bounding the expected count of witnesses.

# Core Definition
Since X >= 0, Markov's inequality gives P[X >= 1] <= E(X). If E(X) -> 0 as n -> infinity, then almost no G in G(n,p) satisfies X(G) >= 1. The expectation is much easier to calculate than probabilities because E(sum X_i) = sum E(X_i) regardless of independence (Diestel, p. 317).

# Prerequisites
- **Markov's inequality** — The key inequality
- **Expected value** — Must compute E(X)

# Key Properties
1. Only requires computing E(X), not analyzing correlations
2. Sufficient for the "below threshold" direction
3. Cannot prove properties hold (only that they fail)
4. The second moment method is needed for the complementary direction

# Context & Application
The first moment method is the easier half of threshold function proofs. It shows that below the threshold, the expected number of witnesses for a property tends to 0.

# Relationships
## Builds Upon
- **Markov's inequality** — The tool

## Contrasts With
- **Second moment method** — First moment shows failure; second moment shows success

# Source Reference
Chapter 11, Section 11.4, page 317.

# Verification Notes
- Description from p. 317
- Confidence: HIGH — explicitly described
