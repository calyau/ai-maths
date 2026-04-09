---
concept: Three-Flow Conjecture
slug: three-flow-conjecture
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
  - "3-flow conjecture"
  - "Tutte's 3-flow conjecture"
prerequisites:
  - k-flow
  - three-flow
  - flow-number
related:
  - five-flow-conjecture
  - four-flow-conjecture
  - flow-colouring-duality
answers_questions:
  - "What is the 3-flow conjecture?"
---

# Quick Definition
Tutte's 3-flow conjecture (1972) states that every multigraph without a cut of exactly one or exactly three edges has a 3-flow.

# Core Definition
**Three-Flow Conjecture** (Tutte 1972): Every multigraph without a cut consisting of exactly one or exactly three edges has a 3-flow.

For planar graphs, this is equivalent to Grotzsch's theorem (every triangle-free planar graph is 3-colourable) via the flow-colouring duality. (Diestel, p. 157)

# Prerequisites
- **k-flow** — The conjecture concerns 3-flows
- **Three-flow** — Understanding what a 3-flow is

# Key Properties
1. The condition "no 1-edge or 3-edge cut" is necessary but not sufficient on its own
2. Not best possible: some graphs with 3-edge cuts do have 3-flows
3. For planar graphs, equivalent to Grotzsch's theorem via duality

# Relationships
## Related
- **Five-flow conjecture**, **Four-flow conjecture**
- **Flow-colouring duality** — Translates to Grotzsch's theorem for planar graphs

# Source Reference
Chapter 6: Flows, Section 6.6, page 157 (pdf page 167).

# Verification Notes
- Confidence: HIGH — named conjecture, explicitly stated
