---
concept: "MacLane's Theorem"
slug: maclane-theorem
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
  - "Theorem 4.5.1"
  - "MacLane 1937"
  - "cycle space planarity criterion"
prerequisites:
  - simple-basis
  - kuratowski-theorem
extends: []
related:
  - facial-cycle
  - kelmans-planarity-criterion
  - whitney-planarity-theorem
contrasts_with: []
answers_questions:
  - "How can planarity be characterized algebraically?"
  - "What is the relationship between cycle space and planarity?"
---

# Quick Definition
MacLane's theorem states that a graph is planar if and only if its cycle space has a simple basis (one where every edge appears in at most two basis elements).

# Core Definition
**Theorem 4.5.1** (MacLane 1937): "A graph is planar if and only if its cycle space has a simple basis" (Diestel, p. 101).

# Prerequisites
- **Simple basis** -- The key concept in the characterization
- **Kuratowski's theorem** -- The backward direction of the proof uses Kuratowski's theorem

# Key Properties
1. Forward direction: facial cycles of a plane graph form a simple basis
2. Backward direction: if cycle space has simple basis, then no TK^5 or TK_{3,3}, hence planar
3. The non-planarity proof for K^5 uses dim C(K^5) = 6 and counting
4. The non-planarity proof for K_{3,3} uses dim C(K_{3,3}) = 4 and counting
5. Having a simple basis is hereditary: subgraphs inherit it

# Context & Application
MacLane's theorem provides an algebraic characterization of planarity, connecting the geometric property of embeddability to the algebraic structure of the cycle space. Combined with Tutte's theorem on cycle spaces of 3-connected graphs, it yields the Kelmans planarity criterion (Theorem 4.5.2).

# Relationships
## Builds Upon
- **Simple basis**, **Kuratowski's theorem**

## Enables
- **Kelmans planarity criterion** -- Combined with Tutte's theorem
- **Whitney's planarity theorem** -- Abstract duality relates to simple bases

# Source Reference
Chapter 4, Section 4.5, Theorem 4.5.1, pages 101-102.

# Verification Notes
- Theorem statement quoted from p. 101
- Full proof given pp. 101-102
- Confidence: HIGH -- named classical theorem with proof
