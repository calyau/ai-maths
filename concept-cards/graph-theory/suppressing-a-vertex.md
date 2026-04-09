---
concept: Suppressing a Vertex
slug: suppressing-a-vertex

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 39
section: "1.10 Other notions of graphs"

extraction_confidence: high

aliases:
  - "vertex suppression"

prerequisites:
  - multigraph
  - degree
extends: []
related:
  - contraction
  - subdivision
contrasts_with: []

answers_questions:
  - "What does it mean to suppress a vertex?"
---

# Quick Definition
Suppressing a vertex v of degree 2 in a multigraph means deleting v and adding an edge between its two neighbours.

# Core Definition
If v is a vertex of degree 2 in a multigraph G, then by suppressing v we mean deleting v and adding an edge between its two neighbours. Suppressing several vertices always yields a well-defined multigraph independent of order (Diestel, p. 29).

# Prerequisites
- **Multigraph**, **degree** — suppression applies to degree-2 vertices

# Key Properties
1. Only applicable to vertices of degree 2
2. The result is independent of the order of suppression
3. It is the inverse of subdivision (adding a degree-2 vertex on an edge)

# Examples
**Example** (p. 29): Fig. 1.10.2 shows suppressing the white vertices.

# Relationships
## Builds Upon
- **multigraph**, **degree**

## Related
- **subdivision** — suppression undoes subdivision

# Source Reference
Chapter 1: The Basics, Section 1.10, page 29 (pdf p. 39). See Fig. 1.10.2.

# Verification Notes
- Direct from p. 29
- Confidence: HIGH
