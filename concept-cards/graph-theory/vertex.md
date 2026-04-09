---
# === CORE IDENTIFICATION ===
concept: Vertex
slug: vertex

# === CLASSIFICATION ===
category: graph-fundamentals
tier: foundational

# === PROVENANCE ===
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "node"
  - "point"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
extends: []
related:
  - edge
  - adjacent
  - incident
  - degree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a vertex?"
  - "What are the elements of V(G)?"
---

# Quick Definition
A vertex is an element of the vertex set V of a graph G = (V, E). Vertices are the fundamental objects that edges connect.

# Core Definition
The elements of V are the vertices (or nodes, or points) of the graph G. The vertex set of a graph G is referred to as V(G). We may speak of a vertex v in G (rather than v in V(G)) (Diestel, p. 2).

# Prerequisites
- **Graph** — a vertex is defined as an element of a graph's vertex set

# Key Properties
1. Vertices are elements of the set V in the pair G = (V, E)
2. V and E are assumed disjoint
3. Vertices can be adjacent (connected by an edge) or non-adjacent
4. A vertex can be incident with zero or more edges

# Construction / Recognition
A vertex is any element of the vertex set V of a graph. In drawings, vertices are represented as dots.

# Context & Application
Vertices are one of the two fundamental building blocks of a graph. The number of vertices is the graph's order, denoted |G|.

# Examples
**Example** (p. 2): In the graph on V = {1, ..., 7} with edge set E = {{1,2}, {1,5}, {2,5}, {3,4}, {5,7}}, the vertices are 1, 2, 3, 4, 5, 6, 7.

# Relationships
## Builds Upon
- **graph** — vertices are elements of a graph

## Enables
- **edge** — edges connect pairs of vertices
- **degree** — the number of edges at a vertex
- **adjacent** — relation between vertices connected by an edge

# Common Errors
- **Error**: Assuming every vertex must have at least one edge
  **Correction**: Isolated vertices (degree 0) are permitted

# Common Confusions
- **Confusion**: Confusing a vertex with its label or its position in a drawing
  **Clarification**: A vertex is an abstract element; its label and position are representational choices

# Source Reference
Chapter 1: The Basics, Section 1.1 "Graphs," page 2 (pdf p. 12).

# Verification Notes
- Definition directly from p. 2
- Confidence: HIGH — explicitly defined
