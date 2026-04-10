---
concept: Rank of a Multigraph
slug: rank-of-multigraph
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 342
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "r(G)"
  - "graph rank"
prerequisites: []
extends: []
related:
  - nullity-of-multigraph
  - rank-generating-polynomial
contrasts_with:
  - nullity-of-multigraph
answers_questions:
  - "What must I know before understanding the Tutte polynomial?"
---

# Quick Definition
The rank of a multigraph $G = (V, E)$ is $r(G) = |V| - k(G)$, where $k(G)$ is the number of components.

# Core Definition
"The rank $r(G)$ and nullity $n(G)$ of $G$ are defined as for graphs: $r(G) = |V| - k(G) = |G| - k(G)$ and $n(G) = |E| - |V| + k(G)$" (Bollobás, p. 342). For a spanning subgraph $(V, F)$: $r(F) = |V| - k(F)$.

# Prerequisites
This is a foundational concept with no prerequisites.

# Key Properties
1. $r(G) = |V| - k(G)$ = number of vertices minus number of components
2. For connected $G$: $r(G) = |V| - 1$
3. $r(G) = |E(T)|$ where $T$ is any spanning forest
4. $r(E) - r(F) = k(F) - k(E)$: measures how many more components $F$ has than $G$
5. $\deg_x T_G = r(G)$

# Context & Application
Rank appears as the exponent of $(x-1)$ in the Tutte polynomial definition and measures the "tree part" of the graph.

# Examples
**Example**: $r(K_n) = n - 1$. $r(E_n) = 0$ (empty graph, $n$ components).

# Relationships
## Enables
- **tutte-polynomial**, **rank-generating-polynomial**

## Contrasts With
- **nullity-of-multigraph** — Measures the "cycle part" while rank measures the "tree part"

# Source Reference
Chapter X, Section X.1, page 342.

# Verification Notes
- Definition source: Direct from p. 342
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
