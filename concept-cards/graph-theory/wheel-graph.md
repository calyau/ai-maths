---
concept: Wheel Graph
slug: wheel-graph
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 69
section: "3.2 The structure of 3-connected graphs"
extraction_confidence: high
aliases:
  - "wheel"
  - "C^n * K^1"
prerequisites:
  - graph
  - cycle
extends: []
related:
  - tuttes-wheel-theorem
  - three-connected-graph
contrasts_with: []
answers_questions:
  - "What is a wheel graph?"
---

# Quick Definition
A wheel is a graph of the form C^n * K^1: a cycle C^n with an additional vertex joined to all vertices of the cycle. K4 is the smallest wheel.

# Core Definition
Graphs of the form C^n * K^1 are called **wheels**; thus, K4 is the smallest wheel (Diestel, p. 69, footnote 2).

# Prerequisites
- **Graph**, **cycle**

# Key Properties
1. A wheel W_n = C^n * K^1 has n+1 vertices
2. The central vertex (hub) has degree n
3. The cycle vertices have degree 3
4. Wheels are 3-connected
5. K4 = W_3 is the smallest wheel and the starting graph for Tutte's wheel theorem

# Context & Application
Wheels give Tutte's wheel theorem its name. Every 3-connected graph can be built from K4 (the smallest wheel) by vertex splitting operations.

# Examples
**Example**: K4 is W_3. W_4 is a square with a center vertex connected to all four corners.

# Relationships
## Builds Upon
- **Cycle**, **graph**

## Related
- **Tutte's wheel theorem** — named after wheels; K4 is the starting graph
- **3-connected graph** — all wheels are 3-connected

# Source Reference
Chapter 3, Section 3.2, p. 69 footnote (pdf p. 69).

# Verification Notes
- Definition from footnote 2, p. 69
- Confidence: HIGH — explicitly defined
