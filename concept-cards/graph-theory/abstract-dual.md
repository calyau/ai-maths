---
concept: Abstract Dual
slug: abstract-dual
category: planar-graphs
subcategory: plane-duality
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.6 Plane duality"
extraction_confidence: high
aliases: []
prerequisites:
  - plane-dual
extends:
  - plane-dual
related:
  - whitney-planarity-theorem
  - cycle-space
contrasts_with:
  - plane-dual
answers_questions:
  - "What is an abstract dual of a graph?"
  - "How does abstract duality relate to planarity?"
---

# Quick Definition
A multigraph G* is an abstract dual of G if E(G*) = E(G) and the bonds (minimal edge cuts) in G* are precisely the edge sets of cycles in G.

# Core Definition
"Call a multigraph G* an abstract dual of a multigraph G if E(G*) = E(G) and the bonds in G* are precisely the edge sets of cycles in G" (Diestel, p. 105).

# Prerequisites
- **Plane dual** -- Abstract duality generalizes plane duality

# Key Properties
1. Same edge set as G, but different vertex structure
2. Bonds of G* = cycles of G
3. If G* is an abstract dual of G, then G is an abstract dual of G* (symmetry)
4. The cut space of G* equals the cycle space of G (Proposition 4.6.2)
5. A graph has an abstract dual iff it is planar (Whitney's theorem 4.6.3)

# Context & Application
Abstract duality removes the geometric requirement from plane duality, defining duality purely in terms of the cycle-bond correspondence. Whitney's theorem (4.6.3) shows this algebraic property characterizes planarity -- a remarkable connection between topology and algebra.

# Relationships
## Builds Upon
- **Plane dual** -- Generalization of geometric duality

## Enables
- **Whitney's planarity theorem** -- Planarity iff abstract dual exists

## Contrasts With
- **Plane dual** -- Plane dual requires an embedding; abstract dual does not

# Source Reference
Chapter 4, Section 4.6, page 105. Proposition 4.6.2, Theorem 4.6.3.

# Verification Notes
- Definition quoted from p. 105
- Confidence: HIGH -- explicit definition
