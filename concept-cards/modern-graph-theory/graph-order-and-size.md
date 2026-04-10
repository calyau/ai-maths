---
concept: Graph Order and Size
slug: graph-order-and-size
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
  - order of a graph
  - size of a graph
prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - complete-graph
contrasts_with: []
answers_questions:
  - "What is the order of a graph?"
  - "What is the size of a graph?"
---

# Quick Definition

The order of a graph $G$ is the number of vertices, denoted $|G| = |V(G)|$. The size is the number of edges, denoted $e(G)$.

# Core Definition

"The order of $G$ is the number of vertices in $G$; it is denoted by $|G|$. [...] Thus $|G| = |V(G)|$. The size of $G$ is the number of edges in $G$; it is denoted by $e(G)$" (Bollobás, p. 10). The notation $G^n$ denotes an arbitrary graph of order $n$, and $G(n, m)$ denotes one of order $n$ and size $m$.

# Prerequisites

- **Graph** — Order and size are defined for graphs
- **Vertex** — Order counts vertices
- **Edge** — Size counts edges

# Key Properties

1. $0 \le e(G) \le \binom{n}{2}$ for a graph of order $n$
2. For every $m$ with $0 \le m \le \binom{n}{2}$, there exists a graph $G(n, m)$
3. A graph with $\binom{n}{2}$ edges is the complete graph $K_n$
4. A graph with 0 edges is the empty graph $\overline{K}_n$

# Construction / Recognition

Order is determined by counting $|V(G)|$; size by counting $|E(G)|$.

# Context & Application

Order and size are the most basic numerical invariants of a graph. They appear in virtually every bound and theorem in graph theory, such as Euler's formula ($n - m + f = 2$) and the handshaking lemma ($\sum d(x_i) = 2e(G)$).

# Examples

**Example** (p. 11): $K_4$ has order 4 and size $\binom{4}{2} = 6$. The path $P_4$ has order 5 and size 4.

# Relationships

## Builds Upon
- **Graph**, **Vertex**, **Edge**

## Enables
- **Handshaking lemma** — Relates sum of degrees to twice the size
- **Complete graph** — The graph achieving maximum size for given order

# Common Errors

- **Error**: Confusing order and size
  **Correction**: Order = number of vertices; size = number of edges

# Common Confusions

- **Confusion**: Thinking $|G|$ denotes the number of edges
  **Clarification**: $|G|$ denotes order (vertices); $e(G)$ denotes size (edges)

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 10.

# Verification Notes

- Definition source: Direct from p. 10
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
