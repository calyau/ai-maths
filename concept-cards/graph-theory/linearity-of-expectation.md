---
concept: Linearity of Expectation
slug: linearity-of-expectation
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
  []
prerequisites:
  - expected-value
  - indicator-random-variable
extends:
  []
related:
  - probabilistic-method
contrasts_with:
  []
answers_questions:
  - "What is Linearity of Expectation?"
---

# Quick Definition
Linearity of expectation states E(X+Y) = E(X) + E(Y) for any random variables X, Y, regardless of independence. This allows computing expected values of complex random variables by summing expectations of indicator variables.

# Core Definition
The expectation operator E is linear: E(X+Y) = E(X) + E(Y) and E(lambda X) = lambda E(X) for any random variables X, Y and lambda in R. This holds without any independence assumption (Diestel, p. 307).

# Prerequisites
- **expected-value** — Required for understanding Linearity of Expectation
- **indicator-random-variable** — Required for understanding Linearity of Expectation

# Key Properties
1. See Core Definition above

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 307.

# Verification Notes
- Definition from source
- Confidence: HIGH — explicit in source
