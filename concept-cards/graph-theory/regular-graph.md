---
concept: Regular Graph
slug: regular-graph

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
  - "k-regular"
  - "cubic graph"

prerequisites:
  - graph
  - degree
extends: []
related:
  - complete-graph
contrasts_with: []

answers_questions:
  - "What is a regular graph?"
  - "What is a k-regular graph?"
  - "What is a cubic graph?"
---

# Quick Definition
A graph is k-regular if every vertex has degree k. A 3-regular graph is called cubic.

# Core Definition
If all the vertices of G have the same degree k, then G is k-regular, or simply regular. A 3-regular graph is called cubic (Diestel, p. 5).

# Prerequisites
- **Graph** — regularity is a property of a graph
- **Degree** — regularity means all degrees are equal

# Key Properties
1. In a k-regular graph, delta(G) = d(G) = Delta(G) = k
2. A k-regular graph on n vertices has nk/2 edges
3. K^n is (n-1)-regular
4. The Petersen graph is 3-regular (cubic)

# Examples
**Example**: K^n is (n-1)-regular. Cycle graphs C^n are 2-regular.

# Relationships
## Builds Upon
- **degree**

## Related
- **complete-graph** — K^n is the unique (n-1)-regular graph on n vertices

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
