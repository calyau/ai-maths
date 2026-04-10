---
concept: Double Counting Argument
slug: double-counting
category: extremal-graph-theory
subcategory: proof-techniques
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: medium
aliases:
  - "double counting"
  - "counting in two ways"
prerequisites: []
extends: []
related:
  - kovari-sos-turan-bound
  - zarankiewicz-problem
contrasts_with: []
answers_questions:
  - "What is the double counting argument in extremal graph theory?"
---

# Quick Definition
The double counting argument counts the edges of an auxiliary bipartite graph from both sides, then applies convexity to obtain bounds on the original graph.

# Core Definition
The double counting argument counts a quantity in two different ways to derive an inequality. In the proof of Lemma 9, construct a bipartite graph $H$ with $V_1$ on one side and $t$-subsets of $V_2$ on the other. Count $e(H)$ from the $V_1$ side as $\sum \binom{d(x)}{t}$ and from the $V_2$ side as at most $(s-1)\binom{n}{t}$. This is "perhaps the most basic combinatorial argument" (Bollobás, p. 122).

# Prerequisites
This is a foundational proof technique with no prerequisites.

# Key Properties
1. Creates auxiliary bipartite graph connecting vertices to $t$-subsets
2. Left side: sum of $\binom{d(x)}{t}$ over vertices
3. Right side: at most $(s-1)\binom{n}{t}$ by the $K_{s,t}$-free condition
4. Convexity of $\binom{u}{t}$ gives the optimal bound

# Context & Application
Fundamental technique in extremal combinatorics. Used for the Kővári-Sós-Turán bound, Zarankiewicz bounds, and many other results.

# Examples
**Example** (p. 122): In Lemma 9, each $t$-set of $V_2$ is covered by at most $s-1$ vertices, giving $\sum \binom{d(x)}{t} \le (s-1)\binom{n}{t}$.

# Relationships
## Enables
- **kovari-sos-turan-bound** — Key proof technique
- **zarankiewicz-problem** — Bounds obtained via double counting

# Source Reference
Chapter IV, Section IV.2, pages 122-123.

# Verification Notes
- Definition source: Synthesized from p. 122
- Confidence rationale: Described as fundamental technique but not formally defined
- Uncertainties: None
- Cross-reference status: Verified
