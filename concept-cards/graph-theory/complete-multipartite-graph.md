---
concept: Complete Multipartite Graph
slug: complete-multipartite-graph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 26
section: "1.6 Bipartite graphs"

extraction_confidence: high

aliases:
  - "complete r-partite"
  - "K_{n_1,...,n_r}"
  - "K_s^r"
  - "star"

prerequisites:
  - r-partite-graph
extends:
  - r-partite-graph
related:
  - complete-graph
  - bipartite-graph
contrasts_with: []

answers_questions:
  - "What is a complete multipartite graph?"
  - "What is a star graph?"
---

# Quick Definition
A complete r-partite graph has every two vertices from different partition classes adjacent. Denoted K_{n_1,...,n_r} or K_s^r when all classes have size s. Stars are graphs of the form K_{1,n}.

# Core Definition
An r-partite graph in which every two vertices from different partition classes are adjacent is called complete. The complete r-partite graph is denoted by K_{n_1,...,n_r}; if n_1 = ... = n_r = s, we abbreviate to K_s^r. Graphs of the form K_{1,n} are called stars; the vertex in the singleton partition class is the star's centre (Diestel, p. 17).

# Prerequisites
- **r-partite-graph** — a complete multipartite graph is a special r-partite graph

# Key Properties
1. K_s^r has r * s vertices and s^2 * r(r-1)/2 edges
2. K_{1,n} is a star with center and n leaves
3. The octahedron is K_2^3

# Examples
**Example** (p. 17): The octahedron K_2^3 is shown in Fig. 1.6.1 and Fig. 1.4.3.
**Example** (p. 17): K_{3,3} = K_3^2 is shown with three different drawings in Fig. 1.6.2.

# Relationships
## Builds Upon
- **r-partite-graph**

## Related
- **complete-graph** — K^n = K_1^n

# Source Reference
Chapter 1: The Basics, Section 1.6, page 17 (pdf p. 27). See Figs. 1.6.1, 1.6.2.

# Verification Notes
- Direct from p. 17
- Confidence: HIGH
