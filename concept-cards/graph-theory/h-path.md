---
concept: H-Path
slug: h-path
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 67
section: "3.1 2-Connected graphs and subgraphs"
extraction_confidence: high
aliases:
  - "ear"
prerequisites:
  - path
  - subgraph
extends:
  - path
related:
  - ear-decomposition
  - maders-theorem
contrasts_with: []
answers_questions:
  - "What is an H-path?"
---

# Quick Definition
An H-path is a path P whose endpoints are in a subgraph H but whose internal vertices are all outside H.

# Core Definition
Given a subgraph H of G, an **H-path** is a non-trivial path in G that meets H exactly in its endpoints (Diestel, used in Proposition 3.1.3 and Section 3.4).

# Prerequisites
- **Path** — an H-path is a special kind of path
- **Subgraph** — H is a subgraph of G

# Key Properties
1. Both endpoints lie in H
2. All internal vertices lie outside H
3. An H-path has length >= 1
4. H-paths are the "ears" in ear decomposition
5. The number of independent H-paths in G is related to Mader's theorem (Section 3.4)

# Construction / Recognition
## To Identify an H-Path
1. Check the path has both endpoints in V(H)
2. Verify all internal vertices are in V(G) \ V(H)
3. Verify the path is non-trivial (length >= 1)

# Context & Application
H-paths are used in two main contexts: (1) ear decomposition of 2-connected graphs (Proposition 3.1.3), where they are the "ears" added at each step; (2) Mader's theorem (Section 3.4), which counts independent H-paths.

# Examples
**Example** (p. 67, Fig. 3.1.2): In the ear decomposition, each new path added has its endpoints in the existing graph H and its internal vertices outside H.

# Relationships
## Builds Upon
- **Path**, **subgraph**

## Enables
- **Ear decomposition** — H-paths are the building blocks
- **Mader's theorem** — counts independent H-paths

# Common Errors
- **Error**: Allowing internal vertices to lie in H
  **Correction**: An H-path meets H only at its endpoints

# Source Reference
Chapter 3, Sections 3.1 and 3.4.

# Verification Notes
- Used in Proposition 3.1.3 and Theorem 3.4.1
- Confidence: HIGH — clearly used concept
