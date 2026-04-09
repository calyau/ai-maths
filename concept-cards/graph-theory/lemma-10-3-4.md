---
concept: Captured Vertex Lemma
slug: lemma-10-3-4
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 292
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "Lemma 10.3.4"
prerequisites:
  - two-connected-graph
  - cycle
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "How do you find a cycle capturing a vertex in a 2-connected graph?"
---

# Quick Definition
For every 2-connected graph G and vertex x, there is a cycle C containing x and a vertex y whose all neighbors in G lie on C.

# Core Definition
**Lemma 10.3.4.** For every 2-connected graph G and x in V(G), there is a cycle C in G that contains x as well as a vertex y != x with N_G(y) contained in V(C) (Diestel, p. 292).

# Prerequisites
- **2-connected graph** — the hypothesis
- **Cycle** — the structure being found

# Key Properties
1. The cycle C contains both x and a "captured" vertex y
2. All neighbors of y lie on C (y is captured by C)
3. Proof: if G has a Hamilton cycle, trivial. Otherwise, choose C' and component D of G-C' minimizing |D|
4. The vertex y is found in the smallest component D
5. Key starting point for the proof of Fleischner's theorem

# Construction / Recognition
## Proof Strategy
1. If G has a Hamilton cycle, done
2. Otherwise, let C' be a cycle containing x, D a component of G-C'
3. Choose C', D with |D| minimal
4. D has >= 2 neighbors on C' (2-connectedness)
5. Replace a segment of C' by a path through D to get C
6. A vertex y in D has all neighbors on C (otherwise a smaller component would exist)

# Context & Application
This lemma provides the initial cycle C in the proof of Fleischner's theorem. The captured vertex y* plays a special role in the decomposition.

# Examples
**Example** (p. 292, Fig. 10.3.3): The cycle C and component D, with the path through D replacing a segment of C'.

# Relationships
## Related
- **Fleischner's theorem** — uses this lemma as the starting point

# Source Reference
Chapter 10, Section 10.3, Lemma 10.3.4, p. 292 (pdf p. 292).

# Verification Notes
- Lemma from p. 292
- Confidence: HIGH
