---
concept: Minimum Degree Subgraph
slug: minimum-degree-subgraph

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 16
section: "1.2 The degree of a vertex"

extraction_confidence: high

aliases:
  - "Proposition 1.2.2"

prerequisites:
  - graph
  - degree
  - minimum-degree
  - edge-density
  - induced-subgraph
extends: []
related:
  - average-degree
contrasts_with: []

answers_questions:
  - "Does every graph have a subgraph with large minimum degree?"
---

# Quick Definition
Every graph G with at least one edge has a subgraph H with delta(H) > epsilon(H) >= epsilon(G). That is, every graph has a subgraph whose minimum degree exceeds half its average degree.

# Core Definition
Proposition 1.2.2: Every graph G with at least one edge has a subgraph H with delta(H) > epsilon(H) >= epsilon(G) (Diestel, p. 6).

# Prerequisites
- **Graph**, **degree**, **minimum-degree**, **edge-density**, **induced-subgraph**

# Key Properties
1. The subgraph H is obtained by iteratively deleting vertices of small degree
2. H is an induced subgraph of G
3. delta(H) > epsilon(H) >= epsilon(G)

# Construction / Recognition
1. Start with G_0 = G
2. If G_i has a vertex v_i with d(v_i) <= epsilon(G_i), set G_{i+1} = G_i - v_i
3. Otherwise, set H = G_i and stop
4. The resulting H satisfies delta(H) > epsilon(H) >= epsilon(G)

# Context & Application
This result shows that dense graphs always contain subgraphs where every vertex has high degree. It is a key ingredient in Mader's theorem (Theorem 1.4.3).

# Relationships
## Builds Upon
- **minimum-degree**, **edge-density**

## Enables
- Used in the proof of Theorem 1.4.3

# Source Reference
Chapter 1: The Basics, Section 1.2, Proposition 1.2.2, page 6 (pdf p. 16).

# Verification Notes
- Proposition and proof from p. 6
- Confidence: HIGH
