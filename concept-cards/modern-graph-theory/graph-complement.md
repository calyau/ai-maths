---
concept: Graph Complement
slug: graph-complement
category: graph-fundamentals
subcategory: graph-operations
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
  - complement of a graph
  - "$\\overline{G}$"
prerequisites:
  - graph
  - complete-graph
extends: []
related:
  - empty-graph
contrasts_with: []
answers_questions:
  - "What is the complement of a graph?"
---

# Quick Definition

The complement $\overline{G}$ of a graph $G = (V, E)$ is the graph $(V, V^{(2)} - E)$: two vertices are adjacent in $\overline{G}$ iff they are not adjacent in $G$.

# Core Definition

"For a graph $G = (V, E)$ the complement of $G$ is $\overline{G} = (V, V^{(2)} - E)$; thus, two vertices are adjacent in $\overline{G}$ if and only if they are not adjacent in $G$" (Bollobás, p. 11).

# Prerequisites

- **Graph** — The complement is defined for graphs
- **Complete graph** — $\overline{G}$ has the edges $K_n$ is missing from $G$

# Key Properties

1. $\overline{G}$ has the same vertex set as $G$
2. $e(G) + e(\overline{G}) = \binom{n}{2}$
3. $\overline{\overline{G}} = G$ — complement is an involution
4. $\overline{K}_n = E_n$ and $\overline{E}_n = K_n$

# Construction / Recognition

## To construct $\overline{G}$
1. Keep all vertices of $G$
2. For each pair of distinct vertices, include the edge iff it is absent in $G$

# Context & Application

Complements appear in Ramsey theory and in relating graph properties to their "dual" properties. For example, a clique in $G$ corresponds to an independent set in $\overline{G}$.

# Examples

**Example** (p. 11): $\overline{K}_n$ is the empty graph of order $n$, the complement of $K_n$.

# Relationships

## Builds Upon
- **Graph**, **Complete graph**

## Enables
- Relating cliques to independent sets
- Ramsey-type arguments

## Related
- **Empty graph** — The complement of the complete graph

# Common Errors

- **Error**: Complementing edges without keeping the same vertex set
  **Correction**: The complement always has the same vertex set as the original

# Common Confusions

- **Confusion**: Thinking the complement of a connected graph must be disconnected
  **Clarification**: Both $G$ and $\overline{G}$ can be connected; in fact, at least one of them is always connected

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 11.

# Verification Notes

- Definition source: Direct from p. 11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
