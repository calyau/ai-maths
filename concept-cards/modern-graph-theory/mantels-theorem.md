---
concept: "Mantel's Theorem"
slug: mantels-theorem
category: graph-fundamentals
subcategory: basic-results
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - triangle-free graph bound
prerequisites:
  - graph
  - graph-order-and-size
  - handshaking-lemma
  - cycle
extends: []
related:
  - bipartite-graph
  - complete-bipartite-graph
contrasts_with: []
answers_questions:
  - "What is the maximum number of edges in a triangle-free graph?"
---

# Quick Definition

Mantel's theorem (1907) states that every graph of order $n$ and more than $\lfloor n^2/4 \rfloor$ edges contains a triangle. The bound is sharp, achieved by $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$.

# Core Definition

"**Theorem 2.** Every graph of order $n$ and size greater than $\lfloor n^2/4 \rfloor$ contains a triangle" (Bollobás, p. 13). The proof uses the handshaking lemma and Cauchy's inequality. Mantel's theorem was greatly extended by Turán in 1941.

# Prerequisites

- **Graph** — The theorem applies to graphs
- **Graph order and size** — Bounds size in terms of order
- **Handshaking lemma** — Used in the proof
- **Cycle** — A triangle is $C_3$

# Key Properties

1. A triangle-free graph of order $n$ has at most $\lfloor n^2/4 \rfloor$ edges
2. The bound is best possible: $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ achieves it
3. The proof uses: if $G$ is triangle-free, then $\Gamma(x) \cap \Gamma(y) = \emptyset$ for each edge $xy$
4. This is the starting point of extremal graph theory

# Construction / Recognition

The proof shows: for triangle-free $G$, $d(x) + d(y) \le n$ for every edge $xy$. Summing and applying Cauchy's inequality yields $(2e)^2 \le n^2 e$, giving $e \le n^2/4$.

# Context & Application

Mantel's theorem is the oldest result in extremal graph theory (1907). It was the starting point for Turán's theorem (Chapter IV), which generalizes the bound to $K_r$-free graphs. It illustrates how simple degree-counting arguments can yield tight extremal results.

# Examples

**Example** (p. 13): The complete bipartite graph $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ is the unique triangle-free graph of order $n$ with maximum size $\lfloor n^2/4 \rfloor$.

# Relationships

## Builds Upon
- **Handshaking lemma**, **Graph order and size**, **Cycle**

## Enables
- Turán's theorem (Chapter IV) — generalization to $K_r$-free graphs

## Related
- **Bipartite graph** — Densest triangle-free graphs are bipartite
- **Complete bipartite graph** — The extremal graph

# Common Errors

- **Error**: Stating the bound as $n^2/4$ without the floor function
  **Correction**: The exact bound is $\lfloor n^2/4 \rfloor$

# Common Confusions

- **Confusion**: Thinking Mantel's theorem says triangle-free graphs must be bipartite
  **Clarification**: The extremal graph is bipartite, but not all triangle-free graphs are bipartite (e.g., a pentagon is triangle-free but not bipartite)... Actually, a pentagon is triangle-free but has an odd cycle. Triangle-free graphs can be bipartite or not, but the densest ones are bipartite.

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, Theorem 2, pages 13-14.

# Verification Notes

- Definition source: Direct theorem statement and proof from pp. 13-14
- Confidence rationale: Explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
