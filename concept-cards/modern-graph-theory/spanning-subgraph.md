---
concept: Spanning Subgraph
slug: spanning-subgraph
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
  - subgraph
extends:
  - subgraph
related:
  - induced-subgraph
  - spanning-tree
contrasts_with:
  - induced-subgraph
answers_questions:
  - "What is a spanning subgraph?"
---

# Quick Definition

A spanning subgraph of $G$ is a subgraph $G'$ with $V(G') = V(G)$; it contains all vertices of $G$ but possibly fewer edges.

# Core Definition

"If $V' = V$, then $G'$ is said to be a spanning subgraph of $G$" (Bollobás, p. 10). A spanning subgraph retains all vertices of the parent graph while potentially omitting some edges.

# Prerequisites

- **Graph** — The parent graph
- **Subgraph** — A spanning subgraph is a special type of subgraph

# Key Properties

1. Contains all vertices of the parent graph
2. May contain any subset of the edges of the parent graph
3. A spanning subgraph that is connected and minimal is a spanning tree

# Construction / Recognition

## To verify a spanning subgraph
1. Check $V(G') = V(G)$
2. Check $E(G') \subseteq E(G)$

# Context & Application

Spanning subgraphs appear in optimization problems where one seeks a substructure (e.g., a spanning tree) that includes all vertices while minimizing some cost function on edges.

# Examples

**Example** (p. 10): Fig. I.2 includes an example of a spanning subgraph of the graph in Fig. I.1.

# Relationships

## Builds Upon
- **Subgraph**

## Enables
- **Spanning tree** — A spanning subgraph that is also a tree

## Contrasts With
- **Induced subgraph** — Determined by vertex subset with all edges; spanning subgraph uses all vertices with possibly fewer edges

# Common Errors

- **Error**: Assuming a spanning subgraph must be connected
  **Correction**: A spanning subgraph may be disconnected

# Common Confusions

- **Confusion**: Conflating "spanning" with "induced"
  **Clarification**: Spanning means all vertices are present; induced means all edges between the chosen vertices are present

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct from p. 10
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
