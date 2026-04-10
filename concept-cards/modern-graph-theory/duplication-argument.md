---
concept: Duplication Argument
slug: duplication-argument
category: extremal-graph-theory
subcategory: proof-techniques
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
  - "D(G)"
  - "bipartite double cover"
prerequisites:
  - zarankiewicz-problem
extends: []
related:
  - kovari-sos-turan-bound
contrasts_with: []
answers_questions:
  - "How do you reduce general Zarankiewicz bounds to bipartite ones?"
---

# Quick Definition
Given a graph $G$, construct a bipartite graph $D(G)$ with two copies of $V(G)$ where $x'_i x''_j$ is an edge iff $x_ix_j \in E(G)$. Then $e(D(G)) = 2e(G)$ and $K_{s,t} \not\subset G$ implies $K_{s,t} \not\subset D(G)$.

# Core Definition
Given a graph $G$ with vertex set $\{x_1, \ldots, x_n\}$, construct bipartite graph $H = D(G)$ with copies $V_1 = \{x'_1, \ldots, x'_n\}$ and $V_2 = \{x''_1, \ldots, x''_n\}$, where $x'_ix''_j \in E(H)$ iff $x_ix_j \in E(G)$. Then $e(H) = 2e(G)$, $d_G(x_i) = d_H(x'_i) = d_H(x''_i)$, and $K_{s,t} \not\subset G$ implies $K_{s,t} \not\subset H$, so $z(n,n;s,t) \ge 2ex(n,K_{s,t})$ (Bollobás, p. 124).

# Prerequisites
- **Zarankiewicz problem** — The context for the reduction

# Key Properties
1. Reduces general $ex(n; K_{s,t})$ bounds to bipartite bounds
2. Preserves degree sequences
3. $z(n,n;s,t) \ge 2 \cdot ex(n; K_{s,t})$

# Context & Application
Allows applying bipartite results (Lemma 9) to general graphs without re-proving.

# Examples
**Example** (p. 124): Theorem 11 follows from Lemma 9 applied to $D(G)$.

# Relationships
## Related
- **kovari-sos-turan-bound** — Connected via this argument

# Source Reference
Chapter IV, Section IV.2, page 124.

# Verification Notes
- Definition source: Direct from p. 124
- Confidence rationale: Explicitly described
- Uncertainties: None
- Cross-reference status: Verified
