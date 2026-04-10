---
concept: Subdivision
slug: subdivision
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - topological graph
  - TG
prerequisites:
  - graph
extends: []
related:
  - kuratowskis-theorem
  - graph-minor
contrasts_with:
  - graph-minor
answers_questions:
  - "What is a subdivision of a graph?"
---

# Quick Definition

A subdivision of a graph $G$ (denoted $TG$) is obtained from $G$ by replacing edges with paths. Two graphs are homeomorphic if they have isomorphic subdivisions.

# Core Definition

"A graph $H$ is said to be a subdivision of a graph $G$, or a topological $G$ graph if $H$ is obtained from $G$ by subdividing some of the edges, that is, by replacing the edges by paths having at most their endvertices in common. We shall write $TG$ for a topological $G$ graph" (Bollobás, p. 29). For example, $TK_3$ is an arbitrary cycle, and $TC_8$ is any cycle of length $\ge 8$.

# Prerequisites

- **Graph** — Subdivisions are defined for graphs

# Key Properties

1. Subdividing preserves topological type: $R(G)$ and $R(TG)$ are homeomorphic
2. $TK_3$ = any cycle; $TC_8$ = any cycle of length $\ge 8$
3. If $G$ is nonplanar, so is every graph containing a $TG$
4. Kuratowski's theorem uses subdivisions of $K_5$ and $K_{3,3}$

# Construction / Recognition

To subdivide edge $xy$: replace $xy$ with a path $x, v_1, v_2, \ldots, v_k, y$ introducing new vertices.

# Context & Application

Subdivisions are the foundation of Kuratowski's theorem, which characterizes planar graphs by the absence of subdivisions of $K_5$ and $K_{3,3}$.

# Examples

**Example** (p. 29): $TK_3$ is an arbitrary cycle. $TC_8$ is any cycle of length at least 8.

**Example** (p. 32): Fig. I.20 shows graphs containing $TK_5$ and $TK_{3,3}$, proving their nonplanarity.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Kuratowski's theorem** — Planarity characterized by absence of $TK_5$ and $TK_{3,3}$

## Contrasts With
- **Graph minor** — Minors use contraction; subdivisions use edge replacement

# Common Errors

- **Error**: Thinking subdivision changes the graph's topological type
  **Correction**: Subdivision preserves the topological type (homeomorphism class)

# Common Confusions

- **Confusion**: Confusing subdivision with minor
  **Clarification**: Subdivision adds vertices to edges; taking a minor contracts edges and deletes vertices/edges

# Source Reference

Chapter I: Fundamentals, Section I.4, page 29.

# Verification Notes

- Definition source: Direct from p. 29
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
