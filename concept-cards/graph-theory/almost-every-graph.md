---
concept: Almost Every Graph
slug: almost-every-graph
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 312
section: "11.3 Properties of almost all graphs"
extraction_confidence: high
aliases:
  - "almost surely"
  - "almost all graphs"
prerequisites:
  - random-graph-gnp
extends: []
related:
  - threshold-function
  - monotone-property
contrasts_with: []
answers_questions:
  - "What does 'almost every graph' mean in random graph theory?"
---

# Quick Definition
A graph property P holds for almost every G in G(n,p) if the probability P[G in P] tends to 1 as n -> infinity. Equivalently, almost no G has property P if P[G in P] -> 0.

# Core Definition
If p = p(n) is a fixed function and P is a graph property, we say that G has P for *almost all* (or *almost every*) G in G(n,p), or that G has P *almost surely*, if P[G in P] -> 1 as n -> infinity. If P[G in P] -> 0, we say that *almost no* G has P (Diestel, p. 312).

# Prerequisites
- **Random graph G(n,p)** — The probability space

# Key Properties
1. For constant p in (0,1), almost every G contains any fixed graph H as induced subgraph (Proposition 11.3.1)
2. For constant p, almost every G is k-connected for any fixed k (Corollary 11.3.3)
3. For constant p, almost every G has chromatic number ~ (log(1/q))/(2) * n/log(n) (Proposition 11.3.4)
4. Any first-order sentence about graphs is almost surely true or almost surely false for constant p

# Context & Application
The "almost all" framework provides a powerful lens for understanding typical graph structure. Many graph properties exhibit sharp transitions: below a threshold, almost no graph has the property; above it, almost every graph does.

# Examples
**Example 1** (p. 312): For constant p, every fixed graph H is an induced subgraph of almost every G.

**Example 2** (p. 314): Almost every G in G(n,p) has chi(G) > (log(1/q))/(2+epsilon) * n/log(n).

# Relationships
## Enables
- **Threshold function** — Critical p values for "almost all" transitions

# Source Reference
Chapter 11, Section 11.3, pages 312-316.

# Verification Notes
- Definition from p. 312
- Confidence: HIGH — explicit definition
