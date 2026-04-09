---
concept: Kelmans Planarity Criterion
slug: kelmans-planarity-criterion
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
  - "Theorem 4.5.2"
  - "Kelmans 1978"
  - "Tutte's planarity criterion"
prerequisites:
  - maclane-theorem
  - facial-cycle
extends:
  - maclane-theorem
related:
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "How can I test planarity of a 3-connected graph using non-separating cycles?"
---

# Quick Definition
A 3-connected graph is planar if and only if every edge lies on at most (equivalently, exactly) two non-separating induced cycles.

# Core Definition
**Theorem 4.5.2** (Kelmans 1978): "A 3-connected graph is planar if and only if every edge lies on at most (equivalently: exactly) two non-separating induced cycles" (Diestel, p. 102).

# Prerequisites
- **MacLane's theorem** -- The backward implication follows from MacLane + Tutte
- **Facial cycle** -- In plane graphs, facial cycles are non-separating induced cycles

# Key Properties
1. For 3-connected plane graphs, face boundaries = non-separating induced cycles
2. Each edge lies on exactly two face boundaries
3. Combines Tutte's theorem 3.2.3 and MacLane's theorem 4.5.1

# Context & Application
This criterion is notable for being "tangible" -- it can be checked by examining the local cycle structure of a graph. It emerges from the interplay between two abstract results (Tutte's and MacLane's) in a beautiful way.

# Relationships
## Builds Upon
- **MacLane's theorem**, **Tutte's theorem on cycle spaces** (3.2.3)

## Related
- **Kuratowski's theorem** -- Alternative planarity characterization

# Source Reference
Chapter 4, Section 4.5, Theorem 4.5.2, page 102.

# Verification Notes
- Theorem statement from p. 102
- Confidence: HIGH -- named theorem
