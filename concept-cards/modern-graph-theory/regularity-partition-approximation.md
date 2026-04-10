---
concept: Regularity Partition Approximation
slug: regularity-partition-approximation
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
  - "Theorem 32"
prerequisites:
  - szemeredis-regularity-lemma
  - skeleton-graph
extends: []
related:
  - regularity-removal-lemma
contrasts_with: []
answers_questions:
  - "How well does the regularity partition approximate a graph?"
---

# Quick Definition
The number of edges in a graph $G$ and its regularity piece $H$ differ by at most $(\varepsilon + \delta + 1/m + 2M/n)n^2/2$.

# Core Definition
**Theorem 32**: Let $G$ have order $n \ge M$ and let $H = G[k; \varepsilon; d > \delta]$ be an $(m; \varepsilon; d > \delta)$-piece. Then $e(G) - e(H) < (\varepsilon + \delta + 1/m + 2M/n)n^2/2$. In particular, if $\varepsilon \le \delta/2$, $m \ge 4/\delta$, and $n \ge 8M/\delta$, then $e(G) - e(H) < \delta n^2$ (Bollobás, pp. 149-150).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the partition
- **Skeleton graph** — The reduced structure

# Key Properties
1. Edges lost come from four sources: exceptional class, within-class, non-uniform pairs, low-density pairs
2. Each source contributes at most $O(\varepsilon n^2)$ edges
3. With appropriate parameter choices, $e(G) - e(H) < \delta n^2$

# Context & Application
This lemma quantifies how well the regularity piece approximates the original graph. It is the key technical step for all applications of regularity.

# Examples
**Example** (p. 149): The four types of lost edges are: (1) incident with $C_0$: $\le kn$; (2) within classes: $\le k\binom{n/k}{2}$; (3) non-uniform pairs: $\le \varepsilon n^2/2$; (4) low-density: $\le \delta n^2/2$.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — The partition

## Enables
- **regularity-removal-lemma** — Uses this approximation

# Source Reference
Chapter IV, Section IV.6, pages 149-150. Theorem 32.

# Verification Notes
- Definition source: Direct from pp. 149-150
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
