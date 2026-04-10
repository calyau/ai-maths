---
concept: Induced Subgraph
slug: induced-subgraph
category: graph-fundamentals
subcategory: graph-operations
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
  - spanned subgraph
prerequisites:
  - graph
  - subgraph
extends:
  - subgraph
related:
  - spanning-subgraph
  - graph-deletion
contrasts_with:
  - subgraph
  - spanning-subgraph
answers_questions:
  - "What is an induced subgraph?"
---

# Quick Definition

An induced subgraph $G[V']$ is the subgraph of $G$ whose vertex set is $V'$ and whose edge set consists of all edges of $G$ that join two vertices in $V'$.

# Core Definition

"If $G'$ contains all edges of $G$ that join two vertices in $V'$ then $G'$ is said to be the subgraph induced or spanned by $V'$ and is denoted by $G[V']$. Thus, a subgraph $G'$ of $G$ is an induced subgraph if $G' = G[V(G')]$" (Bollobás, p. 10).

# Prerequisites

- **Graph** — The parent graph from which the subgraph is induced
- **Subgraph** — An induced subgraph is a special type of subgraph

# Key Properties

1. Uniquely determined by the vertex set $V'$: the edge set is forced
2. $G' = G[V(G')]$ characterizes induced subgraphs among all subgraphs
3. The induced subgraph $G[V']$ has all edges of $G$ with both endpoints in $V'$

# Construction / Recognition

## To construct $G[V']$
1. Take the vertex set $V' \subseteq V(G)$
2. Include every edge $xy \in E(G)$ where both $x, y \in V'$

# Context & Application

Induced subgraphs preserve the local adjacency structure of the original graph. They are central to forbidden subgraph characterizations (e.g., bipartite iff no odd cycle as induced subgraph of any closed walk).

# Examples

**Example** (p. 10): Fig. I.2 illustrates an induced subgraph of the graph in Fig. I.1.

# Relationships

## Builds Upon
- **Subgraph** — An induced subgraph is a subgraph with maximal edges

## Enables
- **Graph deletion** — $G - W = G[V \setminus W]$ is an induced subgraph

## Contrasts With
- **Subgraph** — A subgraph may omit some edges between its vertices
- **Spanning subgraph** — Uses all vertices but may omit edges

# Common Errors

- **Error**: Selecting a vertex subset and then arbitrarily choosing which edges to include
  **Correction**: An induced subgraph must include all edges between the selected vertices

# Common Confusions

- **Confusion**: Thinking "induced subgraph" and "subgraph" are synonymous
  **Clarification**: Every induced subgraph is a subgraph, but not every subgraph is induced

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct quote from p. 10
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
