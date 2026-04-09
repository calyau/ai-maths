---
concept: "Lovasz's Characterization of Perfection"
slug: lovasz-perfect-characterization
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "Theorem 5.5.6"
  - "Lovasz 1972"
prerequisites:
  - perfect-graph
  - clique-number
  - independence-number
extends: []
related:
  - perfect-graph-theorem
  - strong-perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "How can perfection be characterized numerically?"
---

# Quick Definition
A graph G is perfect if and only if |H| <= alpha(H) * omega(H) for every induced subgraph H of G.

# Core Definition
**Theorem 5.5.6** (Lovasz 1972): "A graph G is perfect if and only if |H| <= alpha(H) * omega(H) for all induced subgraphs H of G" (Diestel, p. 132).

# Prerequisites
- **Perfect graph**, **Clique number**, **Independence number**

# Key Properties
1. Since the condition is symmetric in G and complement(G), this immediately implies the perfect graph theorem
2. Necessity: if G is perfect, H can be partitioned into omega(H) classes of size <= alpha(H)
3. Sufficiency: elegant linear algebra proof by Gasparian (1996)
4. The proof uses matrices and rank arguments

# Context & Application
This characterization provides a second proof of the perfect graph theorem. The sufficiency proof by Gasparian uses the clever idea of constructing matrices A (incidence of independent sets) and B (incidence of cliques) with AB = J, then showing rank constraints force |V| <= alpha * omega.

# Relationships
## Enables
- **Perfect graph theorem** -- Immediate corollary (condition is self-complementary)

# Source Reference
Chapter 5, Section 5.5, Theorem 5.5.6, pages 132-133.

# Verification Notes
- Full proof given pp. 132-133
- Confidence: HIGH -- named theorem with complete proof
