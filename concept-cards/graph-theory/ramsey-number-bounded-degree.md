---
concept: Ramsey Numbers of Bounded-Degree Graphs
slug: ramsey-number-bounded-degree
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 266
section: "9.2 Ramsey numbers"
extraction_confidence: high
aliases:
  - "Theorem 9.2.2"
  - "linear Ramsey numbers"
  - "Chvatal-Rodl-Szemeredi-Trotter theorem"
prerequisites:
  - graph-ramsey-number
  - regularity-lemma
  - turan-theorem
  - embedding-lemma
related:
  - ramsey-theorem-finite
answers_questions:
  - "How do Ramsey numbers relate to graph colouring?"
  - "How large is R(H) for sparse graphs H?"
---

# Quick Definition
For every positive integer Delta there is a constant c such that R(H) <= c|H| for all graphs H with maximum degree at most Delta.

# Core Definition
**Theorem 9.2.2** (Chvatal, Rodl, Szemeredi & Trotter 1983): For every positive integer Delta there is a constant c such that R(H) <= c|H| for all graphs H with Delta(H) <= Delta.

The proof uses the regularity lemma: given a 2-edge-colouring of G, obtain an epsilon-regular partition. If enough regular pairs have high density, find H in G via the embedding lemma. If not, most pairs have low density, so find H in G-bar. The key is that the regularity graph R contains K^m by Turan's theorem (since R is dense), and by Ramsey's theorem for K^m, it has a monochromatic K^{Delta+1}. (Diestel, pp. 256-258)

# Prerequisites
- **Graph Ramsey number** — The theorem bounds R(H) linearly
- **Regularity lemma** — The partition tool used in the proof
- **Turan's theorem** — Forces K^m in the regularity graph
- **Embedding lemma** — Converts regularity-graph subgraphs to actual subgraphs

# Key Properties
1. The Ramsey number of bounded-degree graphs grows LINEARLY in |H|
2. Enormous improvement over the exponential bound from Theorem 9.1.1
3. The constant c depends on Delta but not on the structure of H
4. Proof is a showcase application of the regularity lemma

# Context & Application
This theorem marks a breakthrough toward the Burr-Erdos conjecture (1975), which asserts linear Ramsey numbers for graphs with bounded average degree in every subgraph. It demonstrates the power of combining the regularity lemma with Ramsey theory.

# Relationships
## Builds Upon
- **Regularity lemma**, **Turan's theorem**, **Embedding lemma**

## Related
- **Ramsey theorem (finite)** — The theorem refines the exponential bound to linear

# Source Reference
Chapter 9, Section 9.2, Theorem 9.2.2, pages 256-258 (pdf pages 266-268).

# Verification Notes
- Confidence: HIGH — complete proof given
