---
concept: Size of a Graph
slug: size-of-a-graph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "||G||"

prerequisites:
  - graph
  - edge
extends: []
related:
  - order-of-a-graph
  - graph-invariant
contrasts_with:
  - order-of-a-graph

answers_questions:
  - "What is the size of a graph?"
  - "What does ||G|| mean?"
---

# Quick Definition
The size of a graph G is its number of edges, denoted ||G||.

# Core Definition
The number of edges of a graph G is denoted by ||G|| (Diestel, p. 2).

# Prerequisites
- **Graph** — size is a property of a graph
- **Edge** — size counts edges

# Key Properties
1. Size is a non-negative integer (for finite graphs)
2. Written as ||G||
3. Size is a graph invariant

# Construction / Recognition
To determine the size, count the edges: ||G|| = |E(G)|.

# Context & Application
Size is one of the most basic graph invariants. For a complete graph K^n, the size is n(n-1)/2.

# Examples
**Example** (p. 2): The graph on V = {1, ..., 7} with E = {{1,2}, {1,5}, {2,5}, {3,4}, {5,7}} has size 5.

# Relationships
## Builds Upon
- **graph**, **edge**

## Contrasts With
- **order-of-a-graph** — order counts vertices, size counts edges

# Common Confusions
- **Confusion**: Confusing size (edges) with order (vertices)
  **Clarification**: ||G|| counts edges; |G| counts vertices

# Source Reference
Chapter 1: The Basics, Section 1.1, page 2 (pdf p. 12).

# Verification Notes
- Direct from p. 2
- Confidence: HIGH
