---
concept: Degree Domination Theorem
slug: degree-domination-theorem
category: extremal-graph-theory
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "Theorem 7"
  - "Erdős 1970"
prerequisites:
  - turans-theorem
extends: []
related:
  - turan-graph
contrasts_with: []
answers_questions:
  - "How does the degree sequence relate to r-partiteness?"
---

# Quick Definition
If a graph $G$ does not contain $K_{r+1}$, then there is an $r$-partite graph $H$ on the same vertex set with $d_G(z) \le d_H(z)$ for every vertex $z$.

# Core Definition
**Theorem 7** (Erdős, 1970): Let $G$ be a graph with vertex set $V$ not containing $K_{r+1}$. Then there is an $r$-partite graph $H$ with vertex set $V$ such that $d_G(z) \le d_H(z)$ for every $z \in V$. If $G$ is not a complete $r$-partite graph, strict inequality holds for at least one vertex (Bollobás, pp. 118-119).

# Prerequisites
- **Turán's theorem** — This provides an alternative proof

# Key Properties
1. Degree sequence of $K_{r+1}$-free graph is dominated by an $r$-partite graph
2. Implies Turán's theorem immediately
3. Proof by induction on $r$

# Construction / Recognition
1. Pick max-degree vertex $x$, let $W = \Gamma(x)$
2. $G[W]$ is $K_r$-free; replace by $(r-1)$-partite graph by induction
3. Join all non-neighbours of $x$ to all of $W$

# Context & Application
Provides a structure theorem: every $K_{r+1}$-free graph is "dominated" by an $r$-partite graph.

# Examples
**Example** (pp. 118-119): The inductive construction builds $H$ from the ground up, replacing the neighbourhood of the highest-degree vertex.

# Relationships
## Builds Upon
- **turans-theorem** — Provides alternative proof

# Source Reference
Chapter IV, Section IV.2, pages 118-119. Theorem 7.

# Verification Notes
- Definition source: Direct from pp. 118-119
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
