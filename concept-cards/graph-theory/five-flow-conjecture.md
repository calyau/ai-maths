---
concept: Five-Flow Conjecture
slug: five-flow-conjecture
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
  - "5-flow conjecture"
  - "Tutte's 5-flow conjecture"
prerequisites:
  - k-flow
  - flow-number
related:
  - four-flow-conjecture
  - three-flow-conjecture
  - six-flow-theorem
  - flow-colouring-duality
  - snark
answers_questions:
  - "What are Tutte's flow conjectures?"
---

# Quick Definition
Tutte's 5-flow conjecture (1954) states that every bridgeless multigraph has a 5-flow.

# Core Definition
**Five-Flow Conjecture** (Tutte 1954): Every bridgeless multigraph has a 5-flow.

This is the oldest and best known of Tutte's three flow conjectures. For planar graphs, it follows from the five colour theorem via the flow-colouring duality. The conjecture can be reduced to snarks. (Diestel, p. 156-157)

# Prerequisites
- **k-flow** — The conjecture asserts existence of a 5-flow
- **Flow number** — Equivalent to phi(G) <= 5 for all bridgeless G

# Key Properties
1. Open as of the writing (2005)
2. True for planar graphs (via duality and the five colour theorem)
3. Reduces to snarks: it suffices to prove it for cubic bridgeless graphs without 3-edge-colourings
4. Seymour's 6-flow theorem (phi(G) <= 6) is the best known general bound

# Relationships
## Related
- **Six-flow theorem** — The best approximation: every bridgeless graph has a 6-flow
- **Four-flow conjecture**, **Three-flow conjecture** — The other two Tutte conjectures
- **Flow-colouring duality** — Motivates the conjecture via planar duality
- **Snark** — The hard cases for the conjecture

# Source Reference
Chapter 6: Flows, Section 6.6, page 156 (pdf page 166).

# Verification Notes
- Confidence: HIGH — named conjecture, explicitly stated
