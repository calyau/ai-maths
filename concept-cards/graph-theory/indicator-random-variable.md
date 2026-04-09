---
concept: Indicator Random Variable
slug: indicator-random-variable
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 304
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases:
  - "indicator variable"
prerequisites:
  - random-variable-on-gnp
  - expected-value
extends:
  []
related:
  - linearity-of-expectation
contrasts_with:
  []
answers_questions:
  - "What is Indicator Random Variable?"
---

# Quick Definition
An indicator random variable X_C for a subgraph C is a {0,1}-valued random variable: X_C(G) = 1 if C is a subgraph of G, 0 otherwise. Its expectation equals the probability P[C subset G].

# Core Definition
An *indicator random variable* X_C for a subgraph C maps G to 1 if C is a subgraph of G and to 0 otherwise. Since X_C takes only 1 as a positive value, E(X_C) = P[X_C = 1] = P[C subset G] (Diestel, p. 308).

# Prerequisites
- **random-variable-on-gnp** — Required for understanding Indicator Random Variable
- **expected-value** — Required for understanding Indicator Random Variable

# Key Properties
1. See Core Definition above

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 304.

# Verification Notes
- Definition from source
- Confidence: HIGH — explicit in source
