---
concept: Infinite Random Graph Theorem
slug: infinite-random-graph-theorem
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 316
section: "11.3 Properties of almost all graphs"
extraction_confidence: high
aliases:
  - "Erdős-Rényi 1963"
prerequisites:
  - rado-graph
  - random-graph-gnp
extends: []
related:
  - almost-every-graph
contrasts_with: []
answers_questions:
  - "What happens when you generate an infinite random graph?"
---

# Quick Definition
With probability 1, a random graph G in G(aleph_0, p) with 0 < p < 1 is isomorphic to the Rado graph R (Erdős and Rényi, 1963).

# Core Definition
**Theorem 11.3.5** (Erdős and Rényi 1963): With probability 1, a random graph G in G(aleph_0, p) with 0 < p < 1 is isomorphic to the Rado graph R (Diestel, p. 316).

# Prerequisites
- **Rado graph** — The unique graph that almost surely appears
- **Random graph G(n,p)** — Extended to infinite vertex sets

# Key Properties
1. For each disjoint finite U, W, the probability that no vertex witnesses property (*) is 0
2. By countable union of measure-0 events, (*) holds almost surely
3. By uniqueness of R, the random graph is almost surely isomorphic to R
4. The result holds for any constant p in (0,1)

# Context & Application
This theorem reveals that infinite random graphs are, paradoxically, completely determined up to isomorphism. The uniqueness holds only up to isomorphism; the symmetry glosses over the actual variety.

# Relationships
## Builds Upon
- **Rado graph** — The target of the isomorphism

# Source Reference
Chapter 11, Section 11.3, pages 316-317 (Theorem 11.3.5).

# Verification Notes
- Statement and proof from pp. 316-317
- Confidence: HIGH — named theorem with proof
