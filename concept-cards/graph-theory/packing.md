---
concept: Packing
slug: packing
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 43
section: "2.3 Packing and covering"
extraction_confidence: high
aliases:
  - "graph packing"
  - "subgraph packing"
prerequisites:
  - graph
  - subgraph
extends: []
related:
  - covering
  - matching
  - erdos-posa-property
contrasts_with:
  - covering
answers_questions:
  - "What is a packing in a graph?"
---

# Quick Definition
A packing problem asks: given a graph G and a class H of graphs, find as many disjoint subgraphs of G as possible that are each isomorphic to a graph in H.

# Core Definition
A generalization of the matching problem is to find in a given graph G as many disjoint subgraphs as possible that are each isomorphic to an element of a given class H of graphs. This is known as the **packing** problem (Diestel, p. 43).

# Prerequisites
- **Graph** — packing is defined within a graph
- **Subgraph** — we pack disjoint copies of subgraphs

# Key Properties
1. The packed subgraphs must be pairwise vertex-disjoint
2. Matching is the special case H = {K2}
3. The packing number is the maximum number of disjoint H-subgraphs
4. Related to covering by the Erdos-Posa property

# Construction / Recognition
## To Find a Packing
1. Given G and class H
2. Find subgraphs of G isomorphic to graphs in H
3. Maximize the number of pairwise vertex-disjoint such subgraphs

# Context & Application
Packing problems generalize matching to arbitrary subgraph classes. The key question is the relationship between packing and covering: if k disjoint H-subgraphs can be packed, at least k vertices are needed to cover all H-subgraphs. The Erdos-Posa property asks whether f(k) vertices always suffice.

# Examples
**Example** (p. 43): When H = {K2} (single edges), the packing problem is exactly the matching problem.

**Example** (Section 2.3): When H is the class of all cycles, the Erdos-Posa theorem gives a function f such that either k disjoint cycles exist or at most f(k) vertices cover all cycles.

# Relationships
## Builds Upon
- **Graph**, **subgraph**

## Enables
- **Erdos-Posa property** — relates packing to covering

## Related
- **Matching** — packing with H = {K2}
- **Covering** — the dual problem

## Contrasts With
- **Covering** — covering asks for few vertices meeting all H-subgraphs

# Common Errors
- **Error**: Allowing packed subgraphs to share vertices
  **Correction**: Packed subgraphs must be pairwise vertex-disjoint

# Common Confusions
- **Confusion**: Confusing vertex-disjoint packing with edge-disjoint packing
  **Clarification**: Standard packing is vertex-disjoint; edge-disjoint packing is a separate concept (treated in Section 2.4)

# Source Reference
Chapter 2, p. 43 (pdf p. 43). Detailed treatment in Section 2.3.

# Verification Notes
- Definition from p. 43
- Confidence: HIGH — explicitly defined
