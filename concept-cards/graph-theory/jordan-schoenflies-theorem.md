---
concept: Jordan-Schoenflies Theorem
slug: jordan-schoenflies-theorem
category: planar-graphs
subcategory: topological-prerequisites
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 96
section: "4.1 Topological prerequisites"
extraction_confidence: high
aliases:
  - "Theorem 4.1.4"
  - "Schoenflies theorem"
prerequisites:
  - polygon
  - jordan-curve-theorem
extends:
  - jordan-curve-theorem
related:
  - topological-isomorphism
  - equivalent-embeddings
contrasts_with: []
answers_questions:
  - "Can a homeomorphism between two circles on S^2 be extended to their regions?"
---

# Quick Definition
The Jordan-Schoenflies Theorem states that a homeomorphism between two circles on S^2 can be extended to a homeomorphism between corresponding regions, enabling the construction of topological isomorphisms between plane graphs.

# Core Definition
**Theorem 4.1.4**: "Let phi: C_1 -> C_2 be a homeomorphism between two circles on S^2, let O_1 be a region of C_1, and let O_2 be a region of C_2. Then phi can be extended to a homeomorphism C_1 U O_1 -> C_2 U O_2" (Diestel, p. 86).

# Prerequisites
- **Polygon** -- Circles on S^2 correspond to polygons in the plane
- **Jordan Curve Theorem** -- The existence of exactly two regions is prerequisite

# Key Properties
1. Extends homeomorphisms from boundaries to interiors
2. Works on the 2-sphere S^2 rather than R^2 (avoiding special status for unbounded faces)
3. Used in the proof that combinatorial isomorphisms are topological (Theorem 4.3.1)

# Context & Application
This theorem is the key tool for proving that combinatorial isomorphisms between 2-connected plane graphs are topological (Theorem 4.3.1). It allows face-by-face extension of a homeomorphism from the graph to the entire sphere, establishing that 3-connected planar graphs have essentially unique embeddings.

# Examples
**Example** (p. 95, proof of Theorem 4.3.1): Used to extend a homeomorphism between edges of two plane graphs to include their faces, constructing a full homeomorphism of S^2.

# Relationships
## Builds Upon
- **Jordan Curve Theorem** -- The JCT guarantees the regions exist

## Enables
- **Topological isomorphism** -- Construction relies on extending homeomorphisms face by face
- **Whitney's uniqueness theorem** -- 3-connected graphs have unique embeddings

## Related
- **Equivalent embeddings** -- Equivalence of embeddings is proved via this theorem

# Common Errors
- **Error**: Attempting to apply the theorem directly in R^2 rather than S^2
  **Correction**: The theorem is stated for circles on S^2; the detour via stereographic projection avoids issues with unbounded faces

# Common Confusions
- **Confusion**: Thinking the theorem is just the Jordan Curve Theorem restated
  **Clarification**: The JCT only asserts regions exist; Jordan-Schoenflies says homeomorphisms between boundaries extend to homeomorphisms between regions

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," Theorem 4.1.4, page 86.

# Verification Notes
- Theorem statement directly adapted from p. 86
- Confidence: HIGH -- explicitly stated theorem
