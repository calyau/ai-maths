---
concept: Odd Cycle
slug: odd-cycle

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 26
section: "1.6 Bipartite graphs"

extraction_confidence: high

aliases: []

prerequisites:
  - cycle
extends: []
related:
  - bipartite-graph
contrasts_with: []

answers_questions:
  - "What is an odd cycle?"
  - "Why are odd cycles important?"
---

# Quick Definition
An odd cycle is a cycle of odd length. A graph is bipartite if and only if it contains no odd cycle.

# Core Definition
Clearly, a bipartite graph cannot contain an odd cycle, a cycle of odd length. In fact, the bipartite graphs are characterized by this property: Proposition 1.6.1 states that a graph is bipartite if and only if it contains no odd cycle (Diestel, p. 17).

# Prerequisites
- **Cycle** — an odd cycle is a cycle with an odd number of edges

# Key Properties
1. The shortest odd cycle has length 3 (a triangle)
2. A graph is bipartite iff it has no odd cycle
3. A graph with no triangle may still have an odd 5-cycle, 7-cycle, etc.

# Relationships
## Builds Upon
- **cycle**

## Related
- **bipartite-graph** — characterized by absence of odd cycles

# Source Reference
Chapter 1: The Basics, Section 1.6, page 17 (pdf p. 27). Proposition 1.6.1.

# Verification Notes
- Direct from p. 17
- Confidence: HIGH
