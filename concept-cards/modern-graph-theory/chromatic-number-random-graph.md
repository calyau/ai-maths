---
# === CORE IDENTIFICATION ===
concept: Chromatic Number of a Random Graph
slug: chromatic-number-random-graph

# === CLASSIFICATION ===
category: random-graphs
subcategory: graph-invariants
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 242
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clique-number-random-graph
extends: []
related:
  - chromatic-number-eigenvalue-bound
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the chromatic number of a typical random graph?"
---

# Quick Definition

For fixed $0 < p < 1$, the chromatic number of almost every $G_{n,p}$ is $(\frac{1}{2} + o(1))\frac{\log n}{\log(1/q)}$, where $q = 1 - p$.

# Core Definition

**Theorem 10** (Bollobás, p. 243): Let $0 < p < 1$ be constant. Then $\chi(G_{n,p}) = (\frac{1}{2} + o(1))\frac{\log n}{\log(1/q)}$ for a.e. $G_{n,p}$, where $q = 1-p$. The lower bound follows from $\chi \ge n/\alpha$ and the clique number result for complements. The matching upper bound was proved by Bollobás in 1988 using a non-algorithmic approach.

# Prerequisites

- **Clique number of random graph** -- Lower bound via $\chi \ge n/\alpha$

# Key Properties

1. The chromatic number grows as $\Theta(n/\log n)$ for fixed $p$
2. The greedy algorithm gives a factor-2 approximation
3. The exact asymptotic $\chi \sim \frac{n}{2\log_b n}$ (where $b = 1/q$) was established by Bollobás (1988)
4. The trivial lower bound from independence number turns out to be tight

# Construction / Recognition

## Derivation of the Lower Bound
1. The complement $\overline{G_{n,p}}$ is $G_{n,q}$ with $q = 1-p$
2. $\alpha(G_{n,p}) = \omega(G_{n,q}) \sim 2\log_{1/q} n$
3. Therefore $\chi(G_{n,p}) \ge n/\alpha(G_{n,p}) \sim \frac{n}{2\log_{1/q} n} = \frac{\log n}{2\log(1/q)} \cdot \frac{n}{\log n \cdot \frac{1}{\log(1/q)}}$

# Context & Application

The asymptotic chromatic number of random graphs was a major open problem for many years. The greedy algorithm was shown by Bollobás and Erdos (1976) to use about $n/\log_b n$ colors, which is only a factor 2 from optimal.

# Examples

**Example** (p. 243): For $p = 1/2$, $q = 1/2$, so $\chi(G_{n,1/2}) \sim \frac{n}{2\log_2 n}$.

# Relationships

## Builds Upon
- **Clique number of random graph** -- Lower bound via complement

## Enables
- Further research on algorithmic graph coloring

## Related
- **Chromatic number eigenvalue bound** -- Algebraic bounds on chromatic number

## Contrasts With
- None

# Common Errors

- **Error**: Thinking greedy coloring is optimal for random graphs
  **Correction**: Greedy uses $\sim n/\log_b n$ colors, while the optimum is $\sim n/(2\log_b n)$

# Common Confusions

- **Confusion**: Thinking high chromatic number means many short cycles
  **Clarification**: Random graphs have high chromatic number due to complex long-range structure, not local density

# Source Reference

Chapter VII: Random Graphs, Section VII.3, Theorem 10, pages 242--243.

# Verification Notes

- Definition source: Direct from Theorem 10, p. 243
- Confidence rationale: Explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
