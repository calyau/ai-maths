---
concept: Externally k-Connected Set
slug: externally-k-connected
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 339
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases: []
prerequisites:
  - tree-width
extends: []
related:
  - grid-theorem
  - bramble
contrasts_with: []
answers_questions:
  - "What is an externally k-connected set?"
---

# Quick Definition
A set X of vertices is externally k-connected in G if |X| >= k and for all disjoint Y, Z subsets of X with |Y| = |Z| <= k, there are |Y| disjoint Y-Z paths in G with no inner vertex or edge in G[X].

# Core Definition
A set X of vertices is *externally k-connected* in G if |X| >= k and for all disjoint subsets Y, Z of X with |Y| = |Z| <= k there are |Y| disjoint Y-Z paths in G that have no inner vertex or edge in G[X] (Diestel, p. 339).

# Prerequisites
- **Tree-width** — Large externally k-connected sets force large tree-width

# Key Properties
1. Canonical obstruction to small tree-width (like brambles and grid minors)
2. A graph has large tree-width iff it has a large externally k-connected set with k large (Exercise 35)
3. Horizontal paths in the k x k grid are externally k-connected
4. Used in the proof of the grid theorem

# Source Reference
Chapter 12, Section 12.4, page 339.

# Verification Notes
- Definition from p. 339
- Confidence: HIGH — explicit definition
