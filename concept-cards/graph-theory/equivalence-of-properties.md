---
concept: Equivalence of Graph Properties (Kuratowski Framework)
slug: equivalence-of-properties
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 280
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "P <= P'"
  - "P ~ P'"
prerequisites:
  - kuratowski-set
related:
  - unavoidable-substructures-connected
answers_questions:
  - "How are graph properties compared in Ramsey theory?"
---

# Quick Definition
Two graph properties P, P' (each containing arbitrarily large graphs) are equivalent (P ~ P') if for every G in P there is G' in P' with G <= G', and vice versa, where <= is a chosen order relation (subgraph, minor, etc.).

# Core Definition
Given an order relation <= between graphs (subgraph, topological minor, or minor), write P <= P' if for every G in P there is G' in P' with G <= G'. If P <= P' and P >= P', write P ~ P' (equivalent). A Kuratowski set is a finite set of pairwise incomparable properties {P_1, ..., P_k} such that every P in the collection has some P_i <= P. (Diestel, p. 270)

# Prerequisites
- **Kuratowski set** — This formalizes the comparison

# Key Properties
1. ~ is an equivalence relation on graph properties
2. Different order relations (subgraph, minor, topological minor) yield different Kuratowski sets
3. For k-connected graphs, the Kuratowski set changes with k and the order relation

# Source Reference
Chapter 9, Section 9.4, page 270 (pdf page 280).

# Verification Notes
- Confidence: HIGH — formally defined
