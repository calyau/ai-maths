---
concept: Skeleton of a Regularity Partition
slug: skeleton-graph
category: regularity-method
subcategory: definitions
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.6 Simple Applications of Szemerédi's Lemma"
extraction_confidence: high
aliases:
  - "S[k; ε; d > δ]"
  - "reduced graph"
prerequisites:
  - szemeredis-regularity-lemma
  - epsilon-uniform-pair
extends: []
related:
  - regularity-removal-lemma
  - regularity-application-subgraph-finding
contrasts_with: []
answers_questions:
  - "What is the skeleton of a regularity partition?"
---

# Quick Definition
The skeleton $S[k; \varepsilon; d > \delta]$ is a graph on $[k]$ where $ij$ is an edge iff $(C_i, C_j)$ is $\varepsilon$-uniform with density $> \delta$.

# Core Definition
Given an $(m; \varepsilon; d > \delta)$-piece $G[k; \varepsilon; d > \delta]$ of a graph $G$, the skeleton $S[k; \varepsilon; d > \delta]$ is the graph on $[k]$ in which $ij$ is an edge if and only if $(C_i, C_j)$ is $\varepsilon$-uniform with density more than $\delta$ (Bollobás, p. 148).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the partition
- **ε-uniform pair** — Determines which pairs form skeleton edges

# Key Properties
1. The skeleton captures the "dense regular" structure of the partition
2. If $G$ has no $K_r$, the skeleton has no $K_r$ (by Theorem 30)
3. Turán's theorem applies to the skeleton to bound its edges

# Construction / Recognition
1. Apply Szemerédi's lemma to get partition $(C_i)_{i=0}^k$
2. For each pair $(C_i, C_j)$: check $\varepsilon$-uniformity and density $> \delta$
3. Add edge $ij$ to skeleton if both conditions hold

# Context & Application
The skeleton is the "coarsened" view of the graph: it captures which parts of the graph are densely and regularly connected. Analyzing the skeleton with classical tools (Turán, etc.) gives results about the original graph.

# Examples
**Example** (p. 150): If $G$ has no $F$ with $\chi(F) = r$, the skeleton has no $K_r$, so by Turán, $e(S) \le (r-2)k^2/(2(r-1))$.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — Provides the partition

## Enables
- **regularity-removal-lemma** — Skeleton analysis
- **frankl-pach-theorem** — Uses skeleton structure

# Source Reference
Chapter IV, Section IV.6, page 148.

# Verification Notes
- Definition source: Direct from p. 148
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
