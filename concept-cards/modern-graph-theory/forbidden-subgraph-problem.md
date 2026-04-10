---
concept: Forbidden Subgraph Problem
slug: forbidden-subgraph-problem
category: extremal-graph-theory
subcategory: fundamental-problems
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV Extremal Problems"
extraction_confidence: high
aliases:
  - "Turán-type problem"
prerequisites:
  - extremal-function
extends: []
related:
  - turans-theorem
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "What is the forbidden subgraph problem?"
---

# Quick Definition
Given a graph $F$, the forbidden subgraph problem asks to determine $ex(n; F)$, the maximum edges in an $F$-free graph of order $n$, and to characterize the extremal graphs $EX(n; F)$.

# Core Definition
The quintessential extremal problem: given a graph $F$, determine $ex(n; F)$, the maximal number of edges in a graph of order $n$ not containing $F$. Equivalently, how many edges guarantee that a graph contains $F$? (Bollobás, p. 110).

# Prerequisites
- **Extremal function** — The function being determined

# Key Properties
1. Solved exactly for $F = K_{r+1}$ by Turán's theorem
2. Solved asymptotically for non-bipartite $F$ by Erdős-Stone
3. For bipartite $F$: $ex(n;F) = o(n^2)$ but exact orders often unknown
4. Can forbid multiple graphs: $ex(n; F_1, \ldots, F_k)$

# Context & Application
"Extremal problems are at the very heart of graph theory... the forbidden subgraph problem" is the central question (p. 110).

# Examples
**Example** (p. 110): $ex(n; K_3) = \lfloor n^2/4 \rfloor$ (Mantel); $ex(n; P_\ell) = (l-2)n/2$ (Theorem 3).

# Relationships
## Enables
- **turans-theorem** — Solves for $K_{r+1}$
- **erdos-stone-theorem** — Solves asymptotically

# Source Reference
Chapter IV, introductory section, page 110.

# Verification Notes
- Definition source: Direct from p. 110
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
