---
concept: Arc Does Not Separate
slug: arc-does-not-separate
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
  - "Lemma 4.1.3"
prerequisites:
  - arc
  - region
extends: []
related:
  - jordan-curve-theorem
  - plane-forest
contrasts_with: []
answers_questions:
  - "Does an arc separate the plane?"
---

# Quick Definition
An arc does not separate the plane: if P is an arc between two disjoint point sets X_1, X_2, with interior in a region O of R^2 \ (X_1 U X_2), then O \ interior(P) remains a single region (Lemma 4.1.3).

# Core Definition
**Lemma 4.1.3**: "Let X_1, X_2 be disjoint sets, each the union of finitely many points and arcs, and let P be an arc between a point in X_1 and one in X_2 whose interior lies in a region O of R^2 \ (X_1 U X_2). Then O \ interior(P) is a region of R^2 \ (X_1 U P U X_2)" (Diestel, p. 85).

# Prerequisites
- **Arc**, **Region**

# Key Properties
1. Adding an arc does not split a region into two
2. Contrasts with polygons, which always split R^2 into two regions
3. Used in the proof that plane forests have one face

# Relationships
## Enables
- **Plane forest** has exactly one face

## Contrasts With
- **Jordan Curve Theorem** -- Closed curves DO separate

# Source Reference
Chapter 4, Section 4.1, Lemma 4.1.3, page 85.

# Verification Notes
- Lemma from p. 85
- Confidence: HIGH
