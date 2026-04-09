---
concept: Stereographic Projection
slug: stereographic-projection
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
  - "pi"
prerequisites:
  - polygon
extends: []
related:
  - jordan-schoenflies-theorem
  - equivalent-embeddings
contrasts_with: []
answers_questions:
  - "How does stereographic projection relate to planarity?"
---

# Quick Definition
Stereographic projection pi: S^2 \ {north pole} -> R^2 is a homeomorphism between the punctured sphere and the plane. It allows working on S^2 to avoid special treatment of the outer face of plane graphs.

# Core Definition
"The 2-sphere minus its 'north pole' (0,0,1) is homeomorphic to the plane; let us choose a fixed such homeomorphism pi: S^2 \ {(0,0,1)} -> R^2 (for example, stereographic projection)" (Diestel, p. 85).

# Prerequisites
- **Polygon** -- Used with polygons and circles on S^2

# Key Properties
1. Bijection between R^2 and S^2 minus one point
2. Any face can be made the outer face by rotating S^2
3. Eliminates the special status of the outer face
4. Used in the definitions of topological isomorphism and equivalence of embeddings

# Context & Application
The detour through S^2 and stereographic projection is Diestel's technical solution to the asymmetry between inner and outer faces. On S^2, all faces are topologically equivalent, simplifying many arguments (particularly the definition of topological isomorphism).

# Relationships
## Enables
- **Topological isomorphism** -- Defined via S^2
- **Equivalent embeddings** -- Use S^2 framework

# Source Reference
Chapter 4, Section 4.1, page 85-86.

# Verification Notes
- From pp. 85-86
- Confidence: HIGH
