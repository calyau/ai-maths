---
concept: 4-Flow
slug: four-flow
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
  - "4-flow"
prerequisites:
  - k-flow
  - two-flow
  - even-graph
related:
  - three-flow
  - four-flow-conjecture
  - snark
answers_questions:
  - "When does a graph have a 4-flow?"
---

# Quick Definition
Every 4-edge-connected graph has a 4-flow. A graph has a 4-flow iff it is the union of two even subgraphs. A cubic graph has a 4-flow iff it is 3-edge-colourable.

# Core Definition
**Proposition 6.4.4**: Every 4-edge-connected graph has a 4-flow. The proof uses two edge-disjoint spanning trees and constructs a Z_4-flow by cycling around fundamental cycles with values 1-bar and 2-bar.

**Proposition 6.4.5**:
(i) A graph has a 4-flow if and only if it is the union of two even subgraphs.
(ii) A cubic graph has a 4-flow if and only if it is 3-edge-colourable.

Both use the Klein four-group Z_2^2 = Z_2 x Z_2: by Corollary 6.3.2, a graph has a 4-flow iff it has a Z_2^2-flow. (Diestel, pp. 150-152)

# Prerequisites
- **k-flow** — A 4-flow is a k-flow with k = 4
- **Two-flow** / **Even graph** — 4-flows decompose into two 2-flow-like components

# Key Properties
1. Every 4-edge-connected graph has a 4-flow
2. A graph has a 4-flow iff it is the union of two even subgraphs
3. A cubic graph has a 4-flow iff it is 3-edge-colourable
4. The Petersen graph has no 4-flow (since it is cubic but not 3-edge-colourable)

# Relationships
## Related
- **Four-flow conjecture** — Every bridgeless graph without Petersen minor has a 4-flow
- **Snark** — A cubic bridgeless graph without a 4-flow

# Source Reference
Chapter 6: Flows, Section 6.4, Propositions 6.4.4 and 6.4.5, pages 150-152 (pdf pages 160-162).

# Verification Notes
- Confidence: HIGH — multiple characterization theorems
