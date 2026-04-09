---
concept: Foot of a Path
slug: foot-of-path
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 293
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "foot"
prerequisites:
  - path
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "What is the foot of a path in Fleischner's proof?"
---

# Quick Definition
In the proof of Fleischner's theorem, the foot of a path P at an end y is a chosen neighbor of y on the cycle C in G.

# Core Definition
Every end y of a path P in the path set P has a neighbor on C in G; we choose such a neighbor and call it the **foot** of P at y (Diestel, p. 293).

# Prerequisites
- **Path** — feet are defined for paths in the decomposition

# Key Properties
1. Each end of a non-trivial path P has a foot on C
2. A trivial path (single vertex) has exactly one foot
3. A non-trivial path has feet at each of its two ends (which may coincide)
4. After consolidation (property (2)), no vertex of C is a foot of two distinct paths

# Context & Application
Feet are technical devices in the proof of Fleischner's theorem. They connect the paths in P to the cycle C, enabling the construction of the Hamilton cycle in G^2.

# Examples
**Example** (p. 293, Fig. 10.3.4): The set P(D) consists of paths whose ends have feet on C.

# Relationships
## Related
- **Fleischner's theorem** — feet are used in the proof

# Source Reference
Chapter 10, Section 10.3, p. 293 (pdf p. 293).

# Verification Notes
- Definition from p. 293
- Confidence: HIGH — explicitly defined
