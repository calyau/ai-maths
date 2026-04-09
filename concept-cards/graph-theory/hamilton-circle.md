---
concept: Hamilton Circle
slug: hamilton-circle
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 288
section: "10.1 Simple sufficient conditions"
extraction_confidence: medium
aliases:
  - "Hamiltonian circle"
prerequisites:
  - hamilton-cycle
extends:
  - hamilton-cycle
related:
  - fleischners-theorem
contrasts_with:
  - hamilton-cycle
answers_questions:
  - "What is a Hamilton circle in an infinite graph?"
---

# Quick Definition
A Hamilton circle of an infinite graph G is a homeomorphic copy of the unit circle S^1 in the topological space |G| (formed by G and its ends) that contains every vertex of G.

# Core Definition
A circle in an infinite graph G is a homeomorphic copy of the unit circle S^1 in the topological space |G| formed by G and its ends. A **Hamilton circle** of G is a circle that contains every vertex of G (Diestel, p. 288).

# Prerequisites
- **Hamilton cycle** — the finite analogue

# Key Properties
1. Defined for infinite graphs using topological ends
2. Generalizes Hamilton cycles to infinite graphs
3. Conjectured that every locally finite 4-connected planar graph has a Hamilton circle (Bruhn 2003)
4. Conjectured that the square of every 2-connected locally finite graph has a Hamilton circle (p. 299)

# Context & Application
Hamilton circles extend the concept of Hamiltonicity to infinite graphs. While a ray cannot pass through a finite separator more than finitely often, circles in the topological space |G| can "pass through" ends, allowing a natural generalization.

# Examples
**Example**: The conjecture of Bruhn (2003) states that every locally finite 4-connected planar graph has a Hamilton circle, generalizing Tutte's theorem.

# Relationships
## Builds Upon
- **Hamilton cycle** — finite analogue

## Related
- **Fleischner's theorem** — conjectured to extend to Hamilton circles

## Contrasts With
- **Hamilton cycle** — the finite version

# Source Reference
Chapter 10, Section 10.1, p. 288 (pdf p. 288).

# Verification Notes
- Definition from p. 288
- Confidence: MEDIUM — concept defined briefly, conjectures stated
