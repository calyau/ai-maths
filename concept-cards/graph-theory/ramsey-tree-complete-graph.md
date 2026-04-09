---
concept: Ramsey Number for Trees vs Complete Graphs
slug: ramsey-tree-complete-graph
category: ramsey-theory
subcategory: graph-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 265
section: "9.2 Ramsey numbers"
extraction_confidence: high
aliases:
  - "Proposition 9.2.1"
prerequisites:
  - graph-ramsey-number
related:
  - ramsey-number
answers_questions:
  - "What is R(T, K^s) for a tree T?"
---

# Quick Definition
For a tree T of order t and positive integer s: R(T, K^s) = (s-1)(t-1) + 1.

# Core Definition
**Proposition 9.2.1**: Let s, t be positive integers, and let T be a tree of order t. Then R(T, K^s) = (s-1)(t-1) + 1.

Lower bound: (s-1) copies of K_{t-1} contain no T, and the complement K^{s-1}_{t-1} contains no K^s.
Upper bound: any graph G of order (s-1)(t-1)+1 with K^s not subset G-bar has chi(G) >= t (since at most s-1 vertices share a colour), so G has a subgraph of minimum degree >= t-1, which contains T. (Diestel, pp. 255-256)

# Prerequisites
- **Graph Ramsey number** — R(T, K^s) is a graph Ramsey number

# Key Properties
1. Exact formula: one of the few classes with precisely known Ramsey numbers
2. The proof uses the chromatic number and minimum degree
3. Combines extremal and Ramsey ideas

# Source Reference
Chapter 9, Section 9.2, Proposition 9.2.1, pages 255-256 (pdf pages 265-266).

# Verification Notes
- Confidence: HIGH — proposition with complete proof
