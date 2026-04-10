---
concept: Union of k-Connected Subgraphs
slug: k-union-connectivity
category: connectivity
subcategory: structural-results
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - k-connected-graph
extends: []
related:
  - vertex-connectivity
contrasts_with: []
answers_questions:
  - "When is the union of k-connected subgraphs k-connected?"
---

# Quick Definition
If two $k$-connected subgraphs of a graph share at least $k$ common vertices, their union is also $k$-connected.

# Core Definition
For $k \ge 1$, if $G_1$ and $G_2$ are $k$-connected subgraphs of a graph $G$ having at least $k$ common vertices, then $G_1 \cup G_2$ is also $k$-connected. The proof uses the fact that any set of $k-1$ vertices leaves a common vertex in $V(G_1) \cap V(G_2)$, connecting the two parts (Bollobás, p. 81).

# Prerequisites
- **k-connected graph** — The connectivity condition

# Key Properties
1. Requires at least $k$ shared vertices
2. Proof: removing $k-1$ vertices leaves a shared vertex connecting both parts

# Context & Application
Useful for building up $k$-connected graphs from smaller pieces.

# Examples
**Example** (p. 81): If $W \subset V(G_1) \cap V(G_2)$ has $|W| \le k-1$, there exists $x \in (V(G_1) \cap V(G_2)) \setminus W$, so $G_1 - W$ and $G_2 - W$ share vertex $x$ and their union is connected.

# Relationships
## Builds Upon
- **k-connected-graph** — Property being preserved under union

# Source Reference
Chapter III, Section III.2, page 81.

# Verification Notes
- Definition source: Direct from p. 81
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
