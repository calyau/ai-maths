---
concept: Four-Flow Conjecture
slug: four-flow-conjecture
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 166
section: "6.6 Tutte's flow conjectures"
extraction_confidence: high
aliases:
  - "4-flow conjecture"
  - "Tutte's 4-flow conjecture"
prerequisites:
  - k-flow
  - four-flow
  - flow-number
related:
  - five-flow-conjecture
  - three-flow-conjecture
  - snark
  - flow-colouring-duality
answers_questions:
  - "What is the 4-flow conjecture?"
---

# Quick Definition
Tutte's 4-flow conjecture (1966) states that every bridgeless multigraph not containing the Petersen graph as a minor has a 4-flow.

# Core Definition
**Four-Flow Conjecture** (Tutte 1966): Every bridgeless multigraph not containing the Petersen graph as a minor has a 4-flow.

For planar graphs, this follows from the four colour theorem (since the Petersen graph is non-planar). A proof for cubic graphs was announced in 1998 by Robertson, Sanders, Seymour and Thomas. (Diestel, pp. 156-157)

# Prerequisites
- **k-flow** — The conjecture concerns 4-flows
- **Four-flow** — Understanding what a 4-flow is
- **Flow number** — Asserts phi(G) <= 4 for the given class

# Key Properties
1. The Petersen graph is the obstruction: it is bridgeless but has no 4-flow
2. Not best possible: some graphs containing the Petersen minor do have 4-flows (e.g., K^11)
3. For cubic graphs, equivalent to saying every snark contains the Petersen graph as a minor
4. True for planar graphs via the four colour theorem and flow-colouring duality

# Relationships
## Related
- **Snark** — Snarks are the hard cases; the conjecture says every snark has a Petersen minor
- **Five-flow conjecture**, **Three-flow conjecture** — The other Tutte conjectures

# Source Reference
Chapter 6: Flows, Section 6.6, pages 156-157 (pdf pages 166-167).

# Verification Notes
- Confidence: HIGH — named conjecture, explicitly stated
