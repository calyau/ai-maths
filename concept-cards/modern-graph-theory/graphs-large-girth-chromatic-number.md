---
# === CORE IDENTIFICATION ===
concept: Graphs of Large Girth and Chromatic Number
slug: graphs-large-girth-chromatic-number

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: existence-proofs
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 232
section: "VII.1 The Basic Models—The Use of the Expectation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Erdos girth-chromatic number theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expectation-method
  - gnp-model
extends:
  - probabilistic-method
related:
  - erdos-lower-bound-ramsey
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can graphs have both large girth and large chromatic number?"
  - "How does the probabilistic method prove existence of graphs with surprising properties?"
---

# Quick Definition

Erdos proved that for any natural numbers $g \ge 3$ and $k \ge 2$, there exists a graph of order $k^{3g}$, girth at least $g$, and chromatic number at least $k$, using a combination of expectation bounds and a deletion argument.

# Core Definition

**Theorem 4** (Bollobás, p. 232): Given natural numbers $g \ge 3$ and $k \ge 2$, there is a graph of order $k^{3g}$, girth at least $g$ and chromatic number at least $k$. The proof sets $n = k^{3g}$, $p = 2k^{2-3g}$, and considers $\mathcal{G}(n, p)$. Two events are shown to hold simultaneously with positive probability: (1) the graph has few short cycles (at most $f = 2^{g-1}k^{2g-2}$), and (2) every large independent set spans many edges. Deleting one edge per short cycle yields the desired graph.

# Prerequisites

- **Expectation method** -- Used to bound the number of short cycles
- **G(n,p) model** -- The probability space

# Key Properties

1. Combines expectation bounds with a deletion argument
2. Shows $\mathbb{P}(\Omega_1) > 2/3$ (few short cycles) and $\mathbb{P}(\Omega_2) > 2/3$ (no large sparse sets)
3. Since both have probability $> 2/3$, their intersection is non-empty
4. The bound $n_1(g, k) \le k^{3g}$ on the minimum order is not known to be tight

# Construction / Recognition

## Proof Strategy
1. Show that $\mathbb{E}(\text{short cycles}) < f/3$, so with probability $> 2/3$ there are at most $f$ short cycles
2. Show that $\mathbb{E}(I) < 1/3$, where $I$ counts $s$-sets of vertices spanning at most $f$ edges
3. Find a graph $G_0$ in both events; delete one edge per short cycle
4. Resulting graph $G$ has girth $\ge g$ and $\alpha(G) < n/k$, so $\chi(G) > k$

# Context & Application

This theorem demonstrates that high girth and high chromatic number are not contradictory, despite the intuition that few short cycles should make coloring easier. It is one of the most surprising applications of the probabilistic method.

# Examples

**Example** (p. 232): Setting $g = 4$ and $k = 4$ gives existence of a graph of order $4^{12}$ with girth $\ge 4$ and $\chi \ge 4$.

# Relationships

## Builds Upon
- **Expectation method** -- Bounds on expected number of short cycles
- **G(n,p) model** -- Probability space with $p = 2k^{2-3g}$

## Enables
- Research on the function $n_1(g, k)$

## Related
- **Erdos lower bound for Ramsey numbers** -- Another striking application of the probabilistic method

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the deletion step and claiming the random graph directly has large girth
  **Correction**: The random graph has few short cycles but not zero; edges must be deleted to achieve girth $\ge g$

# Common Confusions

- **Confusion**: Thinking high girth implies low chromatic number
  **Clarification**: This theorem shows exactly the opposite: arbitrarily high girth is compatible with arbitrarily high chromatic number

# Source Reference

Chapter VII: Random Graphs, Section VII.1, Theorem 4, pages 232--234.

# Verification Notes

- Definition source: Direct from Theorem 4, p. 232
- Confidence rationale: Explicit theorem with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
