---
concept: "Tutte's Hamiltonicity Theorem"
slug: tuttes-hamiltonicity-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 288
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases:
  - "Tutte 1956"
  - "4-connected planar Hamiltonian theorem"
prerequisites:
  - hamiltonian-graph
  - four-connected-graph
  - planar-graph
extends: []
related:
  - diracs-theorem
contrasts_with: []
answers_questions:
  - "Are 4-connected planar graphs Hamiltonian?"
---

# Quick Definition
Every 4-connected planar graph has a Hamilton cycle.

# Core Definition
**Theorem 10.1.3 (Tutte 1956).** Every 4-connected planar graph has a Hamilton cycle (Diestel, p. 288).

# Prerequisites
- **Hamiltonian graph** — the conclusion
- **4-connected graph** — kappa(G) >= 4
- **Planar graph** — embeddable in the plane

# Key Properties
1. 3-connectedness is not sufficient for cubic planar graphs (Tutte's 1946 counterexample)
2. The theorem is best possible in terms of connectivity for planar graphs
3. Related to the four colour theorem: if every 3-connected planar cubic graph were Hamiltonian, the four colour theorem would follow
4. Conjectured to extend to infinite graphs with Hamilton circles (Bruhn 2003)

# Context & Application
This theorem shows that planarity combined with high connectivity forces Hamiltonicity. It is related to attempts to prove the four colour theorem via Hamilton cycles in planar graphs.

# Examples
**Example**: Every 4-connected planar graph (e.g., the icosahedron) has a Hamilton cycle. The Tutte graph is a 3-connected cubic planar graph without a Hamilton cycle.

# Relationships
## Builds Upon
- **Hamiltonian graph**, **4-connected graph**, **planar graph**

## Related
- **Four colour theorem** — connected via the relationship between Hamilton cycles and flows

# Source Reference
Chapter 10, Section 10.1, Theorem 10.1.3, p. 288 (pdf p. 288).

# Verification Notes
- Statement from p. 288
- Stated without proof
- Confidence: HIGH — major named theorem
