---
concept: Factor of a Graph
slug: factor-of-graph
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases:
  - "spanning subgraph"
  - "r-factor"
prerequisites: []
extends: []
related:
  - one-factor
  - matching
contrasts_with: []
answers_questions:
  - "What is a factor of a graph?"
---

# Quick Definition
A factor of a graph $G$ is a spanning subgraph — a subgraph containing all vertices of $G$. An $r$-factor is a factor where every vertex has degree $r$.

# Core Definition
A factor of a graph is a spanning subgraph: a subgraph whose vertex set is that of the whole graph. If every vertex of a factor has degree $r$, then we call it an $r$-factor (Bollobás, p. 90).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A 1-factor is a perfect matching
2. A 2-factor is a union of vertex-disjoint cycles covering all vertices
3. An $r$-factor requires $rn/2$ edges (so $rn$ must be even)

# Construction / Recognition
1. Check the subgraph uses all vertices of $G$
2. For an $r$-factor: verify every vertex has degree exactly $r$

# Context & Application
The existence of 1-factors is characterized by Tutte's theorem (Theorem 14).

# Examples
**Example** (p. 90): A 1-factor of a graph is shown in Fig. III.6.

# Relationships
## Enables
- **one-factor** — A factor with degree 1

# Source Reference
Chapter III, Section III.4, page 90.

# Verification Notes
- Definition source: Direct from p. 90
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
