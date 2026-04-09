---
concept: Snark
slug: snark
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 167
section: "6.6 Tutte's flow conjectures"
extraction_confidence: high
aliases:
  - "snark graph"
prerequisites:
  - four-flow
  - k-flow
related:
  - four-flow-conjecture
  - five-flow-conjecture
answers_questions:
  - "What is a snark?"
---

# Quick Definition
A snark is a cubic bridgeless graph (or multigraph) without a 4-flow, equivalently without a 3-edge-colouring.

# Core Definition
A **snark** is a cubic bridgeless graph or multigraph without a 4-flow (equivalently, without a 3-edge-colouring, by Proposition 6.4.5(ii)). The Petersen graph is the smallest snark. (Diestel, p. 157)

# Prerequisites
- **Four-flow** — A snark is defined by the absence of a 4-flow
- **k-flow** — Understanding what flows are

# Key Properties
1. Cubic (3-regular) and bridgeless
2. Not 3-edge-colourable (by Proposition 6.4.5)
3. The Petersen graph is the prototypical and smallest snark
4. Snarks form the "hard core" of both the four colour theorem and the 5-flow conjecture
5. The four colour theorem is equivalent to the non-existence of planar snarks
6. The 4-flow conjecture for cubic graphs says every snark contains the Petersen graph as a minor

# Context & Application
Snarks are the difficult cases for several major conjectures in graph theory. They are rare and hard to construct, yet no known structural characterization makes the associated conjectures tractable. The name references Lewis Carroll's "The Hunting of the Snark" (1876).

# Examples
**Example** (p. 157, Fig. 6.6.1): The Petersen graph, the smallest snark.

# Relationships
## Related
- **Four-flow conjecture** — Says every snark contains the Petersen graph as a minor
- **Five-flow conjecture** — Reduces to snarks

# Source Reference
Chapter 6: Flows, Section 6.6, page 157 (pdf page 167). See Fig. 6.6.1.

# Verification Notes
- Confidence: HIGH — explicitly defined with examples
