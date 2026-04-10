---
concept: Graph Union and Join
slug: graph-union-and-join
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
  - graph union
  - graph join
  - "$G \\cup H$"
  - "$G + H$"
prerequisites:
  - graph
extends: []
related:
  - complete-bipartite-graph
contrasts_with: []
answers_questions:
  - "How are graph union and join defined?"
---

# Quick Definition

The union $G \cup H$ has vertex set $V(G) \cup V(H)$ and edge set $E(G) \cup E(H)$. The join $G + H$ is obtained from $G \cup H$ by adding all edges between $G$ and $H$.

# Core Definition

"We shall write $G \cup H = (V(G) \cup V(H), E(G) \cup E(H))$ and $kG$ for the union of $k$ disjoint copies of $G$. We obtain the join $G + H$ from $G \cup H$ by adding all edges between $G$ and $H$" (Bollobás, p. 15).

# Prerequisites

- **Graph** — Operations defined on graphs

# Key Properties

1. Union preserves existing edges; join adds cross-edges
2. $K_{2,3} = \overline{K}_2 + \overline{K}_3$
3. $kG$ denotes $k$ disjoint copies of $G$

# Construction / Recognition

Union: combine vertex sets and edge sets. Join: take the union and add all possible edges between the two graphs.

# Context & Application

These operations are used to build compound graphs from simpler ones. The join operation produces complete multipartite graphs from empty graphs.

# Examples

**Example** (p. 15): $K_{2,3} = E_2 + E_3 = \overline{K}_2 + \overline{K}_3$.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Complete bipartite graph** — Expressible as a join of empty graphs

# Common Errors

- **Error**: Confusing union with join
  **Correction**: Union preserves existing structure; join adds all cross-edges

# Common Confusions

- **Confusion**: Thinking $G + H$ means adding one edge between $G$ and $H$
  **Clarification**: The join adds all possible edges between the vertex sets of $G$ and $H$

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 15.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
