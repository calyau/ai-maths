---
concept: Cutvertex
slug: cutvertex
category: graph-fundamentals
subcategory: connectivity
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
  - cut vertex
  - articulation point
prerequisites:
  - graph
  - connected-graph
  - component
  - graph-deletion
extends: []
related:
  - bridge
contrasts_with:
  - bridge
answers_questions:
  - "What is a cutvertex?"
---

# Quick Definition

A cutvertex is a vertex whose deletion increases the number of components of the graph.

# Core Definition

"A cutvertex is a vertex whose deletion increases the number of components" (Bollobás, p. 14).

# Prerequisites

- **Graph** — Cutvertices are vertices of graphs
- **Connected graph** — Most naturally considered in connected graphs
- **Component** — Deletion increases component count
- **Graph deletion** — Vertex deletion operation

# Key Properties

1. Deleting a cutvertex disconnects (at least) one component
2. A tree of order $\ge 3$ has at least one cutvertex (any non-leaf vertex)
3. A connected graph with no cutvertex is called 2-connected (if order $\ge 3$)

# Construction / Recognition

To find cutvertices: for each vertex $v$, check if $G - v$ has more components than $G$.

# Context & Application

Cutvertices identify structural vulnerabilities in networks. A graph with no cutvertex (2-connected) has the property that any two vertices lie on a common cycle.

# Examples

**Example** (p. 14): In a path $P_n$ with $n \ge 3$, every internal vertex is a cutvertex.

# Relationships

## Builds Upon
- **Graph**, **Connected graph**, **Component**, **Graph deletion**

## Enables
- 2-connected graph theory
- Block decomposition of graphs

## Contrasts With
- **Bridge** — A bridge is an edge whose deletion disconnects; a cutvertex is a vertex

# Common Errors

- **Error**: Thinking only connected graphs have cutvertices
  **Correction**: Any graph can have cutvertices; deletion increases the total number of components

# Common Confusions

- **Confusion**: Confusing cutvertex with bridge
  **Clarification**: A cutvertex is a vertex; a bridge is an edge

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
