---
concept: Complete Bipartite Graph
slug: complete-bipartite-graph
category: graph-fundamentals
subcategory: special-graphs
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - "$K_{p,q}$"
  - "$K(n_1, \\ldots, n_r)$"
  - complete r-partite graph
prerequisites:
  - graph
  - bipartite-graph
extends:
  - bipartite-graph
related:
  - complete-graph
  - r-partite-graph
contrasts_with:
  - complete-graph
answers_questions:
  - "What is a complete bipartite graph?"
  - "What is a complete r-partite graph?"
---

# Quick Definition

The complete bipartite graph $K_{p,q}$ has vertex classes of sizes $p$ and $q$ with every vertex of one class adjacent to every vertex of the other. More generally, $K(n_1, \ldots, n_r)$ is the complete $r$-partite graph.

# Core Definition

"The symbol $K(n_1, \ldots, n_r)$ denotes a complete $r$-partite graph: it has $n_i$ vertices in the $i$th class and contains all edges joining vertices in distinct classes. For simplicity, we often write $K_{p,q}$ instead of $K(p,q)$" (Bollobás, p. 15). Also, $K_r(t)$ denotes $K(t, \ldots, t)$ with $r$ equal classes.

# Prerequisites

- **Graph** — $K_{p,q}$ is a graph
- **Bipartite graph** — $K_{p,q}$ is a bipartite graph with all possible cross-edges

# Key Properties

1. $K_{p,q}$ has $p + q$ vertices and $pq$ edges
2. $K_{p,q}$ is bipartite with one class of degree $q$ and the other of degree $p$
3. $K_{3,3}$ (the Thomsen graph) is nonplanar (p. 31)
4. $K_{2,3} = \overline{K}_2 + \overline{K}_3$ (as a join)
5. $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ is the unique densest bipartite graph of order $n$

# Construction / Recognition

1. Partition vertices into classes
2. Connect every vertex in each class to every vertex in every other class
3. No edges within a class

# Context & Application

Complete bipartite graphs appear in planarity theory ($K_{3,3}$ is one of the two forbidden subdivisions in Kuratowski's theorem), extremal graph theory (maximum triangle-free graphs), and as building blocks in graph decompositions.

# Examples

**Example** (p. 15): $K_{2,3} = E_2 + E_3 = \overline{K}_2 + \overline{K}_3$.

**Example** (p. 31): $K_{3,3}$ is nonplanar since its girth is 4 and $e(K_{3,3}) = 9 > (4/(4-2))(6-2) = 8$.

# Relationships

## Builds Upon
- **Bipartite graph**

## Enables
- **Kuratowski's theorem** — $K_{3,3}$ is one of two forbidden subdivisions for planarity

## Related
- **Complete graph** — $K_n$ is the complete 1-class graph (all vertices in one class)
- **r-partite graph** — Generalization to $r$ classes

## Contrasts With
- **Complete graph** — $K_n$ allows all edges; $K_{p,q}$ only allows cross-class edges

# Common Errors

- **Error**: Confusing $K_{n,n}$ with $K_n$
  **Correction**: $K_{n,n}$ has $2n$ vertices and $n^2$ edges; $K_n$ has $n$ vertices and $\binom{n}{2}$ edges

# Common Confusions

- **Confusion**: Thinking $K_{3,3}$ is planar because it has few edges
  **Clarification**: $K_{3,3}$ is nonplanar; its girth-based bound shows $e(K_{3,3}) = 9$ exceeds the planar maximum of 8

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 15; Section I.4, page 31.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
