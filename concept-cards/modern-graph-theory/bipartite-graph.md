---
concept: Bipartite Graph
slug: bipartite-graph
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
  - bipartition
prerequisites:
  - graph
  - cycle
extends:
  - graph
related:
  - complete-bipartite-graph
  - r-partite-graph
  - tree
contrasts_with: []
answers_questions:
  - "What is a bipartite graph?"
---

# Quick Definition

A bipartite graph has its vertex set partitioned into two classes $V_1$ and $V_2$ such that every edge joins a vertex of $V_1$ to a vertex of $V_2$. Equivalently, a graph is bipartite iff it contains no odd cycle.

# Core Definition

"A graph $G$ is a bipartite graph with vertex classes $V_1$ and $V_2$ if $V(G) = V_1 \cup V_2$, $V_1 \cap V_2 = \emptyset$ and every edge joins a vertex of $V_1$ to a vertex of $V_2$" (Bollobás, p. 14). Theorem 4: "A graph is bipartite iff it does not contain an odd cycle" (p. 16). A bipartite graph of order $n$ has at most $\lfloor n^2/4 \rfloor$ edges.

# Prerequisites

- **Graph** — A bipartite graph is a graph
- **Cycle** — Characterized by the absence of odd cycles

# Key Properties

1. Vertex set is partitioned into two independent sets $V_1, V_2$
2. No edge has both endpoints in the same class
3. Contains no odd cycle (Theorem 4)
4. Maximum size is $\lfloor n^2/4 \rfloor$, achieved by $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$
5. Every tree is bipartite
6. Every forest is bipartite

# Construction / Recognition

## To verify bipartiteness
1. Attempt a 2-colouring: pick a vertex, colour it, colour all neighbours the other colour, and continue
2. The graph is bipartite iff no contradiction arises (no edge between same-colour vertices)

# Context & Application

Bipartite graphs model situations with two distinct types of entities and connections between types (e.g., jobs and workers, incidence graphs of hypergraphs). The maximum size bound connects to Mantel's theorem and Turán's theorem.

# Examples

**Example** (p. 14): The graphs in Fig. I.1 and Fig. I.5 are bipartite.

**Example** (p. 16): The bipartition of a connected graph can be found from a vertex $x$ as $V_1 = \{y : d(x,y) \text{ is odd}\}$, $V_2 = V \setminus V_1$ (proof of Theorem 4).

# Relationships

## Builds Upon
- **Graph**, **Cycle**

## Enables
- **Complete bipartite graph** — $K_{r,s}$ is a bipartite graph with all cross-edges
- König's theorems on matchings

## Related
- **Tree** — Every tree is bipartite
- **r-partite graph** — Bipartite is the case $r = 2$

# Common Errors

- **Error**: Assuming the two vertex classes must have equal size
  **Correction**: The classes $V_1, V_2$ can have any sizes

# Common Confusions

- **Confusion**: Thinking a bipartite graph cannot contain even cycles
  **Clarification**: Bipartite graphs can contain even cycles; they just cannot contain odd cycles

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14; Theorem 4, pages 16-17.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined with characterization theorem
- Uncertainties: None
- Cross-reference status: Verified
