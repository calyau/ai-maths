---
concept: Separating Set
slug: separating-set
category: connectivity
subcategory: separating-sets
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "vertex separator"
  - "separator"
prerequisites:
  - graph-connectivity
extends: []
related:
  - vertex-connectivity
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "What is a separating set in a graph?"
---

# Quick Definition
A set $W$ of vertices or edges separates a connected graph $G$ if $G - W$ is disconnected. If $s$ and $t$ are in different components of $G - W$, then $W$ separates $s$ from $t$.

# Core Definition
If $G$ is connected and, for some set $W$ of vertices or edges, $G - W$ is disconnected, then we say that $W$ separates $G$. If in $G - W$ two vertices $s$ and $t$ belong to different components then $W$ separates $s$ from $t$ (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — Separating sets disconnect connected graphs

# Key Properties
1. The minimum size of a vertex separator defines $\kappa(G)$
2. The minimum size of an edge separator defines $\lambda(G)$
3. Menger's theorem relates separators to independent paths

# Context & Application
Separating sets are the fundamental objects in connectivity theory, dual to independent paths via Menger's theorem.

# Examples
**Example** (p. 80): In a $k$-connected graph, every vertex separator has at least $k$ vertices.

# Relationships
## Enables
- **vertex-connectivity** — Minimum separator size
- **mengers-theorem** — Min separator = max independent paths

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
