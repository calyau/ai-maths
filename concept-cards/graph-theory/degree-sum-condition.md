---
concept: Degree Sum Condition
slug: degree-sum-condition
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: medium
aliases:
  - "sufficient degree conditions for Hamiltonicity"
prerequisites:
  - hamiltonian-graph
  - degree-sequence
extends: []
related:
  - diracs-theorem
  - ores-theorem
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "What degree conditions are sufficient for Hamiltonicity?"
---

# Quick Definition
Various degree conditions force Hamiltonicity: delta >= n/2 (Dirac), d(x)+d(y) >= n for non-adjacent x,y (Ore), and the Chvatal condition on degree sequences.

# Core Definition
The historical development of degree conditions for Hamiltonicity is: Dirac (1952) proved delta(G) >= n/2 suffices; Ore (1960) weakened this to d(x)+d(y) >= n for all non-adjacent x,y; Chvatal (1972) gave a complete characterization of which degree sequences force Hamiltonicity. Each later result strictly generalizes the earlier ones (Diestel, p. 289).

# Prerequisites
- **Hamiltonian graph** — the property being forced
- **Degree sequence** — the conditions are on degrees

# Key Properties
1. Dirac: delta >= n/2 (strongest individual vertex condition)
2. Ore: d(x)+d(y) >= n for non-adjacent pairs (weaker individual, considers pairs)
3. Chvatal: complete characterization of Hamiltonian degree sequences
4. Each implies the previous: Chvatal => Ore => Dirac
5. All proofs share the common structure of using a longest path or edge-maximal non-Hamiltonian graph

# Context & Application
Degree sum conditions represent the classical approach to Hamiltonicity: if the graph has "enough edges" distributed appropriately, a Hamilton cycle must exist. Chvatal's theorem provides the definitive answer within this framework.

# Examples
**Example** (Exercise 8): Chvatal's theorem implies that if fewer than i vertices have degree <= i for every i < n/2, then G is Hamiltonian.

# Relationships
## Builds Upon
- **Hamiltonian graph**, **degree sequence**

## Related
- **Dirac's theorem**, **Ore's theorem**, **Chvatal's theorem** — the hierarchy of conditions

# Source Reference
Chapter 10, Sections 10.1-10.2.

# Verification Notes
- Synthesized from the development in Sections 10.1-10.2
- Confidence: MEDIUM — concept is a synthesis of several theorems
