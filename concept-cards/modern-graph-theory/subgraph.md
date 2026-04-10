---
concept: Subgraph
slug: subgraph
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
aliases: []
prerequisites:
  - graph
extends: []
related:
  - induced-subgraph
  - spanning-subgraph
  - graph-deletion
contrasts_with:
  - induced-subgraph
  - spanning-subgraph
answers_questions:
  - "What is a subgraph?"
  - "What are the different types of subgraphs?"
---

# Quick Definition

A graph $G' = (V', E')$ is a subgraph of $G = (V, E)$ if $V' \subset V$ and $E' \subset E$, written $G' \subset G$.

# Core Definition

"We say that $G' = (V', E')$ is a subgraph of $G = (V, E)$ if $V' \subset V$ and $E' \subset E$. In this case we write $G' \subset G$" (Bollobás, p. 10). There are two important special cases: if $G'$ contains all edges of $G$ joining two vertices in $V'$, then $G'$ is the induced subgraph $G[V']$; if $V' = V$, then $G'$ is a spanning subgraph.

# Prerequisites

- **Graph** — A subgraph is defined relative to a parent graph

# Key Properties

1. A subgraph must have its vertex set contained in the parent's vertex set
2. A subgraph must have its edge set contained in the parent's edge set
3. Every edge in the subgraph must have both endvertices in the subgraph's vertex set
4. Every graph is a subgraph of itself

# Construction / Recognition

## To verify $G'$ is a subgraph of $G$
1. Check $V(G') \subseteq V(G)$
2. Check $E(G') \subseteq E(G)$

# Context & Application

Subgraphs are used extensively in graph theory to study local structure, prove properties by restriction, and build up or decompose graphs.

# Examples

**Example** (p. 10): Fig. I.2 shows a subgraph, an induced subgraph, and a spanning subgraph of the graph in Fig. I.1.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Induced subgraph** — A subgraph that includes all edges between its vertices
- **Spanning subgraph** — A subgraph that includes all vertices
- **Spanning tree** — A spanning subgraph that is a tree

## Contrasts With
- **Induced subgraph** — Must contain all edges between its vertices from the parent
- **Spanning subgraph** — Must contain all vertices of the parent

# Common Errors

- **Error**: Assuming a subgraph must be induced
  **Correction**: A subgraph may omit edges between its vertices; only induced subgraphs must retain all such edges

# Common Confusions

- **Confusion**: Conflating subgraph with induced subgraph
  **Clarification**: A subgraph $G'$ is induced only if $G' = G[V(G')]$; otherwise it is merely a subgraph

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct quote from p. 10
- Confidence rationale: Explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
