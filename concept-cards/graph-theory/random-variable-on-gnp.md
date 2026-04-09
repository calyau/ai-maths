---
concept: Random Variable on G(n,p)
slug: random-variable-on-gnp
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
  - "graph random variable"
prerequisites:
  - random-graph-gnp
extends: []
related:
  - expected-value
  - indicator-random-variable
  - variance
contrasts_with: []
answers_questions:
  - "What is a random variable on a random graph?"
---

# Quick Definition
A random variable on G(n,p) is a non-negative function X: G(n,p) -> [0, infinity) that assigns a numerical value to each graph in the probability space. Graph invariants like degree, girth, and chromatic number are natural random variables.

# Core Definition
In the context of random graphs, each of the familiar graph invariants (like average degree, connectivity, girth, chromatic number, etc.) may be interpreted as a non-negative random variable on G(n,p), a function X: G(n,p) -> [0, infinity) (Diestel, p. 307).

# Prerequisites
- **Random graph G(n,p)** — The probability space on which random variables are defined

# Key Properties
1. The expectation E(X) = sum over G in G(n,p) of P({G}) * X(G)
2. The expectation operator E is linear: E(X+Y) = E(X) + E(Y)
3. If X counts subgraphs from a set H, then E(X) = sum over H in H of P[H subset G]
4. Indicator random variables take values in {0, 1}

# Context & Application
Random variables allow quantitative analysis of random graph properties. The linearity of expectation is especially powerful: it allows computing expected values of complex random variables by decomposing them into indicator random variables.

# Examples
**Example 1** (pp. 307-308, Lemma 11.1.5): The expected number of k-cycles in G(n,p) is (n)_k / (2k) * p^k.

# Relationships
## Enables
- **Expected value** computations
- **Markov's inequality** and **Chebyshev's inequality**

# Source Reference
Chapter 11, Section 11.1, pages 307-308.

# Verification Notes
- Definition from p. 307
- Confidence: HIGH — explicit definition
