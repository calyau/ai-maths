---
concept: Six-Flow Theorem
slug: six-flow-theorem
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
  - "6-flow theorem"
  - "Seymour's 6-flow theorem"
prerequisites:
  - k-flow
  - flow-number
  - circulation
  - two-flow
extends:
  - five-flow-conjecture
related:
  - four-flow-conjecture
  - three-flow-conjecture
answers_questions:
  - "Does every bridgeless graph have a finite flow number?"
  - "What is the best known upper bound on flow numbers?"
---

# Quick Definition
Every bridgeless graph has a 6-flow (Seymour 1981). This is the strongest known general result toward Tutte's 5-flow conjecture.

# Core Definition
**Theorem 6.6.1** (Seymour 1981): Every bridgeless graph has a 6-flow.

The proof constructs a sequence of connected even subgraphs H_0, ..., H_n spanning all vertices, connected by edge sets F_1, ..., F_n. A Z_3-circulation f_0 is constructed that is nowhere zero except on edges of the H_i. Composing with the map h-bar -> 2h-bar from Z_3 to Z_6 and adding 2-flows on each H_i yields a Z_6-flow, and hence a 6-flow by Theorem 6.3.3. (Diestel, pp. 157-160)

# Prerequisites
- **k-flow** — The theorem proves existence of a 6-flow
- **Flow number** — Implies phi(G) <= 6 for all bridgeless G
- **Circulation** — The proof constructs Z_3-circulations and Z_6-circulations
- **Two-flow** — 2-flows on even subgraphs are a key ingredient

# Key Properties
1. Every bridgeless graph has flow number at most 6
2. This is the main result of Chapter 6
3. Best general bound toward the 5-flow conjecture (which asserts phi(G) <= 5)
4. The proof uses 2-edge-connectivity and constructs the flow from Z_3 and Z_2 components

# Context & Application
The 6-flow theorem answers the fundamental existence question: a graph has a finite flow number if and only if it is bridgeless. It is the strongest unconditional result in the direction of Tutte's 5-flow conjecture.

# Relationships
## Builds Upon
- **k-flow**, **Circulation**, **Two-flow**

## Related
- **Five-flow conjecture** — The 6-flow theorem is the best approximation

# Source Reference
Chapter 6: Flows, Section 6.6, Theorem 6.6.1, pages 157-160 (pdf pages 167-170).

# Verification Notes
- Theorem statement: Directly from p. 157
- Proof: Long constructive proof summarized from pp. 157-160
- Confidence: HIGH — the main theorem of the chapter, fully proved
