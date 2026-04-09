---
concept: NP-Completeness of Hamiltonicity
slug: npc-hamiltonicity
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 285
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases:
  - "NP-hardness of Hamilton cycle"
prerequisites:
  - hamiltonian-graph
extends: []
related:
  - diracs-theorem
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "Why is there no good characterization of Hamiltonian graphs?"
---

# Quick Definition
Deciding whether a graph is Hamiltonian is NP-complete, one of the early prototypes of NP-complete problems. No good characterization of Hamiltonicity is expected to exist.

# Core Definition
Deciding whether a given graph is hamiltonian is NP-hard (indeed, one of the early prototypes of an NP-complete decision problem), while the existence of a good characterization would place it in NP intersect co-NP, which is widely believed to equal P. Thus, unless P = NP, no good characterization of hamiltonicity exists (Diestel, p. 300, notes).

# Prerequisites
- **Hamiltonian graph** — the property whose complexity is at issue

# Key Properties
1. NP-complete: no known polynomial-time algorithm
2. No "good characterization" (polynomial-time certificate for both YES and NO) is expected
3. Contrasts sharply with Euler tours (polynomial-time characterization: all even degrees)
4. Motivates the search for sufficient conditions (Dirac, Ore, Chvatal)
5. The travelling salesman problem is the optimization version

# Context & Application
The NP-completeness of Hamiltonicity is the fundamental barrier that makes the subject difficult. Unlike Euler tours (simple characterization), Hamiltonicity has no clean necessary-and-sufficient condition. This motivates the entire study of sufficient conditions in Chapter 10.

# Examples
**Example**: The contrast between Euler tours (complete characterization by Theorem 1.8.1) and Hamilton cycles (no good characterization) is the opening theme of Chapter 10.

# Relationships
## Builds Upon
- **Hamiltonian graph**

## Related
- **Dirac's theorem**, **Chvatal's theorem** — sufficient conditions, not full characterizations

# Source Reference
Chapter 10, p. 285 (pdf p. 285) and notes p. 300.

# Verification Notes
- From notes section, p. 300
- Also mentioned p. 285
- Confidence: HIGH — explicitly discussed
