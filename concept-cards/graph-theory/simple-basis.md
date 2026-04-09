---
concept: Simple Basis
slug: simple-basis
category: planar-graphs
subcategory: algebraic-planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.5 Algebraic planarity criteria"
extraction_confidence: high
aliases:
  - "simple family"
prerequisites:
  - cycle-space
extends: []
related:
  - maclane-theorem
  - facial-cycle
contrasts_with: []
answers_questions:
  - "What is a simple basis of the cycle space?"
  - "What does simplicity mean for a set of edge sets?"
---

# Quick Definition
A subset F of the edge space of a graph is simple if every edge lies in at most two sets of F. A simple basis of the cycle space is a basis that is also simple.

# Core Definition
"We call a subset F of its edge space E(G) simple if every edge of G lies in at most two sets of F" (Diestel, p. 101).

# Prerequisites
- **Cycle space** -- Simple bases are bases of the cycle space

# Key Properties
1. Every edge appears in at most two members of a simple family
2. The facial cycles of a 2-connected plane graph form a simple basis
3. The cut space always has a simple basis (the vertex cuts E(v))
4. K^5 and K_{3,3} do not have simple bases for their cycle spaces

# Context & Application
Simplicity of cycle space bases characterizes planarity (MacLane's theorem). The non-existence of simple bases for K^5 and K_{3,3} is proved by counting arguments: the minimum total size of cycle space basis elements exceeds twice the number of edges.

# Relationships
## Enables
- **MacLane's theorem** -- Planarity iff cycle space has simple basis

## Related
- **Facial cycle** -- Facial cycles form a simple basis for plane graphs

# Source Reference
Chapter 4, Section 4.5, page 101.

# Verification Notes
- Definition quoted from p. 101
- Confidence: HIGH -- explicit definition
