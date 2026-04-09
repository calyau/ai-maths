---
concept: Subdivision
slug: subdivision

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 29
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases:
  - "TX"
  - "subdividing vertex"
  - "branch vertex"

prerequisites:
  - graph
  - path
extends: []
related:
  - topological-minor
  - contraction
contrasts_with: []

answers_questions:
  - "What is a subdivision of a graph?"
  - "What are branch vertices and subdividing vertices?"
---

# Quick Definition
A subdivision of X is obtained by replacing each edge of X with an independent path between its ends. The original vertices of X are branch vertices; the new vertices are subdividing vertices.

# Core Definition
If we replace the edges of X with independent paths between their ends (so that none of these paths has an inner vertex on another path or in X), we call the graph G obtained a subdivision of X and write G = TX. If G = TX, we view V(X) as a subset of V(G) and call these vertices the branch vertices of G; the other vertices of G are its subdividing vertices. All subdividing vertices have degree 2, while the branch vertices retain their degree from X (Diestel, p. 20).

# Prerequisites
- **Graph** — a subdivision is a graph
- **Path** — edges are replaced by paths

# Key Properties
1. Subdividing vertices have degree 2
2. Branch vertices retain their degree from X
3. The number of branch vertices equals |V(X)|
4. TX denotes the class of all subdivisions of X

# Construction / Recognition
## To Construct a Subdivision of X
1. For each edge xy of X, choose a path P_xy with ends x and y
2. Ensure paths share no inner vertices with each other or with V(X)
3. The union of all these paths is a subdivision of X

# Relationships
## Builds Upon
- **graph**, **path**

## Enables
- **topological-minor** — defined using subdivisions

# Source Reference
Chapter 1: The Basics, Section 1.7, page 20 (pdf p. 30).

# Verification Notes
- Direct from p. 20
- Confidence: HIGH
