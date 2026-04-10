---
concept: "Hall's Condition"
slug: halls-condition
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "marriage condition"
  - "|Γ(S)| ≥ |S|"
prerequisites:
  - matching
extends: []
related:
  - halls-theorem
  - complete-matching
contrasts_with: []
answers_questions:
  - "What is Hall's condition for a complete matching?"
---

# Quick Definition
Hall's condition for a bipartite graph with classes $V_1, V_2$ states: $|\Gamma(S)| \ge |S|$ for every $S \subset V_1$.

# Core Definition
In a bipartite graph with vertex classes $V_1$ and $V_2$, Hall's condition requires $|\Gamma(S)| \ge |S|$ for every $S \subset V_1$. This is necessary and sufficient for a complete matching from $V_1$ to $V_2$ (Theorem 7). The necessity is obvious: if $k$ girls know at most $k-1$ boys, not all can marry (Bollobás, p. 85).

# Prerequisites
- **Matching** — Hall's condition characterizes matching existence

# Key Properties
1. Must hold for every subset $S \subset V_1$, including singletons and $V_1$ itself
2. Automatically satisfied for regular bipartite graphs
3. Checking all $2^{|V_1|}$ subsets is generally required

# Construction / Recognition
1. For each $S \subset V_1$, compute $\Gamma(S) = \bigcup_{v \in S} \Gamma(v) \cap V_2$
2. Check $|\Gamma(S)| \ge |S|$

# Context & Application
Hall's condition is "a particularly simple and pleasant necessary and sufficient condition" for complete matchings in bipartite graphs (p. 85).

# Examples
**Example** (p. 85): If any $k$ girls collectively know fewer than $k$ boys, Hall's condition fails and no complete matching exists.

# Relationships
## Enables
- **halls-theorem** — Hall's condition is the theorem's condition

## Related
- **complete-matching** — What the condition guarantees

# Source Reference
Chapter III, Section III.3, pages 85-86.

# Verification Notes
- Definition source: Direct from pp. 85-86
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
