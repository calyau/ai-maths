---
# === CORE IDENTIFICATION ===
concept: Edge
slug: edge

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
  - "line"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
  - vertex
extends: []
related:
  - incident
  - adjacent
  - endvertex
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an edge?"
  - "How are edges denoted?"
---

# Quick Definition
An edge is a 2-element subset of the vertex set V of a graph G = (V, E). An edge {x, y} is usually written as xy (or yx) and represents a connection between vertices x and y.

# Core Definition
The elements of E are the edges (or lines) of the graph G. An edge {x, y} is usually written as xy (or yx). The two vertices incident with an edge are its endvertices or ends, and an edge joins its ends. If x is in X and y is in Y, then xy is an X-Y edge (Diestel, p. 2-3).

# Prerequisites
- **Graph** — edges are elements of a graph's edge set
- **Vertex** — edges connect pairs of vertices

# Key Properties
1. Each edge is a 2-element subset of V
2. An edge connects exactly two distinct vertices (its ends)
3. Two edges are adjacent if they share a common end
4. The notation xy is shorthand for the set {x, y}
5. E(X, Y) denotes the set of all X-Y edges; E(v) denotes all edges at vertex v

# Construction / Recognition
An edge exists between vertices x and y if and only if {x, y} is an element of E.

# Context & Application
Edges encode the relationships or connections in a graph. The number of edges is denoted ||G||. The set of all X-Y edges is E(X, Y); the set of all edges at a vertex v is E(v).

# Examples
**Example** (p. 2): In the graph on V = {1, ..., 7}, the edges are {1,2}, {1,5}, {2,5}, {3,4}, {5,7}.

# Relationships
## Builds Upon
- **graph**, **vertex**

## Enables
- **degree** — counts edges at a vertex
- **path**, **cycle** — sequences of edges
- **adjacent** — vertices connected by an edge

# Common Errors
- **Error**: Treating xy and yx as different edges
  **Correction**: Since an edge is a set {x, y}, xy = yx

# Common Confusions
- **Confusion**: Believing edges must have labels or weights
  **Clarification**: In Diestel's basic definition, edges are simply 2-element subsets with no additional structure

# Source Reference
Chapter 1: The Basics, Section 1.1 "Graphs," pages 2-3 (pdf pp. 12-13).

# Verification Notes
- Definition directly from p. 2-3
- Notation E(X,Y) and E(v) from p. 3
- Confidence: HIGH — explicitly defined
