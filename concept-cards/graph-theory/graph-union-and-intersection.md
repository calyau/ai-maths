---
concept: Graph Union and Intersection
slug: graph-union-and-intersection

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "union"
  - "intersection"
  - "disjoint graphs"

prerequisites:
  - graph
extends: []
related:
  - subgraph
contrasts_with: []

answers_questions:
  - "What is the union of two graphs?"
  - "What is the intersection of two graphs?"
  - "When are two graphs disjoint?"
---

# Quick Definition
The union of graphs G and G' is G union G' := (V union V', E union E'). Their intersection is G intersection G' := (V intersection V', E intersection E'). If G intersection G' is empty, G and G' are disjoint.

# Core Definition
We set G union G' := (V union V', E union E') and G intersection G' := (V intersection V', E intersection E'). If G intersection G' = the empty set, then G and G' are disjoint (Diestel, p. 4).

# Prerequisites
- **Graph** — union and intersection combine graphs

# Key Properties
1. Union: vertices and edges from both graphs
2. Intersection: only vertices and edges common to both
3. Disjoint: no vertices or edges in common
4. If G and G' are disjoint, G*G' denotes the join (connecting all vertices of G to all of G')

# Examples
**Example** (p. 4): Fig. 1.1.2 shows union, difference, and intersection of two graphs.

**Example** (p. 4): If G and G' are disjoint, G*G' joins all vertices of G to all vertices of G'. For instance, K^2 * K^3 = K^5.

# Relationships
## Builds Upon
- **graph**

## Related
- **subgraph** — containment of one graph in another

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14). See Fig. 1.1.2.

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
