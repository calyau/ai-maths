---
concept: Graph Minor
slug: graph-minor
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
  - minor
  - edge contraction
prerequisites:
  - graph
  - subgraph
extends: []
related:
  - subdivision
  - kuratowskis-theorem
  - wagners-theorem
contrasts_with:
  - subdivision
answers_questions:
  - "What is a graph minor?"
  - "What is edge contraction?"
---

# Quick Definition

A graph $H$ is a minor of $G$ if $H$ can be obtained from $G$ by a sequence of vertex deletions, edge deletions, and edge contractions. Edge contraction of $xy$ identifies $x$ and $y$ and removes loops and duplicate edges.

# Core Definition

"Given an edge $xy$ of a graph $G$, the graph $G/xy$ is obtained from $G$ by contracting the edge $xy$; that is, to get $G/xy$ we identify the vertices $x$ and $y$ and remove all resulting loops and duplicate edges. [...] A graph $H$ is a minor of $G$, written $G \succ H$, if it is a subgraph of a graph obtained from $G$ by a sequence of edge-contractions" (Bollobás, p. 32).

# Prerequisites

- **Graph** — Minors are defined for graphs
- **Subgraph** — A minor is a subgraph of a contraction

# Key Properties

1. $G \supset TH$ implies $G \succ H$ (having a subdivision implies having a minor)
2. If $H$ has maximum degree $\le 3$, then $G \supset TH$ iff $G \succ H$
3. If $G \succ K_5$ then either $G \supset TK_5$ or $G \supset TK_{3,3}$
4. The minor relation is a partial order on graphs (up to isomorphism)

# Construction / Recognition

## Edge contraction $G/xy$
1. Identify vertices $x$ and $y$ into a single vertex
2. Remove any resulting loops
3. Remove any resulting duplicate edges

## To find a minor
1. Delete vertices, delete edges, and contract edges in any order

# Context & Application

Minors are central to Wagner's theorem (Theorem 18) and the Robertson-Seymour theorem (graph minor theorem), which proves that any minor-closed graph property can be characterized by a finite set of forbidden minors.

# Examples

**Example** (p. 32): Fig. I.21 shows a graph $G$, its contraction $G/xy$, and a minor $H$.

# Relationships

## Builds Upon
- **Graph**, **Subgraph**

## Enables
- **Wagner's theorem** — Planarity characterized by forbidden minors

## Related
- **Kuratowski's theorem** — Equivalent characterization using subdivisions

## Contrasts With
- **Subdivision** — Subdivisions add vertices; minors contract edges

# Common Errors

- **Error**: Forgetting to remove loops and duplicate edges after contraction
  **Correction**: Contraction in simple graphs always removes loops and duplicates

# Common Confusions

- **Confusion**: Thinking minor and subdivision are the same
  **Clarification**: Having a subdivision implies having a minor, but not vice versa (for high-degree graphs)

# Source Reference

Chapter I: Fundamentals, Section I.4, pages 32-33.

# Verification Notes

- Definition source: Direct from p. 32
- Confidence rationale: Explicitly defined
- Uncertainties: Some OCR artifacts in source text
- Cross-reference status: Verified
