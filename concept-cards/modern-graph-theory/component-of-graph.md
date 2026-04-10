---
concept: Component of a Graph
slug: component-of-graph
category: connectivity
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "connected component"
prerequisites:
  - graph-connectivity
extends: []
related:
  - odd-component
  - block-of-graph
contrasts_with: []
answers_questions:
  - "What is a component of a graph?"
---

# Quick Definition
A component of a graph $G$ is a maximal connected subgraph.

# Core Definition
A maximal connected subgraph of a graph $G$ is a component of $G$ (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — Components are defined via connectivity

# Key Properties
1. Every graph partitions into its components
2. Different components share no vertices
3. An odd component has an odd number of vertices
4. The number of components is denoted by $c(G)$ or $\omega(G)$ in some texts

# Context & Application
Components are the basic building blocks of graph structure. Odd components are key in Tutte's theorem.

# Examples
**Example** (p. 80): A disconnected graph has $\ge 2$ components.

# Relationships
## Builds Upon
- **graph-connectivity** — Components = maximal connected subgraphs

## Enables
- **odd-component** — Components with odd order
- **block-of-graph** — Finer decomposition within components

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
