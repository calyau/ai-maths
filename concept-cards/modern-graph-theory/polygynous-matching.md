---
concept: Polygynous Matching
slug: polygynous-matching
category: matchings
subcategory: extensions
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Corollary 11"
  - "degree-constrained matching"
prerequisites:
  - halls-theorem
extends:
  - halls-theorem
related:
  - bipartite-max-flow-min-cut
contrasts_with: []
answers_questions:
  - "How does Hall's theorem extend to non-uniform degree requirements?"
---

# Quick Definition
A bipartite graph contains a subgraph $H$ with $d_H(x_i) = d_i$ and $0 \le d_H(y_j) \le 1$ iff $|\Gamma(S)| \ge \sum_{x_i \in S} d_i$ for every $S \subset V_1$.

# Core Definition
**Corollary 11**: Let $G$ be bipartite with classes $V_1 = \{x_1, \ldots, x_m\}$ and $V_2 = \{y_1, \ldots, y_n\}$. Then $G$ contains a subgraph $H$ with $d_H(x_i) = d_i$ and $0 \le d_H(y_j) \le 1$ iff $|\Gamma(S)| \ge \sum_{x_i \in S} d_i$ for every $S \subset V_1$ (Bollobás, p. 88).

# Prerequisites
- **Hall's theorem** — This extends it to prescribed degrees

# Key Properties
1. Proved by replacing each $x_i$ by $d_i$ copies, each joined to $\Gamma(x_i)$
2. Reduces to Hall's theorem in the expanded graph
3. Models a "polygynous" society where boy $i$ marries $d_i$ girls

# Context & Application
Generalizes Hall's theorem to handle varying capacity at vertices in $V_1$.

# Examples
**Example** (p. 88): Setting all $d_i = 1$ recovers Hall's theorem.

# Relationships
## Builds Upon
- **halls-theorem** — Generalized

# Source Reference
Chapter III, Section III.3, page 88. Corollary 11.

# Verification Notes
- Definition source: Direct from p. 88
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
