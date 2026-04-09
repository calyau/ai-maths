---
concept: Graph Invariant
slug: graph-invariant

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

aliases: []

prerequisites:
  - graph
  - graph-isomorphism
extends: []
related:
  - graph-property
  - order-of-a-graph
  - size-of-a-graph
contrasts_with:
  - graph-property

answers_questions:
  - "What is a graph invariant?"
---

# Quick Definition
A graph invariant is a map taking graphs as arguments that assigns equal values to isomorphic graphs.

# Core Definition
A map taking graphs as arguments is called a graph invariant if it assigns equal values to isomorphic graphs. The number of vertices and the number of edges of a graph are two simple graph invariants; the greatest number of pairwise adjacent vertices is another (Diestel, p. 3).

# Prerequisites
- **Graph** — invariants are functions on graphs
- **Graph isomorphism** — invariants must respect isomorphism

# Key Properties
1. An invariant assigns the same value to isomorphic graphs
2. Invariants capture structural information
3. Examples: order, size, maximum clique size, chromatic number

# Context & Application
Much of graph theory concerns how the value of one invariant influences that of another (Diestel, p. 1). Invariants are the primary tools for classifying and comparing graphs.

# Examples
**Example** (p. 3): The number of vertices, the number of edges, and the greatest number of pairwise adjacent vertices are all graph invariants.

# Relationships
## Builds Upon
- **graph**, **graph-isomorphism**

## Related
- **order-of-a-graph**, **size-of-a-graph** — simple examples of invariants

## Contrasts With
- **graph-property** — a property is a class of graphs; an invariant is a function on graphs

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
