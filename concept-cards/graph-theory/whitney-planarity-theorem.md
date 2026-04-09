---
concept: "Whitney's Planarity Theorem"
slug: whitney-planarity-theorem
category: planar-graphs
subcategory: plane-duality
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.6 Plane duality"
extraction_confidence: high
aliases:
  - "Theorem 4.6.3"
  - "Whitney 1933"
prerequisites:
  - abstract-dual
  - maclane-theorem
extends: []
related:
  - kuratowski-theorem
  - plane-dual
contrasts_with: []
answers_questions:
  - "When does a graph have an abstract dual?"
  - "How does duality characterize planarity?"
---

# Quick Definition
Whitney's planarity theorem states that a graph is planar if and only if it has an abstract dual.

# Core Definition
**Theorem 4.6.3** (Whitney 1933): "A graph is planar if and only if it has an abstract dual" (Diestel, p. 105).

# Prerequisites
- **Abstract dual** -- The existence of an abstract dual characterizes planarity
- **MacLane's theorem** -- Used in the proof

# Key Properties
1. Planarity <-> existence of an abstract dual
2. Forward: plane duals provide abstract duals
3. Backward: abstract dual implies cycle space has simple basis (via Proposition 1.9.3), hence planar by MacLane's theorem

# Context & Application
Whitney's theorem provides yet another characterization of planarity, this time through algebraic duality. It shows that the notion of an abstract dual, which could have been defined purely from algebraic considerations (cycle-bond interchange), turns out to coincide exactly with the topological property of planarity.

# Relationships
## Builds Upon
- **Abstract dual**, **MacLane's theorem**

## Related
- **Kuratowski's theorem** -- Alternative forbidden-minor characterization
- **Plane dual** -- Geometric version of the dual concept

# Source Reference
Chapter 4, Section 4.6, Theorem 4.6.3, pages 105-106.

# Verification Notes
- Theorem statement quoted from p. 105
- Confidence: HIGH -- named classical theorem
