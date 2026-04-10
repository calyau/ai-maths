---
concept: Tree Embedding via Regularity
slug: tree-embedding-via-regularity
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
  - "Theorem 36"
  - "Komlós-Sárközy-Szemerédi theorem"
prerequisites:
  - szemeredis-regularity-lemma
extends: []
related:
  - regularity-application-subgraph-finding
contrasts_with: []
answers_questions:
  - "What trees are guaranteed in graphs with minimum degree slightly above n/2?"
---

# Quick Definition
For every $\varepsilon > 0$ and $\Delta \ge 1$, every graph of order $n$ with $\delta(G) \ge (1+\varepsilon)n/2$ contains every tree of order $n$ and maximum degree at most $\Delta$ (for $n$ large enough).

# Core Definition
**Theorem 36** (Komlós-Sárközy-Szemerédi, 1993): For every $\varepsilon > 0$ and $\Delta \ge 1$ there is $n_0$ such that every graph of order $n \ge n_0$ and minimal degree at least $(1+\varepsilon)n/2$ contains every tree of order $n$ and maximal degree at most $\Delta$ (Bollobás, p. 153).

# Prerequisites
- **Szemerédi's regularity lemma** — The key tool

# Key Properties
1. Conjectured by Bollobás in 1978, proved in 1993
2. The minimum degree bound $(1+\varepsilon)n/2$ is slightly above Dirac's $n/2$ threshold
3. The result extends to maximum degree $cn$ for small enough $c$
4. Related to the Erdős-Sós conjecture: every graph with $e(G) > (k-1)n/2$ contains every tree with $k$ edges

# Context & Application
One of the "great number of substantial applications of Szemerédi's regularity lemma" (p. 153).

# Examples
**Example** (p. 153): For $\Delta = 2$ (paths), the result is weaker than what's known. The power is for bounded-degree trees of nearly full order.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — The key proof tool

# Source Reference
Chapter IV, Section IV.6, page 153. Theorem 36.

# Verification Notes
- Definition source: Direct from p. 153
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
