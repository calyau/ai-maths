---
concept: Neighbourhood
slug: neighbourhood
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
  - open neighbourhood
  - closed neighbourhood
  - "$\\Gamma(x)$"
prerequisites:
  - graph
  - adjacency
extends: []
related:
  - vertex-degree
contrasts_with: []
answers_questions:
  - "What is the neighbourhood of a vertex?"
---

# Quick Definition

The neighbourhood $\Gamma(x)$ of a vertex $x$ is the set of all vertices adjacent to $x$. The closed neighbourhood is $\Gamma(x) \cup \{x\}$.

# Core Definition

"The set of vertices adjacent to a vertex $x \in G$, the neighbourhood of $x$, is denoted by $\Gamma(x)$. Occasionally one calls $\Gamma(x)$ the open neighbourhood of $x$, and $\Gamma(x) \cup \{x\}$ the closed neighbourhood of $x$" (Bollobás, p. 11). When emphasis on the underlying graph is needed, $\Gamma_G(x)$ is used. For an induced subgraph $H = G[W]$, $\Gamma_H(x) = \Gamma_G(x) \cap W$.

# Prerequisites

- **Graph** — Neighbourhoods are defined within graphs
- **Adjacency** — A neighbour is an adjacent vertex

# Key Properties

1. $\Gamma(x) = \{y \in V(G) : xy \in E(G)\}$
2. $|\Gamma(x)| = d(x)$, the degree of $x$
3. $y \in \Gamma(x) \iff x \in \Gamma(y) \iff xy \in E(G)$
4. In an induced subgraph $H = G[W]$: $\Gamma_H(x) = \Gamma_G(x) \cap W$

# Construction / Recognition

To find $\Gamma(x)$: collect all vertices $y$ such that $xy \in E(G)$.

# Context & Application

Neighbourhoods are the basis for defining degree, local structure, and many graph algorithms. They play a key role in proofs such as Mantel's theorem (Theorem 2), where the condition $\Gamma(x) \cap \Gamma(y) = \emptyset$ for every edge $xy$ characterizes triangle-free graphs.

# Examples

**Example** (p. 11): For any vertex $x$, $y \in \Gamma(x)$, $x \in \Gamma(y)$, $x \sim y$, and $y \sim x$ are all equivalent.

# Relationships

## Builds Upon
- **Graph**, **Adjacency**

## Enables
- **Vertex degree** — $d(x) = |\Gamma(x)|$

# Common Errors

- **Error**: Including $x$ in the open neighbourhood $\Gamma(x)$
  **Correction**: The open neighbourhood excludes $x$ itself; the closed neighbourhood includes it

# Common Confusions

- **Confusion**: Conflating open and closed neighbourhood
  **Clarification**: Open neighbourhood $\Gamma(x)$ excludes $x$; closed neighbourhood $\Gamma(x) \cup \{x\}$ includes $x$

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 11.

# Verification Notes

- Definition source: Direct from p. 11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
