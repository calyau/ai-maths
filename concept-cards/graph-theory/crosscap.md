---
concept: Crosscap
slug: crosscap
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
  - handle
  - genus
  - projective-plane
  - klein-bottle
contrasts_with:
  - handle
answers_questions:
  - "What is a crosscap?"
  - "How does adding a crosscap change a surface?"
---

# Quick Definition
To add a crosscap to a surface, remove one open disc and identify opposite points on its boundary circle in pairs. Adding a crosscap raises the Euler genus by 1 and makes the surface non-orientable.

# Core Definition
"To add a crosscap, we remove one open disc, and then identify opposite points on its boundary circle in pairs" (Diestel, p. 362).

# Prerequisites
- **Surface** and **Sphere**

# Key Properties
1. Adding a crosscap raises Euler genus by 1 (Lemma B.3(ii))
2. The projective plane is S^2 plus one crosscap
3. The Klein bottle is S^2 plus two crosscaps
4. Creates one-sided circles from arcs that run half-way around the boundary
5. Produces a non-orientable surface

# Context & Application
Crosscaps are the second operation (with handles) in surface classification. They produce non-orientable surfaces. The Euler genus increase of 1 per crosscap (vs 2 for handles) means crosscaps are "half" of a handle in topological complexity.

# Relationships
## Related
- **Projective plane** -- Sphere plus one crosscap
- **Klein bottle** -- Sphere plus two crosscaps

## Contrasts With
- **Handle** -- Adds 2 to Euler genus; preserves orientability

# Source Reference
Appendix B, page 362. Lemma B.3.

# Verification Notes
- Definition from p. 362
- Confidence: HIGH -- explicit definition
