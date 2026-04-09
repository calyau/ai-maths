---
concept: Plane Dual of a Tree
slug: plane-dual-of-tree
category: planar-graphs
subcategory: plane-duality
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
  - "Exercise 25"
prerequisites:
  - plane-dual
  - plane-forest
extends: []
related:
  - plane-multigraph
contrasts_with: []
answers_questions:
  - "What does the dual of a plane tree look like?"
---

# Quick Definition
The plane dual of a plane tree T has one vertex (since T has one face) with n-1 loops (one for each edge of T). This illustrates why plane duals require multigraphs.

# Core Definition
"What does the plane dual of a plane tree look like?" (Diestel, p. 108, Exercise 25). Since a plane tree has one face (Proposition 4.2.4), its dual has one vertex. Each edge of T becomes a loop in the dual.

# Prerequisites
- **Plane dual**, **Plane forest**

# Key Properties
1. One vertex (one face in the tree)
2. n-1 loops (one per edge)
3. Illustrates the necessity of multigraphs in duality theory
4. The dual of the dual recovers the original tree

# Relationships
## Related
- **Plane multigraph** -- Dual of a tree requires loops

# Source Reference
Chapter 4, Exercise 25, page 108.

# Verification Notes
- Exercise 25
- Confidence: MEDIUM
