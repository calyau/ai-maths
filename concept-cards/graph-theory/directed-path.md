---
concept: Directed Path
slug: directed-path
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 60
section: "2.5 Path covers"
extraction_confidence: high
aliases:
  - "directed path (Section 2.5)"
prerequisites:
  - directed-graph
  - path
extends:
  - path
related:
  - path-cover
  - gallai-milgram-theorem
contrasts_with: []
answers_questions:
  - "What is a directed path?"
---

# Quick Definition
A directed path is a directed graph with distinct vertices x0, ..., xk and edges e0, ..., e_{k-1} where each ei is directed from xi to x_{i+1}.

# Core Definition
A **directed path** is a directed graph P with distinct vertices x0, ..., xk and edges e0, ..., e_{k-1} such that ei is an edge directed from xi to x_{i+1}, for all i < k. The vertex xk is the **last vertex** of P (Diestel, p. 60).

# Prerequisites
- **Directed graph** — directed paths live in directed graphs
- **Path** — the undirected analogue

# Key Properties
1. All vertices are distinct
2. All edges are directed in a consistent direction
3. The last vertex xk is the terminal vertex
4. For a set P of paths, ter(P) denotes the set of last vertices

# Context & Application
Directed paths are the key objects in Section 2.5, where the Gallai-Milgram theorem gives bounds on path covers using independent sets.

# Examples
**Example** (p. 60): Directed paths in a directed graph form a path cover when they are vertex-disjoint and cover all vertices.

# Relationships
## Builds Upon
- **Directed graph**, **path**

## Enables
- **Path cover** — uses directed paths
- **Gallai-Milgram theorem** — about directed path covers

# Source Reference
Chapter 2, Section 2.5, p. 60 (pdf p. 60).

# Verification Notes
- Definition from p. 60
- Confidence: HIGH — explicitly defined
