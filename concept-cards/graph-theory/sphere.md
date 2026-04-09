---
concept: Sphere
slug: sphere
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
aliases:
  - "S^2"
  - "2-sphere"
prerequisites:
  - surface
extends:
  - surface
related:
  - plane-graph
  - euler-formula
  - euler-characteristic
contrasts_with: []
answers_questions:
  - "What is the sphere in graph theory?"
  - "How does the sphere relate to the plane?"
---

# Quick Definition
The sphere S^2 = {x in R^3 : ||x|| = 1} is the simplest surface. It is the starting point for the classification theorem and has Euler genus 0 (Euler characteristic 2).

# Core Definition
"The sphere S^2 = {x in R^3 : ||x|| = 1}" (Diestel, p. 361). The classification theorem states that every surface is obtained from S^2 by adding handles or crosscaps.

# Prerequisites
- **Surface** -- The sphere is the fundamental surface

# Key Properties
1. Euler genus epsilon(S^2) = 0 (by Theorem 4.2.9)
2. Euler characteristic chi(S^2) = 2
3. Every surface other than S^2 contains a non-separating circle
4. Related to the plane via stereographic projection
5. Plane graph theory can be equivalently formulated on S^2

# Context & Application
The sphere is the base case for surface classification and for induction on Euler genus. The plane R^2 is homeomorphic to S^2 minus a point, so plane graphs can be equivalently studied as graphs on the sphere. This equivalence (via stereographic projection) is used throughout Chapter 4 to avoid special treatment of the outer face.

# Relationships
## Builds Upon
- **Surface** -- S^2 is the simplest surface

## Enables
- **Classification of surfaces** -- All surfaces built from S^2
- **Euler's formula** -- n - m + l = 2 on S^2

## Related
- **Plane graph** -- Plane graphs are essentially graphs on S^2

# Source Reference
Appendix B, page 361.

# Verification Notes
- Confidence: HIGH -- fundamental object
