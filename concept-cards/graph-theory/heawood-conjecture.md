---
concept: Heawood's Theorem
slug: heawood-conjecture
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "Notes"
extraction_confidence: medium
aliases:
  - "Heawood formula"
  - "map colour theorem"
prerequisites:
  - euler-characteristic
  - chromatic-number
  - surface
extends: []
related:
  - four-colour-theorem
  - genus
contrasts_with: []
answers_questions:
  - "How many colours suffice for graphs on higher surfaces?"
---

# Quick Definition
Heawood's formula gives the maximum chromatic number of graphs embeddable on a surface of Euler characteristic chi: at most floor((7 + sqrt(49 - 24*chi))/2). For surfaces other than the sphere, this bound is tight.

# Core Definition
For a surface S with Euler characteristic chi(S), the chromatic number of any graph embeddable on S is at most H(S) = floor((7 + sqrt(49 - 24*chi(S)))/2). For all surfaces except the sphere, this bound is achieved.

# Prerequisites
- **Euler characteristic**, **Chromatic number**, **Surface**

# Key Properties
1. For the torus (chi = 0): H = 7; K_7 embeds on the torus
2. For the projective plane (chi = 1): H = 6
3. Heawood proved the upper bound; the lower bound (existence of tight examples) was proved by Ringel and Youngs (1968)
4. The sphere is the exception: H(sphere) = 7 but the true answer is 4

# Context & Application
Heawood's theorem extends the four colour theorem to higher surfaces. It shows that surface topology constrains chromaticity, with the constraint becoming weaker (more colours needed) as the surface becomes more complex.

# Relationships
## Related
- **Four colour theorem** -- The sphere case (with better bound)
- **Genus** -- Higher genus allows more colours

# Source Reference
Chapter 4, Notes, page 109 (referenced in Exercise 6). Also relevant to Appendix B.

# Verification Notes
- Referenced indirectly in exercises and notes
- Confidence: MEDIUM -- not a main theorem in the text
