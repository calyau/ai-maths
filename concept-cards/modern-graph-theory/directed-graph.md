---
concept: Directed Graph
slug: directed-graph
category: graph-fundamentals
subcategory: basic-definitions
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
  - digraph
  - oriented graph
prerequisites:
  - graph
extends:
  - graph
related:
  - multigraph
contrasts_with:
  - graph
answers_questions:
  - "What is a directed graph?"
  - "What is an oriented graph?"
---

# Quick Definition

A directed graph (digraph) has ordered pairs of vertices as edges. An edge $(a, b)$, denoted $\overrightarrow{ab}$, goes from $a$ to $b$. An oriented graph is a digraph obtained by orienting the edges of an undirected graph.

# Core Definition

"If the edges are ordered pairs of vertices, then we get the notions of a directed graph and directed multigraph. An ordered pair $(a, b)$ is said to be an edge directed from $a$ to $b$, or an edge beginning at $a$ and ending at $b$" (Bollobás, p. 16). A vertex $x$ has outdegree $d^+(x)$ and indegree $d^-(x)$.

"An oriented graph is a directed graph obtained by orienting the edges of a graph, that is, by giving the edge $ab$ an orientation $\overrightarrow{ab}$ or $\overrightarrow{ba}$" (p. 16).

# Prerequisites

- **Graph** — A directed graph extends the graph concept with edge orientations

# Key Properties

1. Edges are ordered pairs: $\overrightarrow{ab} \neq \overrightarrow{ba}$
2. Each vertex has an outdegree $d^+(x)$ and indegree $d^-(x)$
3. Directed cycle partition: edge set partitions into directed cycles iff $d^+(x) = d^-(x)$ for all $x$
4. An oriented graph has at most one of $\overrightarrow{ab}$ and $\overrightarrow{ba}$

# Construction / Recognition

An oriented graph is constructed by assigning a direction to each edge of an undirected graph. A general digraph may have both $\overrightarrow{ab}$ and $\overrightarrow{ba}$.

# Context & Application

Directed graphs model asymmetric relationships (one-way streets, web links, tournament results). They are essential for electrical networks (edges are oriented for current direction) and for the matrix-tree theorem.

# Examples

**Example** (p. 16): Theorem 1 has a directed variant: the edge set of a directed multigraph partitions into directed cycles iff $d^+(x) = d^-(x)$ for every vertex $x$.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Kirchhoff's current law** — Requires oriented edges for current direction
- **BEST theorem** — Counts directed Euler circuits

## Contrasts With
- **Graph** — Undirected edges are unordered pairs

# Common Errors

- **Error**: Assuming an oriented graph can have both $\overrightarrow{ab}$ and $\overrightarrow{ba}$
  **Correction**: An oriented graph has at most one direction per edge pair; a general digraph may have both

# Common Confusions

- **Confusion**: Confusing "directed graph" with "oriented graph"
  **Clarification**: An oriented graph is a special directed graph obtained by orienting an undirected graph; a general directed graph may have both $\overrightarrow{ab}$ and $\overrightarrow{ba}$

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 16.

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
