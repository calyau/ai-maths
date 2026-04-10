---
concept: Regularity Application for Subgraph Finding
slug: regularity-application-subgraph-finding
category: regularity-method
subcategory: applications
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
  - "Theorem 30"
  - "embedding lemma"
prerequisites:
  - szemeredis-regularity-lemma
  - epsilon-uniform-pair
extends: []
related:
  - regularity-removal-lemma
contrasts_with: []
answers_questions:
  - "How do I apply Szemerédi's regularity lemma?"
---

# Quick Definition
If $r$ disjoint vertex sets are pairwise $\varepsilon$-uniform with positive density, then every $r$-partite graph on $f$ vertices can be found as a subgraph (when the sets are large enough).

# Core Definition
**Theorem 30**: Let $f \ge 2$, $r \ge 2$, $0 < \delta < 1/r$, and let $V_1, \ldots, V_r$ be disjoint sets with $|V_i| \ge \delta^{-f}$. If for $1 \le i < j \le r$, all large subsets $W_i \subset V_i$, $W_j \subset V_j$ with $|W_i| \ge \delta^f|V_i|$ satisfy $d(W_i, W_j) \ge \delta$, then for all non-negative $f_1, \ldots, f_r$ with $\sum f_i = f$, there exist $U_i \subset V_i$ with $|U_i| = f_i$ forming a complete $r$-partite subgraph. In particular, $G$ contains every $r$-partite graph on $f$ vertices (Bollobás, p. 147).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the uniform pairs
- **ε-uniform pair** — The density condition

# Key Properties
1. Works by induction on $f$
2. Requires sets large enough: $|V_i| \ge \delta^{-f}$
3. Finds any $r$-partite graph on $f$ vertices as a subgraph
4. The density $\delta$ must be positive

# Construction / Recognition
1. Pick vertex $x \in V_1$ with at least $\delta|V_i|$ neighbours in each $V_i$
2. Restrict to neighbourhoods: $V_i' = V_i \cap \Gamma(x)$
3. Apply induction with $f - 1$ vertices

# Context & Application
This is the standard way to use regularity to find small subgraphs. Combined with a Szemerédi partition, it finds all small $r$-partite subgraphs.

# Examples
**Example** (p. 147-148): The proof removes vertices with few neighbours in some $V_i$; at most $(r-1)\delta^f|V_1|$ such vertices exist.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — Provides the partition

## Enables
- **regularity-removal-lemma** — Uses subgraph finding

# Source Reference
Chapter IV, Section IV.6, pages 147-148. Theorem 30.

# Verification Notes
- Definition source: Direct theorem statement from p. 147
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
