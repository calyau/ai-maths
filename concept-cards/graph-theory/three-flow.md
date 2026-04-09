---
concept: 3-Flow
slug: three-flow
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 160
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "3-flow"
prerequisites:
  - k-flow
related:
  - two-flow
  - four-flow
  - three-flow-conjecture
answers_questions:
  - "When does a cubic graph have a 3-flow?"
---

# Quick Definition
A cubic graph has a 3-flow if and only if it is bipartite. For even n > 4, K^n has a 3-flow.

# Core Definition
**Proposition 6.4.2**: A cubic graph has a 3-flow if and only if it is bipartite. The proof shows that in a cubic graph with a Z_3-flow, consecutive edges on any cycle receive alternating values 1-bar and 2-bar, forcing even-length cycles. Conversely, a bipartite cubic graph with bipartition {X, Y} admits a Z_3-flow by assigning 1-bar from X to Y. (Diestel, p. 150)

**Proposition 6.4.3**: For all even n > 4, phi(K^n) = 3.

# Prerequisites
- **k-flow** — A 3-flow is a k-flow with k = 3

# Key Properties
1. A cubic graph has a 3-flow iff it is bipartite
2. K^n has flow number 3 for even n > 4
3. K^6 decomposes into two K^3 (with 2-flows) and a K_{3,3} (with 3-flow)

# Relationships
## Related
- **Three-flow conjecture** — Conjectures that every multigraph without 1- or 3-edge cuts has a 3-flow

# Source Reference
Chapter 6: Flows, Section 6.4, Propositions 6.4.2 and 6.4.3, pages 150-151 (pdf pages 160-161).

# Verification Notes
- Confidence: HIGH — characterization theorem with proof
