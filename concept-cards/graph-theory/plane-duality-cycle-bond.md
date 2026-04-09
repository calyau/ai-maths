---
concept: Cycle-Bond Duality
slug: plane-duality-cycle-bond
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
aliases:
  - "Proposition 4.6.1"
  - "duality of cycles and cuts"
prerequisites:
  - plane-dual
  - cycle-space
extends: []
related:
  - abstract-dual
  - maclane-theorem
contrasts_with: []
answers_questions:
  - "How do cycles and cuts relate in dual graphs?"
---

# Quick Definition
In a connected plane multigraph G with dual G*, an edge set E forms a cycle in G if and only if the corresponding set E* = {e* | e in E} is a minimal cut (bond) in G*.

# Core Definition
**Proposition 4.6.1**: "For any connected plane multigraph G, an edge set E of E(G) is the edge set of a cycle in G if and only if E* := {e* | e in E} is a minimal cut in G*" (Diestel, p. 104).

# Prerequisites
- **Plane dual** -- Duality between G and G*
- **Cycle space** -- Cycles in G correspond to bonds in G*

# Key Properties
1. Cycle in G <-> minimal cut in G*
2. Bond in G <-> cycle in G*
3. This extends to: cycle space of G = cut space of G* (Proposition 4.6.2)
4. The correspondence uses the bijection e -> e*

# Context & Application
This proposition is the geometric manifestation of the algebraic duality between cycle space and cut space. It provides the bridge between plane duality and abstract duality, and is key to Whitney's planarity theorem.

# Relationships
## Builds Upon
- **Plane dual** -- Uses the edge bijection e -> e*

## Enables
- **Abstract dual** -- Motivated by this correspondence
- **Whitney's planarity theorem** -- Connects abstract duality to planarity

# Source Reference
Chapter 4, Section 4.6, Proposition 4.6.1, page 104.

# Verification Notes
- Statement quoted from p. 104
- Confidence: HIGH -- explicit named proposition
