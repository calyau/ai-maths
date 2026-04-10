---
concept: Graph Deletion
slug: graph-deletion
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
  - vertex deletion
  - edge deletion
  - edge addition
prerequisites:
  - graph
  - subgraph
  - induced-subgraph
extends: []
related:
  - cutvertex
  - bridge
contrasts_with: []
answers_questions:
  - "How are new graphs constructed from old ones by deletion or addition?"
---

# Quick Definition

Graph deletion operations produce new graphs by removing vertices or edges. If $W \subset V(G)$, then $G - W = G[V \setminus W]$. If $E' \subset E(G)$, then $G - E' = (V(G), E(G) \setminus E')$.

# Core Definition

"If $W \subset V(G)$, then $G - W = G[V \setminus W]$ is the subgraph of $G$ obtained by deleting the vertices in $W$ and all edges incident with them. Similarly, if $E' \subset E(G)$, then $G - E' = (V(G), E(G) \setminus E')$" (Bollobás, p. 10). For singletons, $G - w$ and $G - xy$ are used. Edge addition: if $x$ and $y$ are nonadjacent, $G + xy$ is obtained by joining $x$ to $y$.

# Prerequisites

- **Graph** — The base graph being modified
- **Subgraph** — Deletion produces subgraphs
- **Induced subgraph** — Vertex deletion produces induced subgraphs

# Key Properties

1. Vertex deletion removes the vertex and all incident edges
2. Edge deletion removes edges but keeps all vertices
3. $G - W$ is an induced subgraph of $G$
4. $G - E'$ is a spanning subgraph of $G$ (when no vertices are removed)
5. Edge addition $G + xy$ requires $x$ and $y$ to be nonadjacent in $G$

# Construction / Recognition

## To delete a vertex set $W$
1. Remove all vertices in $W$ from $V(G)$
2. Remove all edges incident with any vertex in $W$

## To delete an edge set $E'$
1. Keep all vertices of $G$
2. Remove the edges in $E'$ from $E(G)$

# Context & Application

Deletion and addition operations are the basic tools for constructing inductive proofs in graph theory. They underpin the definitions of cutvertex, bridge, and many structural decompositions.

# Examples

**Example** (p. 10): These operations are illustrated through the concepts of subgraph, induced subgraph, and spanning subgraph in Fig. I.2.

# Relationships

## Builds Upon
- **Graph**, **Subgraph**, **Induced subgraph**

## Enables
- **Cutvertex** — A vertex whose deletion increases the number of components
- **Bridge** — An edge whose deletion increases the number of components

# Common Errors

- **Error**: Forgetting to remove edges incident with deleted vertices
  **Correction**: Vertex deletion always removes the vertex and all its incident edges

# Common Confusions

- **Confusion**: Thinking edge deletion also removes the endpoints
  **Clarification**: Edge deletion only removes the edge; both endvertices remain in the graph

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct from p. 10
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
