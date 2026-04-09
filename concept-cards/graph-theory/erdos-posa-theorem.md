---
concept: "Erdos-Posa Theorem"
slug: erdos-posa-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 55
section: "2.3 Packing and covering"
extraction_confidence: high
aliases:
  - "Erdos & Posa 1965"
  - "cycle packing theorem"
prerequisites:
  - erdos-posa-property
  - cycle
extends:
  - erdos-posa-property
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "Do cycles have the Erdos-Posa property?"
---

# Quick Definition
Every graph contains either k disjoint cycles or a set of at most f(k) vertices (with f(k) roughly 4k log k) that meets all cycles.

# Core Definition
**Theorem 2.3.2 (Erdos & Posa 1965).** There is a function f: N -> R such that, given any k in N, every graph contains either k disjoint cycles or a set of at most f(k) vertices meeting all its cycles (Diestel, p. 55).

# Prerequisites
- **Erdos-Posa property** — the theorem proves cycles have this property
- **Cycle** — the subgraph class under consideration

# Key Properties
1. The function f(k) = s_k + k - 1 where s_k is approximately 4k log k for k >= 2
2. The proof uses Lemma 2.3.1: cubic multigraphs on >= s_k vertices contain k disjoint cycles
3. The bound is roughly O(k log k)
4. A directed analogue exists but is much harder to prove (notes, p. 53)
5. The result extends in Chapter 12 via graph minor theory

# Construction / Recognition
## Proof Strategy
1. Reduce to a maximal subgraph H where all vertices have degree 2 or 3
2. Handle 2-regular components and "extra" cycles separately
3. Apply Lemma 2.3.1 to the cubic part to find k disjoint cycles or bound the cubic vertices

# Context & Application
The Erdos-Posa theorem establishes that cycles form a "well-behaved" class with respect to the packing-covering duality. This theorem reappears as a corollary of graph minor theory in Chapter 12.

# Examples
**Example** (p. 55): The proof shows that for f(k) = s_k + k - 1, either k disjoint cycles exist, or a set X union U of at most f(k) vertices meets all cycles, where U is the set of degree-3 vertices in a maximal subgraph.

# Relationships
## Builds Upon
- **Erdos-Posa property** — instantiated for cycles

## Related
- **Konig's theorem** — analogous min-max result for edges

# Common Errors
- **Error**: Expecting f(k) = k (as in Konig's theorem)
  **Correction**: For cycles, f(k) grows as O(k log k), not linearly

# Common Confusions
- **Confusion**: Thinking the theorem gives a tight bound
  **Clarification**: The function f is not tight; better bounds may exist

# Source Reference
Chapter 2, Section 2.3, Theorem 2.3.2, p. 55 (pdf p. 55). Proved using Lemma 2.3.1.

# Verification Notes
- Theorem statement from p. 55
- Confidence: HIGH — major named theorem with proof
