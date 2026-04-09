---
concept: Girth-Dependent Edge Bound for Planar Graphs
slug: girth-edge-bound
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "Exercises"
extraction_confidence: medium
aliases:
  - "Exercise 4"
prerequisites:
  - euler-formula
  - edge-bound-planar
  - triangle-free-edge-bound
extends:
  - edge-bound-planar
related: []
contrasts_with: []
answers_questions:
  - "How does girth affect the edge count of planar graphs?"
---

# Quick Definition
A connected planar graph with n vertices, m edges, and finite girth g satisfies m <= g/(g-2) * (n-2). For g=3: m <= 3(n-2); for g=4: m <= 2(n-2); as g grows, the bound approaches n-2 (a tree).

# Core Definition
"Show that every connected planar graph with n vertices, m edges and finite girth g satisfies m <= g/(g-2) * (n-2)" (Diestel, p. 107, Exercise 4).

# Prerequisites
- **Euler's formula**, **Edge bound for planar graphs**, **Triangle-free edge bound**

# Key Properties
1. Generalizes both m <= 3n-6 (g=3) and m <= 2n-4 (g=4)
2. Higher girth means sparser planar graphs
3. The proof uses 2m >= gl from Euler's formula

# Relationships
## Extends
- **Edge bound** (general and triangle-free cases)

# Source Reference
Chapter 4, Exercise 4, page 107.

# Verification Notes
- Exercise 4
- Confidence: MEDIUM
