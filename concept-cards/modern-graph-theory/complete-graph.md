---
concept: Complete Graph
slug: complete-graph
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
  - "$K_n$"
  - complete n-graph
prerequisites:
  - graph
  - graph-order-and-size
extends:
  - graph
related:
  - empty-graph
  - graph-complement
  - complete-bipartite-graph
contrasts_with:
  - empty-graph
answers_questions:
  - "What is a complete graph?"
---

# Quick Definition

The complete graph $K_n$ is the graph of order $n$ in which every two vertices are adjacent. It has $\binom{n}{2}$ edges.

# Core Definition

"A graph of order $n$ and size $\binom{n}{2}$ is called a complete $n$-graph and is denoted by $K_n$" (Bollobás, p. 11). "In $K_n$ every two vertices are adjacent." The trivial graph $K_1 = E_1$ has one vertex and no edges.

# Prerequisites

- **Graph** — $K_n$ is a graph
- **Graph order and size** — Defined by having maximum size for given order

# Key Properties

1. $K_n$ has order $n$ and size $\binom{n}{2}$
2. Every vertex has degree $n - 1$, so $K_n$ is $(n-1)$-regular
3. $K_n$ is the unique graph (up to isomorphism) of order $n$ with maximum size
4. $K_1$ is the trivial graph
5. $K_5$ is nonplanar (Bollobás, p. 31)

# Construction / Recognition

## To construct $K_n$
1. Take $n$ vertices
2. Connect every pair of distinct vertices by an edge

## To recognize $K_n$
1. Verify the graph has $n$ vertices and $\binom{n}{2}$ edges
2. Equivalently, verify every vertex has degree $n - 1$

# Context & Application

Complete graphs are fundamental objects in graph theory. $K_n$ appears as an extremal case in many theorems. The nonplanarity of $K_5$ is one of the two forbidden subgraph conditions in Kuratowski's theorem. Complete graphs also appear in the travelling salesman problem and Hamilton cycle decompositions (Theorem 11).

# Examples

**Example** (p. 12): $K_4$ is shown in Fig. I.4, having 4 vertices and 6 edges.

**Example** (p. 24): For odd $n \ge 3$, $K_n$ can be decomposed into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton cycles (Theorem 11).

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Hamilton cycle** — $K_n$ decomposition into Hamilton cycles for odd $n$
- **Kuratowski's theorem** — $K_5$ is one of the two forbidden subdivisions

## Contrasts With
- **Empty graph** — $\overline{K}_n$ has no edges; $K_n$ has all possible edges

# Common Errors

- **Error**: Thinking $K_n$ has $n^2$ edges
  **Correction**: $K_n$ has $\binom{n}{2} = n(n-1)/2$ edges

# Common Confusions

- **Confusion**: Confusing $K_n$ with the complete bipartite graph $K_{n,n}$
  **Clarification**: $K_n$ has $n$ vertices all pairwise adjacent; $K_{n,n}$ has $2n$ vertices in two classes

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 11-12.

# Verification Notes

- Definition source: Direct from p. 11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
