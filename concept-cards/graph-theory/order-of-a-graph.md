---
concept: Order of a Graph
slug: order-of-a-graph

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
  - "|G|"

prerequisites:
  - graph
  - vertex
extends: []
related:
  - size-of-a-graph
  - graph-invariant
contrasts_with:
  - size-of-a-graph

answers_questions:
  - "What is the order of a graph?"
  - "What does |G| mean?"
---

# Quick Definition
The order of a graph G is the number of its vertices, written as |G|.

# Core Definition
The number of vertices of a graph G is its order, written as |G|. Graphs are finite, infinite, countable, and so on according to their order (Diestel, p. 2).

# Prerequisites
- **Graph** — order is a property of a graph
- **Vertex** — order counts vertices

# Key Properties
1. Order is a non-negative integer (for finite graphs)
2. Written as |G|
3. A graph of order 0 or 1 is called trivial
4. Order is a graph invariant

# Construction / Recognition
To determine the order of a graph, count its vertices: |G| = |V(G)|.

# Context & Application
Order is one of the most basic graph invariants. It classifies graphs as finite, infinite, countable, etc.

# Examples
**Example** (p. 2): The graph on V = {1, ..., 7} has order 7.

# Relationships
## Builds Upon
- **graph**, **vertex**

## Enables
- Classification of graphs by size

## Contrasts With
- **size-of-a-graph** — size counts edges, not vertices

# Common Confusions
- **Confusion**: Confusing order (number of vertices) with size (number of edges)
  **Clarification**: |G| is the order (vertices); ||G|| is the size (edges)

# Source Reference
Chapter 1: The Basics, Section 1.1, page 2 (pdf p. 12).

# Verification Notes
- Direct from p. 2
- Confidence: HIGH
