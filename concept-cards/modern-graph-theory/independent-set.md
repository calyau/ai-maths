---
concept: Independent Set
slug: independent-set
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
  - independent vertices
  - independent edges
  - independent paths
  - internally disjoint paths
prerequisites:
  - graph
  - adjacency
extends: []
related:
  - empty-graph
contrasts_with: []
answers_questions:
  - "What is an independent set in a graph?"
---

# Quick Definition

A set of vertices (or edges) is independent if no two elements are adjacent. Independent paths share only their common endvertices.

# Core Definition

"A set of vertices (edges) is independent if no two elements of it are adjacent; also, $W \subset V(G)$ consists of independent vertices iff $G[W]$ is an empty graph. A set of paths is independent if for any two paths each vertex belonging to both paths is an endvertex of both" (Bollobás, p. 12). Independent paths are also called internally disjoint.

# Prerequisites

- **Graph** — Independence is defined within a graph
- **Adjacency** — Independent means no two elements are adjacent

# Key Properties

1. An independent vertex set induces an empty subgraph
2. An independent edge set is also called a matching
3. Independent paths $P_1, \ldots, P_k$ are $x$-$y$ paths with $V(P_i) \cap V(P_j) = \{x, y\}$ for $i \neq j$
4. The independence number of a graph is the size of a largest independent vertex set

# Construction / Recognition

## To verify independence of a vertex set $W$
1. Check that no edge of $G$ has both endpoints in $W$
2. Equivalently, verify $G[W]$ has no edges

# Context & Application

Independent sets appear in optimization, colouring, and Ramsey theory. The independence number is a key graph parameter. Independent paths are central to Menger's theorem on connectivity.

# Examples

**Example** (p. 12): The vertex classes $V_1$ and $V_2$ of a bipartite graph are independent sets.

# Relationships

## Builds Upon
- **Graph**, **Adjacency**

## Enables
- Chromatic number — Related to partitioning into independent sets
- Menger's theorem — Uses independent paths

## Related
- **Empty graph** — An independent vertex set induces an empty graph

# Common Errors

- **Error**: Confusing independent vertices with independent edges
  **Correction**: Independent vertices share no edge; independent edges share no vertex

# Common Confusions

- **Confusion**: Thinking independent paths must be completely vertex-disjoint
  **Clarification**: Independent paths may share endvertices; they are "internally disjoint"

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
