---
concept: Minor
slug: minor

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 29
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases:
  - "graph minor"
  - "MX"

prerequisites:
  - graph
  - subgraph
  - contraction
extends: []
related:
  - topological-minor
  - subdivision
contrasts_with:
  - topological-minor
  - subgraph

answers_questions:
  - "What is a graph minor?"
  - "What does MX mean?"
  - "What distinguishes a minor from a topological minor?"
---

# Quick Definition
X is a minor of Y if a graph isomorphic to X can be obtained from a subgraph of Y by contracting edges. Equivalently, Y contains a subgraph G with connected subsets (branch sets) that contract to the vertices of X.

# Core Definition
If G = MX is a subgraph of another graph Y, we call X a minor of Y and write X <= Y. More precisely, G is an MX if there is a partition of V(G) into connected subsets {V_x | x in V(X)} (the branch sets) such that for any two vertices x, y in X, there is a V_x-V_y edge in G if and only if xy in E(X) (Diestel, pp. 19-20).

By Proposition 1.7.1, any minor of a graph can be obtained from it by first deleting some vertices and edges, and then contracting some further edges. Conversely, any graph obtained from another by repeated deletions and contractions (in any order) is its minor.

# Prerequisites
- **Graph**, **subgraph** — a minor must occur as a contraction of a subgraph
- **Contraction** — the key operation for producing minors

# Key Properties
1. Every subgraph is a minor (no contractions needed)
2. Every graph is its own minor
3. The minor relation is a partial ordering on finite graphs (Proposition 1.7.3)
4. The minor relation is transitive
5. Branch sets are connected subsets that contract to vertices of X
6. Every topological minor is also a minor (Proposition 1.7.2(i))

# Construction / Recognition
## To Check if X is a Minor of Y
1. Find a subgraph G of Y
2. Partition V(G) into connected subsets {V_x | x in V(X)}
3. Verify: xy in E(X) iff there is a V_x-V_y edge in G

# Context & Application
The minor relation is one of the most important structural relations in graph theory. The Robertson-Seymour theorem (Chapter 12) shows that finite graphs are well-quasi-ordered by the minor relation. Kuratowski/Wagner-type theorems characterize graph classes by forbidden minors.

# Examples
**Example** (p. 20): Fig. 1.7.2 shows Y containing G = MX, making X a minor of Y.

# Relationships
## Builds Upon
- **graph**, **subgraph**, **contraction**

## Enables
- Graph structure theory, well-quasi-ordering (Chapter 12)
- Kuratowski's and Wagner's theorems (Chapter 4)

## Contrasts With
- **topological-minor** — every topological minor is a minor, but not conversely (unless Delta(X) <= 3)
- **subgraph** — every subgraph is a minor, but not conversely

# Common Confusions
- **Confusion**: Thinking minor and topological minor are the same thing
  **Clarification**: Every topological minor is a minor, but a minor need not be a topological minor. They coincide when Delta(X) <= 3 (Proposition 1.7.2(ii)).

# Source Reference
Chapter 1: The Basics, Section 1.7, pages 19-21 (pdf pp. 29-31). See Figs. 1.7.2, 1.7.4.

# Verification Notes
- Direct from pp. 19-21
- Confidence: HIGH
