---
concept: Odd Component
slug: odd-component
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 49
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "component of odd order"
prerequisites:
  - graph
  - component
extends: []
related:
  - tuttes-theorem
  - tuttes-condition
contrasts_with: []
answers_questions:
  - "What is an odd component?"
---

# Quick Definition
An odd component of a graph is a connected component with an odd number of vertices.

# Core Definition
Given a graph G, let q(G) denote the number of its **odd components**, those of odd order (Diestel, p. 49).

# Prerequisites
- **Graph** — odd components are components of a graph
- **Component** — a maximal connected subgraph

# Key Properties
1. An odd component has an odd number of vertices
2. q(G) denotes the number of odd components of G
3. If G has a 1-factor, every odd component of G-S sends at least one factor edge to S
4. The parity constraint is crucial: odd components cannot be internally perfectly matched

# Construction / Recognition
## To Count Odd Components
1. Find all connected components of G
2. Count the vertices in each component
3. A component is odd if its vertex count is odd
4. q(G) = number of odd components

# Context & Application
Odd components are central to Tutte's 1-factor theorem. The key observation is that if G has a 1-factor and S is any vertex set, each odd component of G-S must send at least one factor edge to S (since it cannot match all its own vertices internally). This gives the necessary condition q(G-S) <= |S|.

# Examples
**Example** (p. 49-50, Fig. 2.2.1): The figure shows a graph with S removed, leaving several components, three of which are odd. The contracted graph G_S is also depicted.

# Relationships
## Builds Upon
- **Component** — an odd component is a component with odd order

## Enables
- **Tutte's condition** — q(G-S) <= |S|
- **Tutte's theorem** — characterizes 1-factor existence via odd components

# Common Errors
- **Error**: Counting all components, not just odd ones
  **Correction**: Only components with an odd number of vertices are odd components; even components can be perfectly matched internally

# Common Confusions
- **Confusion**: Thinking an odd component has odd-length edges
  **Clarification**: "Odd" refers to the number of vertices (order), not edges or edge lengths

# Source Reference
Chapter 2, Section 2.2, p. 49 (pdf p. 49).

# Verification Notes
- Definition from p. 49
- Confidence: HIGH — explicitly defined
