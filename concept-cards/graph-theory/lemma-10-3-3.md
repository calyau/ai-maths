---
concept: Cubic Multigraph Walk Lemma
slug: lemma-10-3-3
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
  - "Lemma 10.3.3"
prerequisites:
  - euler-tour
  - hamilton-cycle
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "How are closed walks constructed in cubic multigraphs for Fleischner's theorem?"
---

# Quick Definition
Lemma 10.3.3 shows that a cubic multigraph with a Hamilton cycle C has a closed walk that traverses one edge of C once, all other C-edges once or twice, and all non-C edges once.

# Core Definition
**Lemma 10.3.3.** Let G be a cubic multigraph with a Hamilton cycle C. Let e in E(C) and f in E \ E(C) share an end v. Then there exists a closed walk in G that traverses e once, every other edge of C once or twice, and every edge in E \ E(C) once. This walk contains the triple (e, v, f) (Diestel, p. 292).

# Prerequisites
- **Euler tour** — the proof uses Euler tours in 4-regular multigraphs
- **Hamilton cycle** — the starting structure

# Key Properties
1. The walk traverses all non-C edges exactly once
2. C-edges are traversed once or twice (except e, which is traversed once)
3. Constructed by doubling alternate C-edges, splitting a vertex, and finding an Euler tour
4. Key technical lemma for Fleischner's theorem

# Construction / Recognition
## Proof Strategy
1. C has even length (Proposition 1.2.1)
2. Replace every other C-edge by a double edge (not e)
3. The result is 4-regular; split v into v', v''
4. By Theorem 1.8.1, the multigraph has an Euler tour
5. The Euler tour induces the desired walk in G

# Context & Application
This lemma provides the initial closed walk W in the proof of Fleischner's theorem. The walk is then modified to pass through each vertex exactly once.

# Examples
**Example** (p. 292, Fig. 10.3.2): The multigraphs G and G' showing the vertex splitting and doubling construction.

# Relationships
## Related
- **Fleischner's theorem** — uses this lemma

# Source Reference
Chapter 10, Section 10.3, Lemma 10.3.3, p. 292 (pdf p. 292).

# Verification Notes
- Lemma from p. 292
- Confidence: HIGH
