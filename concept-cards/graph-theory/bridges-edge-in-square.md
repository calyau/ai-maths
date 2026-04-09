---
concept: Bridges (Edge in Square)
slug: bridges-edge-in-square
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 291
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "bridging edge"
prerequisites:
  - square-of-a-graph
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for an edge to bridge a vertex in G^2?"
---

# Quick Definition
An edge e in G^2 bridges a vertex v in G if the ends of e are both neighbors of v in G.

# Core Definition
An edge e in G^2 **bridges** a vertex v in G if its ends are neighbours of v in G (Diestel, p. 291).

# Prerequisites
- **Square of a graph** — bridging is defined for edges of G^2

# Key Properties
1. If e bridges v, then e is an edge of G^2 (since its ends have distance <= 2 via v)
2. e may or may not be an edge of G itself
3. Bridging edges are key to the proof of Fleischner's theorem (Lemma 10.3.2)
4. In Lemma 10.3.2, paths Q in P^2 are constructed so that vertices are bridged by edges of Q

# Context & Application
Bridging edges are a technical concept used in the proof of Fleischner's theorem. They ensure that the Hamilton cycle in G^2 can be constructed by "skipping" vertices on the original cycle C via their common neighbors.

# Examples
**Example** (Lemma 10.3.2): In a path P = v0...vk, the path Q in P^2 ensures that vertices v1, ..., v_{k-1} are each bridged by an edge of Q.

# Relationships
## Builds Upon
- **Square of a graph**

## Related
- **Fleischner's theorem** — bridging edges are used in the proof

# Source Reference
Chapter 10, Section 10.3, p. 291 (pdf p. 291).

# Verification Notes
- Definition from p. 291
- Confidence: HIGH — explicitly defined
