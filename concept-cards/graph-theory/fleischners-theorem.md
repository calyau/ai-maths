---
concept: "Fleischner's Theorem"
slug: fleischners-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 291
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "Fleischner 1974"
prerequisites:
  - square-of-a-graph
  - two-connected-graph
  - hamiltonian-graph
extends: []
related:
  - diracs-theorem
  - toughness-conjecture
contrasts_with: []
answers_questions:
  - "Is the square of a 2-connected graph always Hamiltonian?"
---

# Quick Definition
If G is a 2-connected graph, then G^2 has a Hamilton cycle.

# Core Definition
**Theorem 10.3.1 (Fleischner 1974).** If G is a 2-connected graph, then G^2 has a Hamilton cycle (Diestel, p. 291).

# Prerequisites
- **Square of a graph** — G^2 is the graph where vertices at distance <= 2 are adjacent
- **2-connected graph** — the hypothesis
- **Hamiltonian graph** — the conclusion (G^2 is Hamiltonian)

# Key Properties
1. G^2 is always Hamiltonian when G is 2-connected
2. 2-connectedness is necessary: Exercise 11 asks for a connected G whose G^2 has no Hamilton cycle
3. The proof (by Riha) proceeds by induction on |G|
4. The proof constructs a Hamilton cycle H in G^2 such that both edges at a specified vertex x* lie in G (property (*))
5. One of the main results in the field of Hamilton cycles

# Construction / Recognition
## Proof Strategy (sketch)
1. Find a cycle C in G containing x* and a vertex y* whose all neighbors lie on C (Lemma 10.3.4)
2. Decompose G-C into components; for each component D, find paths in D^2 forming P(D)
3. Use Lemma 10.3.3 to construct a closed walk W traversing each interval and path
4. Modify W so each vertex of C appears exactly once (using Lemma 10.3.2)
5. Incorporate paths from P1 (single-foot paths) to complete the Hamilton cycle

# Context & Application
Fleischner's theorem is described as "one of the main results in the field of Hamilton cycles" (Diestel, p. 285). It shows that squaring a 2-connected graph always creates enough adjacencies for a Hamilton cycle. The proof presented (due to Riha) is longer than most proofs in the book but not difficult.

Conjectured extension: the square of every 2-connected locally finite graph contains a Hamilton circle (p. 299).

# Examples
**Example** (p. 291-292): The proof uses three lemmas. Lemma 10.3.2 handles path rearrangements in P^2. Lemma 10.3.3 constructs closed walks in cubic multigraphs. Lemma 10.3.4 finds suitable cycles with captured vertices.

# Relationships
## Builds Upon
- **Square of a graph**, **2-connected graph**, **Hamiltonian graph**

## Related
- **Toughness conjecture** — Fleischner's theorem would follow from the conjecture with t=2 (Exercise 9)
- **Seymour's conjecture** — generalizes Dirac via higher powers

# Common Errors
- **Error**: Applying the theorem to graphs that are only connected (not 2-connected)
  **Correction**: 2-connectedness is essential; there exist connected graphs whose square has no Hamilton cycle

# Common Confusions
- **Confusion**: Thinking the Hamilton cycle lies in G itself
  **Clarification**: The Hamilton cycle is in G^2, not G; it may use edges not present in G (distance-2 edges)

# Source Reference
Chapter 10, Section 10.3, Theorem 10.3.1, pp. 291-299 (pdf pp. 291-299).

# Verification Notes
- Theorem from p. 291
- Proof spanning pp. 291-299 (the longest proof in this chapter)
- Confidence: HIGH — major theorem with complete proof
