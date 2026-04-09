---
concept: Branch Set
slug: branch-set

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 28
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases: []

prerequisites:
  - graph
  - minor
  - connected-graph
extends: []
related:
  - contraction
contrasts_with: []

answers_questions:
  - "What is a branch set in a graph minor?"
---

# Quick Definition
In an MX (a graph that contracts to X), the branch sets are the connected subsets {V_x | x in V(X)} that partition the vertices and contract to the vertices of X.

# Core Definition
If X is another graph and {V_x | x in V(X)} is a partition of V into connected subsets such that, for any two vertices x, y in X, there is a V_x-V_y edge in G if and only if xy in E(X), we call G an MX. The sets V_x are the branch sets of this MX. Intuitively, we obtain X from G by contracting every branch set to a single vertex (Diestel, p. 19).

# Prerequisites
- **Graph**, **minor**, **connected-graph** — branch sets must be connected

# Key Properties
1. Branch sets are connected subsets of V(G)
2. They partition V(G)
3. Edges between branch sets correspond exactly to edges in X
4. In infinite graphs, branch sets may be infinite

# Relationships
## Builds Upon
- **minor**, **connected-graph**

# Source Reference
Chapter 1: The Basics, Section 1.7, page 19 (pdf p. 29). See Fig. 1.7.2.

# Verification Notes
- Direct from p. 19
- Confidence: HIGH
