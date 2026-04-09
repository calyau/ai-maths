---
concept: Average Degree of Planar Graphs
slug: planar-average-degree
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - edge-bound-planar
extends:
  - edge-bound-planar
related:
  - five-colour-theorem
  - greedy-colouring
contrasts_with: []
answers_questions:
  - "What is the average degree of a planar graph?"
  - "Why does every planar graph have a vertex of degree at most 5?"
---

# Quick Definition
Every planar graph with n >= 3 has average degree d(G) = 2m/n < 6 (since m <= 3n-6). Therefore, every planar graph has a vertex of degree at most 5.

# Core Definition
From Corollary 4.2.10: d(G) = 2m/n <= 2(3n-6)/n < 6 for n >= 3 (Diestel, p. 112, proof of Proposition 5.1.2).

# Prerequisites
- **Edge bound for planar graphs**

# Key Properties
1. d(G) < 6 for all planar graphs with n >= 3
2. Therefore delta(G) <= 5
3. This is the key fact enabling the five colour theorem proof
4. More generally, for girth g: d(G) < 2g/(g-2)

# Context & Application
The bound d(G) < 6 is the entry point for all inductive colouring arguments on planar graphs. It guarantees a low-degree vertex that can be removed, the graph coloured by induction, and the vertex recoloured.

# Relationships
## Builds Upon
- **Edge bound** m <= 3n-6

## Enables
- **Five colour theorem** -- Uses d(G) < 6 to find degree-5 vertex
- **Thomassen's theorem** -- Same structural property

# Source Reference
Chapter 4, Corollary 4.2.10 (p. 91). Chapter 5, Proposition 5.1.2 proof (p. 112).

# Verification Notes
- From p. 112
- Confidence: HIGH
