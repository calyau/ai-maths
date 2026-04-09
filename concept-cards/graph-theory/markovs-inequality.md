---
concept: Markov's Inequality
slug: markovs-inequality
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
  - "first moment method"
prerequisites:
  - expected-value
  - random-variable-on-gnp
extends:
  []
related:
  - chebyshevs-inequality
contrasts_with:
  - probabilistic-method
answers_questions:
  - "What is Markov's Inequality?"
---

# Quick Definition
Markov's inequality states that for a non-negative random variable X and a > 0: P[X >= a] <= E(X)/a. It is the basis of the first moment method.

# Core Definition
**Lemma 11.1.4** (Markov's Inequality): Let X >= 0 be a random variable on G(n,p) and a > 0. Then P[X >= a] <= E(X)/a (Diestel, p. 307).

# Prerequisites
- **expected-value** — Required for understanding Markov's Inequality
- **random-variable-on-gnp** — Required for understanding Markov's Inequality

# Key Properties
1. See Core Definition above

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 307.

# Verification Notes
- Definition from source
- Confidence: HIGH — explicit in source
