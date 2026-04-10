---
concept: Regularity Piece
slug: regularity-piece
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
  - "G[k; ε; d > δ]"
  - "(m; ε; d > δ)-piece"
prerequisites:
  - szemeredis-regularity-lemma
  - epsilon-uniform-pair
extends: []
related:
  - skeleton-graph
  - regularity-partition-approximation
contrasts_with: []
answers_questions:
  - "What is a regularity piece of a graph?"
---

# Quick Definition
The regularity piece $G[k; \varepsilon; d > \delta]$ is the union of bipartite subgraphs between $\varepsilon$-regular pairs of density $> \delta$ in a Szemerédi partition.

# Core Definition
Given a Szemerédi partition of $G$, let $G[k; \varepsilon; d > \delta]$ be the union of the bipartite subgraphs spanned by $(C_i, C_j)$ for the $\varepsilon$-regular pairs of density greater than $\delta$. This is called an $(m; \varepsilon; d > \delta)$-piece of $G$. The vertex set is $\bigcup_{i=1}^k C_i$ (Bollobás, p. 148).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the partition
- **ε-uniform pair** — Determines which pairs are included

# Key Properties
1. Vertex set is $\bigcup C_i$, excluding the exceptional class
2. Only includes edges in regular, dense pairs
3. $e(G) - e(H) < (\varepsilon + \delta + 1/m + 2M/n)n^2/2$ (Theorem 32)
4. The skeleton $S[k; \varepsilon; d > \delta]$ captures the pair structure

# Context & Application
The regularity piece is the "cleaned" version of the graph used in applications of the regularity lemma.

# Examples
**Example** (p. 148): Four types of edges are excluded: those incident with $C_0$, within classes, in non-regular pairs, and in regular pairs with density $\le \delta$.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — Provides the partition

## Enables
- **skeleton-graph** — Captures the pair structure
- **regularity-partition-approximation** — Bounds the error

# Source Reference
Chapter IV, Section IV.6, page 148.

# Verification Notes
- Definition source: Direct from p. 148
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
