---
concept: Ramsey Graph
slug: ramsey-graph
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 268
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "Ramsey graph for H"
prerequisites:
  - graph-ramsey-number
  - monochromatic-subgraph
related:
  - induced-ramsey-theorem
answers_questions:
  - "What is a Ramsey graph?"
---

# Quick Definition
A Ramsey graph for H is a graph G such that every 2-colouring of E(G) yields a monochromatic INDUCED copy of H.

# Core Definition
A graph G is a **Ramsey graph** for H if every 2-colouring of E(G) yields a monochromatic induced subgraph isomorphic to H, i.e., G contains an induced copy of H with all edges in one colour class. (Diestel, p. 259)

This is a stronger requirement than just finding a (non-induced) monochromatic copy of H.

# Prerequisites
- **Graph Ramsey number** — The basic Ramsey problem (non-induced)
- **Monochromatic subgraph** — The property being guaranteed

# Key Properties
1. Requires an INDUCED monochromatic copy, not just a subgraph
2. A sufficiently large complete graph is a Ramsey graph for K^r (by classical Ramsey)
3. Finding Ramsey graphs for general H requires careful construction
4. The second proof of Theorem 9.3.1 constructs G with omega(G) = omega(H)

# Relationships
## Enables
- **Induced Ramsey theorem** — Every graph has a Ramsey graph (Theorem 9.3.1)

## Contrasts With
- Classical Ramsey (non-induced) — Complete graphs suffice for the non-induced version

# Source Reference
Chapter 9, Section 9.3, page 259 (pdf page 268).

# Verification Notes
- Confidence: HIGH — explicitly defined
