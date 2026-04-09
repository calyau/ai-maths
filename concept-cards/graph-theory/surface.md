---
concept: Surface
slug: surface
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
  - "closed surface"
  - "2-manifold"
prerequisites:
  - graph
extends: []
related:
  - sphere
  - handle
  - crosscap
  - euler-characteristic
  - genus
contrasts_with: []
answers_questions:
  - "What is a surface in graph theory?"
  - "How are surfaces classified?"
---

# Quick Definition
A surface is a compact connected Hausdorff topological space in which every point has a neighbourhood homeomorphic to R^2. Surfaces are classified by the number of handles or crosscaps added to a sphere.

# Core Definition
"A surface, for the purpose of this book, is a compact connected Hausdorff topological space S in which every point has a neighbourhood homeomorphic to the Euclidean plane R^2" (Diestel, p. 361).

# Prerequisites
- **Graph** -- Graphs are embedded in surfaces

# Key Properties
1. Compact, connected, Hausdorff, locally Euclidean
2. Every surface can be obtained from S^2 by adding finitely many handles or crosscaps (classification theorem)
3. Different numbers of handles/crosscaps give distinct (non-homeomorphic) surfaces
4. Every surface other than the sphere contains a non-separating circle (Lemma B.1)
5. Arcs, circles, and discs in surfaces are defined via homeomorphisms to [0,1], S^1, and the unit disc

# Context & Application
Surfaces provide the topological setting for graph embeddings beyond the plane. The classification of surfaces (by handles and crosscaps) enables inductive proofs via surgery (cutting along non-separating circles). This machinery is essential for the graph minor theorem and the generalized Kuratowski theorem for arbitrary surfaces.

# Examples
**Example**: The sphere S^2 is the simplest surface (Euler genus 0).

**Example**: The torus is obtained from S^2 by adding one handle (Euler genus 2).

**Example**: The projective plane is obtained from S^2 by adding one crosscap (Euler genus 1).

# Relationships
## Enables
- **Euler characteristic** -- chi(S) is defined for surfaces
- **Graph embedding** -- Graphs can be embedded in surfaces
- **Graph minor theorem** -- Uses surface classification

## Related
- **Sphere**, **Handle**, **Crosscap**, **Genus**

# Source Reference
Appendix B: Surfaces, page 361.

# Verification Notes
- Definition directly quoted from p. 361
- Confidence: HIGH -- explicit definition
