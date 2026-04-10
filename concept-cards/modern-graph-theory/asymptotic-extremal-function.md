---
concept: Asymptotic Extremal Function
slug: asymptotic-extremal-function
category: extremal-graph-theory
subcategory: fundamental-theorems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "Corollary 23"
  - "Corollary 24"
prerequisites:
  - erdos-stone-theorem
  - turans-theorem
extends:
  - erdos-stone-theorem
related:
  - forbidden-subgraph-problem
contrasts_with: []
answers_questions:
  - "What is the asymptotic value of ex(n; F) for non-bipartite F?"
---

# Quick Definition
For any non-bipartite graph $F$ with $\chi(F) = r+1$: $ex(n; F) = (1 - 1/r)\binom{n}{2} + o(n^2)$.

# Core Definition
**Corollary 24**: Let $F_1, \ldots, F_t$ be non-empty graphs and let $r+1$ be the minimum chromatic number. Then $ex(n; F_1, \ldots, F_t) = (1-1/r)\binom{n}{2} + o(n^2)$ (Bollobás, p. 137).

**Corollary 23**: For $F = K_{r+1}(t)$: $ex(n; F) = (1-1/r)\binom{n}{2} + o(n^2)$ (p. 137).

# Prerequisites
- **Erdős-Stone theorem** — The primary tool
- **Turán's theorem** — Provides the lower bound

# Key Properties
1. The asymptotic extremal function depends only on $\chi(F)$
2. The leading term is $(1-1/r)/2$ times $n^2$
3. For bipartite $F$: $ex(n;F) = o(n^2)$ (the theorem gives no useful information)

# Context & Application
This completely solves the forbidden subgraph problem asymptotically for non-bipartite forbidden graphs.

# Examples
**Example** (p. 137): The lower bound comes from $T_r(n)$ (no $K_{r+1}$, hence no $F$); the upper bound from Erdős-Stone.

# Relationships
## Builds Upon
- **erdos-stone-theorem** — Implies the asymptotic formula

# Source Reference
Chapter IV, Section IV.4, page 137. Corollaries 23-24.

# Verification Notes
- Definition source: Direct from p. 137
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
