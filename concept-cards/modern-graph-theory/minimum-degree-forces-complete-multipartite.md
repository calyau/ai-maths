---
concept: Minimum Degree Forces Complete Multipartite Subgraph
slug: minimum-degree-forces-complete-multipartite
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
  - "Theorem 20"
prerequisites:
  - turans-theorem
extends:
  - turans-theorem
related:
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "What complete multipartite subgraphs are forced by large minimum degree?"
---

# Quick Definition
If $\delta(G) \ge (1-1/r+\varepsilon)n$, then $G$ contains $K_{r+1}(t)$ with $t \ge \varepsilon \log n / (2^{r-1}(r-1)!)$.

# Core Definition
**Theorem 20**: Let $r \ge 1$ and $\varepsilon > 0$. If $|G| = n \ge n_0$ and $\delta(G) \ge (1-1/r+\varepsilon)n$, then $G \supset K_{r+1}(t)$ where $t \ge \varepsilon \log n / (2^{r-1}(r-1)!)$ (Bollobás, p. 135).

# Prerequisites
- **Turán's theorem** — The base case; this extends it quantitatively

# Key Properties
1. Proof by induction on $r$; base case $r=1$ uses double counting
2. The logarithmic growth in $t$ is optimal
3. The constant in $t$ depends on $r$ and $\varepsilon$

# Construction / Recognition
1. For $r = 1$: if $G$ has no $K_2(t)$, count $t$-sets covered by vertices
2. For general $r$: find $K_r(T)$ by induction, then find many vertices connected to most of it

# Context & Application
This is the minimum-degree version of the Erdős-Stone theorem; Lemma 21 converts the size version (Theorem 22) to this.

# Examples
**Example** (p. 134): For $r = 1$, $\delta \ge \varepsilon n$ implies $K_2(t)$ with $t = \lceil\varepsilon\log n\rceil$.

# Relationships
## Builds Upon
- **turans-theorem** — Extended quantitatively

## Enables
- **erdos-stone-theorem** — Via Lemma 21

# Source Reference
Chapter IV, Section IV.4, pages 134-136. Theorem 20.

# Verification Notes
- Definition source: Direct from p. 135
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
