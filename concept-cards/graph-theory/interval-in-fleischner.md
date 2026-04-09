---
concept: Interval (Fleischner's Proof)
slug: interval-in-fleischner
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 295
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "cycle interval"
prerequisites:
  - cycle
  - foot-of-path
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "What is an interval in the proof of Fleischner's theorem?"
---

# Quick Definition
An interval in Fleischner's proof is a maximal subpath of the cycle C between consecutive foot vertices (elements of X_2), with no internal vertices in X_2.

# Core Definition
A non-trivial path P = vi vi+1 ... v_{j-1} vj in C such that V(P) intersect X_2 = {vi, vj} is called an **interval**, with left end vi and right end vj. The cycle C is the union of 2|P_2| intervals (Diestel, p. 295).

# Prerequisites
- **Cycle** — intervals are subpaths of C
- **Foot of path** — X_2 consists of feet of paths with two feet

# Key Properties
1. Intervals partition C (minus X_2 vertices) into maximal segments
2. C = union of 2|P_2| intervals
3. Three types: traversed once (type 1), traversed twice as dead end (type 2), traversed twice separately (type 3)
4. I* is the special interval containing x*
5. Each type requires different modification in the proof

# Context & Application
Intervals structure the cycle C for the proof of Fleischner's theorem. The modification of the walk W to pass through each vertex exactly once is done interval by interval.

# Examples
**Example** (p. 296, Fig. 10.3.5): Modification of W on a type 2 interval using Lemma 10.3.2.

# Relationships
## Related
- **Fleischner's theorem** — intervals are central to the proof

# Source Reference
Chapter 10, Section 10.3, pp. 295-298 (pdf pp. 295-298).

# Verification Notes
- Definition from p. 295
- Confidence: HIGH — explicitly defined
