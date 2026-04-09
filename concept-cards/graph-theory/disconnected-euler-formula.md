---
concept: Euler Formula for Disconnected Graphs
slug: disconnected-euler-formula
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
  - "Exercise 3"
prerequisites:
  - euler-formula
extends:
  - euler-formula
related: []
contrasts_with: []
answers_questions:
  - "Does Euler's formula apply to disconnected plane graphs?"
---

# Quick Definition
For a disconnected plane graph with n vertices, m edges, l faces, and c connected components: n - m + l = 1 + c.

# Core Definition
"Find an Euler formula for disconnected graphs" (Diestel, p. 107, Exercise 3). The answer is n - m + l = 1 + c, where c is the number of components.

# Prerequisites
- **Euler's formula** (connected case)

# Key Properties
1. Reduces to n - m + l = 2 when c = 1
2. Each additional component adds a face (separating it from other components)
3. The "1 + c" replaces the "2" in the connected formula

# Relationships
## Extends
- **Euler's formula**

# Source Reference
Chapter 4, Exercise 3, page 107.

# Verification Notes
- Exercise 3
- Confidence: MEDIUM
