---
concept: Spanning Subgraph
slug: spanning-subgraph

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
  - subgraph
extends:
  - subgraph
related:
  - induced-subgraph
  - spanning-tree
contrasts_with:
  - induced-subgraph

answers_questions:
  - "What is a spanning subgraph?"
---

# Quick Definition
A subgraph G' of G is spanning if it contains all the vertices of G, i.e., V(G') = V(G).

# Core Definition
G' is a subset of G is a spanning subgraph of G if V' spans all of G, i.e. if V' = V (Diestel, p. 4).

# Prerequisites
- **Graph** — a spanning subgraph is a graph
- **Subgraph** — a spanning subgraph is a special subgraph

# Key Properties
1. A spanning subgraph has V(G') = V(G) but may have fewer edges
2. Every graph is a spanning subgraph of itself
3. A spanning subgraph with no edges is an edgeless graph on V

# Context & Application
Spanning subgraphs preserve the vertex set while potentially reducing the edge set. Spanning trees are the most important example.

# Relationships
## Builds Upon
- **subgraph**

## Enables
- **spanning-tree** — a spanning subgraph that is also a tree

## Contrasts With
- **induced-subgraph** — determined by vertex set, includes all relevant edges

# Source Reference
Chapter 1: The Basics, Section 1.1, page 4 (pdf p. 14).

# Verification Notes
- Direct from p. 4
- Confidence: HIGH
