---
concept: Neighborhood
slug: neighborhood

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
  - "N(v)"
  - "N(U)"
  - "neighbours"

prerequisites:
  - graph
  - adjacent
extends: []
related:
  - degree
contrasts_with: []

answers_questions:
  - "What is the neighborhood of a vertex?"
  - "What does N(v) mean?"
---

# Quick Definition
The neighborhood N(v) of a vertex v in G is the set of all neighbours of v. For a set U of vertices, N(U) is the set of all vertices in V minus U that are adjacent to some vertex in U.

# Core Definition
The set of neighbours of a vertex v in G is denoted by N_G(v), or briefly by N(v). More generally for U a subset of V, the neighbours in V minus U of vertices in U are called neighbours of U; their set is denoted by N(U) (Diestel, p. 5).

# Prerequisites
- **Graph** — neighborhoods exist within a graph
- **Adjacent** — neighbors are adjacent vertices

# Key Properties
1. N(v) consists of all vertices adjacent to v
2. v is not in N(v) (in simple graphs)
3. N(U) consists of vertices outside U that are adjacent to at least one vertex in U
4. |N(v)| = d(v) (the degree of v)

# Context & Application
Neighborhoods are fundamental for analyzing local structure in graphs.

# Relationships
## Builds Upon
- **graph**, **adjacent**

## Enables
- **degree** — degree equals the size of the neighborhood

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
