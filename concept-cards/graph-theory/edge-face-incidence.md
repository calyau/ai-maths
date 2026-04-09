---
concept: Edge-Face Incidence
slug: edge-face-incidence
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "Lemma 4.2.2"
prerequisites:
  - plane-graph
  - face
  - face-boundary
extends: []
related:
  - euler-formula
  - facial-cycle
contrasts_with: []
answers_questions:
  - "How many faces does an edge of a plane graph bound?"
---

# Quick Definition
In a plane graph: an edge on a cycle bounds exactly two faces; an edge on no cycle (a bridge) bounds exactly one face. The frontier of a face contains either all of an edge or none of its interior (Lemma 4.2.2).

# Core Definition
**Lemma 4.2.2**: "(i) If X is the frontier of a face of G, then either e is a subset of X or X intersection interior(e) = empty. (ii) If e lies on a cycle, then e lies on the frontier of exactly two faces, and these are contained in distinct faces of C. (iii) If e lies on no cycle, then e lies on the frontier of exactly one face" (Diestel, p. 87).

# Prerequisites
- **Plane graph**, **Face**, **Face boundary**

# Key Properties
1. Edges on cycles: incident with exactly 2 faces
2. Bridges: incident with exactly 1 face
3. Face boundaries are "clean" -- an edge is either entirely in or entirely out

# Context & Application
This lemma is the technical workhorse of Section 4.2. It is used in the proof of Euler's formula, the definition of facial cycles, and the proof that cycle space has a simple basis (MacLane's theorem). The "simple" property of facial cycles (each edge on at most two) follows directly.

# Relationships
## Enables
- **Euler's formula** -- Proof uses this lemma
- **Simple basis** -- Each edge in at most two facial cycles
- **MacLane's theorem**

# Source Reference
Chapter 4, Section 4.2, Lemma 4.2.2, pages 87-88.

# Verification Notes
- Lemma from p. 87
- Confidence: HIGH
