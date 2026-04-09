---
concept: Factor-Critical Graph
slug: factor-critical-graph
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 51
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "factor-critical"
  - "hypomatchable graph"
prerequisites:
  - one-factor
extends: []
related:
  - tuttes-theorem
  - gallai-edmonds-structure
  - odd-component
contrasts_with: []
answers_questions:
  - "What is a factor-critical graph?"
---

# Quick Definition
A graph G is factor-critical if G is non-empty and G-v has a 1-factor for every vertex v in G.

# Core Definition
A graph G = (V, E) is called **factor-critical** if G is non-empty and G-v has a 1-factor for every vertex v in G. Then G itself has no 1-factor, because it has odd order (Diestel, p. 51).

# Prerequisites
- **One-factor** — factor-criticality is defined via 1-factors of G-v

# Key Properties
1. G must have odd order (since G-v has even order to have a 1-factor)
2. G itself has no 1-factor (odd order)
3. Removing any single vertex yields a graph with a 1-factor
4. Factor-critical graphs are the components of G-S in Theorem 2.2.3
5. A single vertex (K1) is factor-critical

# Construction / Recognition
## To Verify Factor-Criticality
1. Check G has odd order
2. For each vertex v in G, verify G-v has a 1-factor
3. If all pass, G is factor-critical

# Context & Application
Factor-critical graphs arise naturally in the Gallai-Edmonds structure theorem (Theorem 2.2.3). Every graph G has a vertex set S such that S is matchable to the components of G-S, and every component of G-S is factor-critical. This provides a canonical structural decomposition for matching theory.

# Examples
**Example**: K1 (a single vertex) is trivially factor-critical. K3 (a triangle) is factor-critical: removing any vertex leaves K2, which has a 1-factor. More generally, every odd complete graph K_{2k+1} is factor-critical.

# Relationships
## Builds Upon
- **One-factor** — used in the definition

## Enables
- **Gallai-Edmonds structure theorem** (Theorem 2.2.3) — components of G-S are factor-critical
- **Tutte-Berge formula** — factor-critical components determine maximum matching size

## Related
- **Odd component** — factor-critical graphs have odd order

# Common Errors
- **Error**: Thinking factor-critical means the graph has a 1-factor
  **Correction**: A factor-critical graph has no 1-factor (odd order); removing any vertex creates one

# Common Confusions
- **Confusion**: Confusing factor-critical with "having many 1-factors"
  **Clarification**: Factor-criticality is about G-v having a 1-factor for every v, not about G itself

# Source Reference
Chapter 2, Section 2.2, p. 51 (pdf p. 51). Used in Theorem 2.2.3.

# Verification Notes
- Definition from p. 51
- Confidence: HIGH — explicitly defined
