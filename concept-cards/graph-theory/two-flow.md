---
concept: 2-Flow
slug: two-flow
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 159
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "2-flow"
prerequisites:
  - k-flow
related:
  - even-graph
  - flow-number
answers_questions:
  - "When does a graph have a 2-flow?"
---

# Quick Definition
A graph has a 2-flow if and only if all its vertex degrees are even.

# Core Definition
**Proposition 6.4.1**: A graph has a 2-flow if and only if all its degrees are even. The proof uses Theorem 6.3.3: a graph has a 2-flow iff it has a Z_2-flow, which holds iff the constant map to 1-bar satisfies (F2), which requires all degrees to be even. (Diestel, p. 149)

# Prerequisites
- **k-flow** — A 2-flow is a k-flow with k = 2

# Key Properties
1. Characterization is purely in terms of vertex degrees
2. A graph with a 2-flow is called an "even graph" (all degrees even)
3. Simplest non-trivial case of k-flows

# Relationships
## Builds Upon
- **k-flow**

## Related
- **Even graph** — Graphs with all even degrees are exactly those admitting 2-flows

# Source Reference
Chapter 6: Flows, Section 6.4, Proposition 6.4.1, page 149 (pdf page 159).

# Verification Notes
- Confidence: HIGH — explicit characterization theorem
