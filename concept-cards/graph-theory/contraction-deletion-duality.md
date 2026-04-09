---
concept: Contraction-Deletion Duality
slug: contraction-deletion-duality
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
  - "Exercise 28"
prerequisites:
  - plane-dual
extends: []
related:
  - abstract-dual
contrasts_with: []
answers_questions:
  - "How do deletion and contraction relate in dual graphs?"
---

# Quick Definition
For dual plane multigraphs G and G* and edge e: deleting e in G corresponds to contracting e* in G*, and contracting e in G corresponds to deleting e* in G*.

# Core Definition
Exercise 28: "(i) If e is not a bridge, then G*/e* is a plane dual of G-e. (ii) If e is not a loop, then G*-e* is a plane dual of G/e" (Diestel, p. 108).

# Prerequisites
- **Plane dual**

# Key Properties
1. Deletion in G = contraction in G*
2. Contraction in G = deletion in G*
3. This duality between deletion and contraction is fundamental to matroid theory
4. The condition (not a bridge for deletion, not a loop for contraction) ensures the operations are well-defined

# Context & Application
This is the edge-level manifestation of cycle-bond duality. It connects planarity to matroid theory, where the same deletion-contraction duality characterizes graphic matroids.

# Relationships
## Builds Upon
- **Plane dual**

## Related
- **Abstract dual** -- Encodes the same relationship

# Source Reference
Chapter 4, Exercise 28, page 108.

# Verification Notes
- Exercise 28
- Confidence: MEDIUM
