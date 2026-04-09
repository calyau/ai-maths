---
concept: Genus
slug: genus
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
  - "orientable genus"
  - "genus of a surface"
  - "genus of a graph"
prerequisites:
  - surface
  - handle
  - euler-genus
extends: []
related:
  - euler-genus
  - euler-characteristic
  - torus
contrasts_with:
  - euler-genus
answers_questions:
  - "What is the genus of a surface?"
  - "What is the genus of a graph?"
---

# Quick Definition
The genus g of an orientable surface is the number of handles added to the sphere. For orientable surfaces, the Euler genus epsilon = 2g. The genus of a graph is the minimum genus of a surface in which it can be embedded.

# Core Definition
For an orientable surface obtained from S^2 by adding g handles, g is the genus. The Euler genus is epsilon = 2g, so chi = 2 - 2g. The genus of a graph G is the minimum g such that G can be embedded in a surface of genus g.

# Prerequisites
- **Surface**, **Handle**, **Euler genus**

# Key Properties
1. Sphere has genus 0; torus has genus 1
2. For orientable surfaces: chi(S) = 2 - 2g
3. For orientable surfaces: epsilon(S) = 2g
4. Genus of K_n: g(K_n) = ceiling((n-3)(n-4)/12) for n >= 3 (Heawood conjecture)
5. Planar graphs have genus 0

# Context & Application
Genus provides a natural measure of topological complexity for both surfaces and graphs. It extends planarity: a graph of genus g can be embedded on a surface with g handles but not fewer. The genus of a graph determines which surfaces it can live on.

# Relationships
## Related
- **Euler genus** -- epsilon = 2g for orientable surfaces
- **Torus** -- Genus 1

## Contrasts With
- **Euler genus** -- Genus counts handles only; Euler genus also counts crosscaps

# Source Reference
Appendix B, pages 361-363.

# Verification Notes
- Synthesized from surface classification and Euler genus
- Confidence: HIGH -- standard concept
