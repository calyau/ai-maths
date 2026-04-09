---
concept: Topological Separation
slug: topological-separation
category: planar-graphs
subcategory: topological-prerequisites
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.1 Topological prerequisites"
extraction_confidence: high
aliases:
  - "separates in the plane"
prerequisites:
  - region
  - frontier
extends: []
related:
  - jordan-curve-theorem
  - polygon
  - arc
contrasts_with:
  - separation
answers_questions:
  - "What does it mean for a set to separate a region in R^2?"
---

# Quick Definition
A closed set X in R^2 separates an open set O if O \ X has more than one region. Polygons separate R^2 into exactly two regions; arcs do not separate.

# Core Definition
"A closed set X in R^2 is said to separate O if O \ X has more than one region" (Diestel, p. 84).

# Prerequisites
- **Region** -- Separation is about creating multiple regions
- **Frontier** -- The frontier separates a region from the rest

# Key Properties
1. Polygons separate R^2 into exactly two regions (Jordan Curve Theorem)
2. Arcs do not separate the plane (Lemma 4.1.3)
3. Topological separation is distinct from graph-theoretic separation

# Relationships
## Related
- **Jordan Curve Theorem** -- Fundamental separation result

## Contrasts With
- **Separation** (graph-theoretic) -- Removal of vertices from a graph

# Source Reference
Chapter 4, Section 4.1, page 84.

# Verification Notes
- Definition from p. 84
- Confidence: HIGH
