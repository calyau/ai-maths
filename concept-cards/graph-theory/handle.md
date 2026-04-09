---
concept: Handle
slug: handle
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases: []
prerequisites:
  - surface
  - sphere
extends: []
related:
  - crosscap
  - genus
  - torus
contrasts_with:
  - crosscap
answers_questions:
  - "What is a handle on a surface?"
  - "How does adding a handle change a surface?"
---

# Quick Definition
To add a handle to a surface S, remove two disjoint open discs and identify their boundary circles with the two ends of a cylinder S^1 x [0,1]. Adding a handle raises the Euler genus by 2.

# Core Definition
"To add a handle to a surface S, we remove two open discs whose closures in S are disjoint, and identify their boundary circles with the circles S^1 x {0} and S^1 x {1} of a copy of S^1 x [0,1] disjoint from S" (Diestel, p. 362).

# Prerequisites
- **Surface** and **Sphere** -- Handles are added to surfaces

# Key Properties
1. Adding a handle raises Euler genus by 2 (Lemma B.3(i))
2. The torus is S^2 plus one handle
3. The middle circle of the added cylinder is a two-sided non-separating circle
4. Produces an orientable surface from an orientable surface

# Context & Application
Handles are one of the two operations (along with crosscaps) in the classification of surfaces. Adding handles creates orientable surfaces (sphere, torus, genus-g surface). The Euler genus increase of 2 per handle is fundamental to induction arguments on surfaces.

# Relationships
## Related
- **Torus** -- Sphere plus one handle

## Contrasts With
- **Crosscap** -- Adds 1 to Euler genus instead of 2; creates non-orientable surfaces

# Source Reference
Appendix B, page 362. Lemma B.3.

# Verification Notes
- Definition from p. 362
- Confidence: HIGH -- explicit definition
