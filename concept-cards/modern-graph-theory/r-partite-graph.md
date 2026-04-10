---
concept: r-Partite Graph
slug: r-partite-graph
category: graph-fundamentals
subcategory: special-graphs
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
  - multipartite graph
  - k-partite graph
prerequisites:
  - graph
  - bipartite-graph
extends:
  - bipartite-graph
related:
  - complete-bipartite-graph
contrasts_with: []
answers_questions:
  - "What is an r-partite graph?"
---

# Quick Definition

An $r$-partite graph has its vertex set partitioned into $r$ classes such that no edge joins two vertices in the same class. A 2-partite graph is a bipartite graph.

# Core Definition

"$G$ is $r$-partite with vertex classes $V_1, V_2, \ldots, V_r$ (or $r$-partition $(V_1, \ldots, V_r)$) if $V(G) = V_1 \cup V_2 \cup \cdots \cup V_r$, $V_i \cap V_j = \emptyset$ whenever $1 \le i < j \le r$, and no edge joins two vertices in the same class" (Bollobás, p. 14).

# Prerequisites

- **Graph** — An $r$-partite graph is a graph
- **Bipartite graph** — The case $r = 2$

# Key Properties

1. Each vertex class is an independent set
2. Bipartite graphs are $r$-partite with $r = 2$
3. $K(n_1, \ldots, n_r)$ is the complete $r$-partite graph with all cross-class edges
4. $K_r(t) = K(t, \ldots, t)$ has $r$ classes each of size $t$

# Construction / Recognition

Partition $V(G)$ into $r$ non-empty classes with no intra-class edges.

# Context & Application

Multipartite graphs appear in Turán's theorem (Chapter IV): the densest $K_{r+1}$-free graph is the complete $r$-partite graph with balanced parts.

# Examples

**Example** (p. 15): $K_{2,3} = \overline{K}_2 + \overline{K}_3$ is a complete bipartite (2-partite) graph.

# Relationships

## Builds Upon
- **Bipartite graph** — $r$-partite generalizes bipartite

## Enables
- Turán's theorem (densest $K_{r+1}$-free graphs)

## Related
- **Complete bipartite graph** — The complete version

# Common Errors

- **Error**: Requiring exactly $r$ classes of equal size
  **Correction**: The classes can have different sizes

# Common Confusions

- **Confusion**: Thinking $r$-partite means $r$-colourable
  **Clarification**: They are equivalent: $r$-partite = $r$-colourable (chromatic number $\le r$)

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
