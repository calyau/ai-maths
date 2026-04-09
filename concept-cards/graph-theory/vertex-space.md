---
concept: Vertex Space
slug: vertex-space

category: algebraic-graph-theory
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 33
section: "1.9 Some linear algebra"

extraction_confidence: high

aliases:
  - "V(G) vector space"

prerequisites:
  - graph
  - vertex
extends: []
related:
  - edge-space
  - cycle-space
  - cut-space
contrasts_with:
  - edge-space

answers_questions:
  - "What is the vertex space of a graph?"
---

# Quick Definition
The vertex space V(G) is the vector space over F_2 = {0, 1} of all functions V -> F_2. Its elements correspond to subsets of V, with addition being symmetric difference.

# Core Definition
The vertex space V(G) of G is the vector space over the 2-element field F_2 = {0, 1} of all functions V -> F_2. Every element corresponds naturally to a subset of V (the set of vertices assigned 1). We may think of V(G) as the power set of V made into a vector space: the sum U + U' of two vertex sets is their symmetric difference, and U = -U for all U. The zero is the empty set. dim V(G) = n (Diestel, p. 23).

# Prerequisites
- **Graph**, **vertex** — the vertex space is defined from the vertex set

# Key Properties
1. Elements are subsets of V (or equivalently, indicator functions V -> F_2)
2. Vector addition = symmetric difference
3. Standard basis: {{v_1}, ..., {v_n}}
4. Dimension = n (number of vertices)
5. Defined over F_2

# Relationships
## Builds Upon
- **graph**, **vertex**

## Related
- **edge-space** — the analogous construction for edges

# Source Reference
Chapter 1: The Basics, Section 1.9, page 23 (pdf p. 33).

# Verification Notes
- Direct from p. 23
- Confidence: HIGH
