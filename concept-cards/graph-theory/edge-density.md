---
concept: Edge Density
slug: edge-density

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 15
section: "1.2 The degree of a vertex"

extraction_confidence: high

aliases:
  - "epsilon(G)"

prerequisites:
  - graph
  - edge
extends: []
related:
  - average-degree
contrasts_with: []

answers_questions:
  - "What is the edge density of a graph?"
  - "What does epsilon(G) mean?"
---

# Quick Definition
The edge density epsilon(G) := |E|/|V| is the ratio of edges to vertices.

# Core Definition
Sometimes it will be convenient to express the ratio of edges to vertices directly, as epsilon(G) := |E|/|V|. We have epsilon(G) = (1/2) * d(G) (Diestel, p. 5).

# Prerequisites
- **Graph** — edge density is a graph property
- **Edge** — it counts edges relative to vertices

# Key Properties
1. epsilon(G) = |E|/|V|
2. epsilon(G) = d(G)/2
3. epsilon(G) >= delta(G)/2

# Context & Application
Edge density provides a normalized measure of how many edges a graph has relative to its order.

# Relationships
## Builds Upon
- **graph**, **edge**

## Related
- **average-degree** — d(G) = 2 * epsilon(G)

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
