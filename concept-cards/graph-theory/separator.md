---
concept: Separator
slug: separator

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "separating set"
  - "vertex cut"

prerequisites:
  - graph
  - connected-graph
  - path
extends: []
related:
  - k-connected
  - cut-vertex
  - bridge
  - separation
contrasts_with: []

answers_questions:
  - "What is a separator in a graph?"
  - "What does it mean for a set to separate two sets of vertices?"
---

# Quick Definition
A set X of vertices and/or edges separates sets A and B in G if every A-B path contains a vertex or edge from X. A separating set of vertices is called a separator.

# Core Definition
If A, B are subsets of V and X is a subset of V union E such that every A-B path in G contains a vertex or an edge from X, we say that X separates the sets A and B in G. Note that this implies A intersection B is a subset of X. More generally, X separates G if G - X is disconnected. A separating set of vertices is a separator (Diestel, p. 11).

# Prerequisites
- **Graph**, **connected-graph**, **path** — separation is defined via paths

# Key Properties
1. A intersection B must be a subset of X
2. A separator is a set of vertices whose removal disconnects the graph
3. A minimum separator has the smallest cardinality among all separators between two given sets

# Context & Application
Separators are central to connectivity theory. The minimum size of a separator determines the connectivity of a graph.

# Relationships
## Builds Upon
- **graph**, **path**, **connected-graph**

## Enables
- **k-connected** — defined via minimum separator size
- **cut-vertex** — a separator of size 1
- **bridge** — a separating edge

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21).

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
