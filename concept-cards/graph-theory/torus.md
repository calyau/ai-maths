---
concept: Torus
slug: torus
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
  - "genus 1 surface"
prerequisites:
  - surface
  - handle
  - sphere
extends:
  - sphere
related:
  - projective-plane
  - klein-bottle
  - euler-genus
contrasts_with: []
answers_questions:
  - "What is a torus?"
  - "What graphs can be embedded on a torus?"
---

# Quick Definition
The torus is the surface obtained from the sphere by adding one handle. It has Euler genus 2 (Euler characteristic 0) and can embed graphs that are not planar, such as K^5 and K_{3,3}.

# Core Definition
The torus is S^2 with one handle attached. By Lemma B.3, epsilon(torus) = 0 + 2 = 2, so chi(torus) = 0.

# Prerequisites
- **Surface**, **Handle**, **Sphere**

# Key Properties
1. Euler genus epsilon = 2
2. Euler characteristic chi = 0
3. Orientable
4. Contains non-separating circles (both one-sided impossible since orientable, but two-sided non-separating exist)
5. K^5 and K_{3,3} can be embedded on the torus
6. The complete graph K_7 can be embedded on the torus

# Context & Application
The torus is the first non-trivial surface beyond the sphere. It serves as a key example in the study of graph embeddings and the generalized Kuratowski theorem. The Heawood conjecture concerns the maximum chromatic number of graphs embeddable on the torus and other surfaces.

# Relationships
## Builds Upon
- **Sphere** plus one **Handle**

## Related
- **Projective plane** -- Non-orientable surface with epsilon = 1
- **Euler genus** -- Torus has epsilon = 2

# Source Reference
Appendix B, pages 362-363.

# Verification Notes
- Constructed from sphere + handle
- Confidence: HIGH -- standard example
