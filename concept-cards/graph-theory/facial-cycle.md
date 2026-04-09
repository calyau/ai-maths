---
concept: Facial Cycle
slug: facial-cycle
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
  - "face boundary cycle"
prerequisites:
  - face-boundary
  - plane-graph
extends:
  - face-boundary
related:
  - maclane-theorem
  - cycle-space
contrasts_with: []
answers_questions:
  - "What is a facial cycle?"
  - "How do facial cycles relate to the cycle space?"
---

# Quick Definition
A facial cycle of a 2-connected plane graph is a cycle that bounds a face. The facial cycles generate the entire cycle space and form a simple basis.

# Core Definition
"One of the most conspicuous features of a plane graph G are its facial cycles, the cycles that bound a face" (Diestel, p. 101). In a 2-connected plane graph, every face boundary is a cycle (Proposition 4.2.6), and these facial cycles generate the cycle space of G.

# Prerequisites
- **Face boundary** -- Facial cycles are the face boundaries that happen to be cycles
- **Plane graph** -- Defined for plane graphs

# Key Properties
1. In a 2-connected plane graph, every face boundary is a facial cycle
2. The set of facial cycles generates the entire cycle space
3. Every edge lies on at most two facial cycles (simplicity)
4. The facial cycles form a simple basis of the cycle space
5. In a 3-connected plane graph, facial cycles = non-separating induced cycles

# Context & Application
Facial cycles connect the geometric structure of a plane graph to its algebraic structure (cycle space). MacLane's theorem (4.5.1) shows that having a simple basis for the cycle space characterizes planarity, making facial cycles central to the algebraic theory of planarity.

# Relationships
## Builds Upon
- **Face boundary** -- Facial cycles are face boundaries in 2-connected case

## Enables
- **MacLane's theorem** -- Planarity iff cycle space has simple basis
- **Plane duality** -- Facial cycles correspond to minimal cuts in the dual

# Source Reference
Chapter 4, Section 4.5, page 101.

# Verification Notes
- Terminology from p. 101
- Confidence: HIGH -- explicit definition in context of MacLane's theorem
