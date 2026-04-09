---
concept: Threshold Function
slug: threshold-function
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 315
section: "11.3 Properties of almost all graphs"
extraction_confidence: high
aliases:
  - "threshold"
  - "sharp threshold"
prerequisites:
  - almost-every-graph
  - random-graph-gnp
extends: []
related:
  - monotone-property
  - second-moment-method
  - erdos-renyi-threshold-theorem
contrasts_with: []
answers_questions:
  - "What is a threshold function for a graph property?"
  - "What distinguishes the first moment method from the second moment method?"
---

# Quick Definition
A function t = t(n) is a threshold function for a graph property P if P[G in P] -> 0 when p/t -> 0 and P[G in P] -> 1 when p/t -> infinity, as n -> infinity. Threshold functions are unique up to a multiplicative constant.

# Core Definition
A real function t = t(n) with t(n) != 0 for all n is a *threshold function* for a graph property P if for all p = p(n) and G in G(n,p): P[G in P] -> 0 if p/t -> 0, and P[G in P] -> 1 if p/t -> infinity, as n -> infinity. If P has a threshold function t, then any positive multiple ct is also a threshold function; thus threshold functions are unique up to a multiplicative constant (Diestel, p. 315).

# Prerequisites
- **Almost every graph** — Threshold functions describe the transition
- **Random graph G(n,p)** — The model

# Key Properties
1. Threshold functions are unique only up to a multiplicative constant
2. All increasing (non-trivial) graph properties have threshold functions (Bollobás-Thomason, 1987)
3. Below the threshold: almost no graph has the property
4. Above the threshold: almost every graph has the property
5. For balanced H with k vertices and l edges: t(n) = n^{-k/l} is the threshold for containing H

# Context & Application
Threshold functions describe the "evolution" of random graphs: as p grows, graphs acquire more structure. The evolution happens in relatively sudden jumps at thresholds. Key thresholds: first edges near p ~ n^{-2}, first cycles near p ~ n^{-1}, connectivity near p ~ (log n)n^{-1}, Hamiltonicity near p ~ (1+epsilon)(log n)n^{-1}.

# Examples
**Example 1** (Corollary 11.4.4): t(n) = n^{-1} is a threshold for containing a k-cycle (any fixed k >= 3).

**Example 2** (Corollary 11.4.5): t(n) = n^{-k/(k-1)} is a threshold for containing a tree of order k.

**Example 3** (Corollary 11.4.6): t(n) = n^{-2/(k-1)} is a threshold for containing K^k.

# Relationships
## Builds Upon
- **Almost every graph** — Threshold separates "almost none" from "almost all"

## Related
- **Second moment method** — Used to prove the upper part (property holds a.s.)
- **First moment method** — Used to prove the lower part (property fails a.s.)

# Source Reference
Chapter 11, Section 11.3, pages 315-316; Section 11.4, pages 317-322.

# Verification Notes
- Definition from p. 315
- Confidence: HIGH — explicit definition with extensive examples
