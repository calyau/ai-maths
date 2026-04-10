---
concept: "Hall's Theorem"
slug: halls-theorem
category: matchings
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Hall's marriage theorem"
  - "marriage theorem"
  - "Theorem 7"
  - "König-Egerváry theorem"
prerequisites:
  - matching
  - complete-matching
  - mengers-theorem
extends: []
related:
  - system-of-distinct-representatives
  - max-flow-min-cut-theorem
  - deficiency-version-halls-theorem
contrasts_with: []
answers_questions:
  - "How do I find a maximum matching in a bipartite graph?"
  - "What is a perfect matching?"
---

# Quick Definition
A bipartite graph with vertex classes $V_1$ and $V_2$ has a complete matching from $V_1$ to $V_2$ if and only if $|\Gamma(S)| \ge |S|$ for every $S \subset V_1$.

# Core Definition
**Theorem 7** (Hall, 1935; König-Egerváry, 1931): A bipartite graph $G$ with vertex sets $V_1$ and $V_2$ contains a complete matching from $V_1$ to $V_2$ iff $|\Gamma(S)| \ge |S|$ for every $S \subset V_1$. The necessity is obvious (if $k$ girls know at most $k-1$ boys, they cannot all marry). The sufficiency is the deep part (Bollobás, pp. 85-86).

# Prerequisites
- **Matching** — The objects whose existence is characterized
- **Complete matching** — The type of matching sought
- **Menger's theorem** — One proof uses Menger's theorem

# Key Properties
1. The condition $|\Gamma(S)| \ge |S|$ for all $S \subset V_1$ is called Hall's condition
2. Three proofs are given: via Menger/max-flow, by induction (Halmos-Vaughn), and by minimality (Rado)
3. A regular bipartite graph always satisfies Hall's condition
4. Implies the SDR theorem (Theorem 8)

# Construction / Recognition
## To Check Hall's Condition
1. For every subset $S \subset V_1$, compute $|\Gamma(S)|$
2. Verify $|\Gamma(S)| \ge |S|$
3. If the condition holds, a complete matching exists

## To Find a Complete Matching (via augmenting paths)
1. Start with any matching $M$
2. Find an $M$-augmenting path and augment
3. Repeat until no augmenting path exists

# Context & Application
Hall's theorem is "a prime example of several results... giving necessary and sufficient conditions for the existence of certain objects; in each case the beauty of the theorem is that a condition whose necessity is obvious is shown to be also sufficient" (p. 74). It answers the marriage problem and the SDR problem.

# Examples
**Example** (p. 85): If $k$ girls know at most $k-1$ boys altogether, then not all girls can marry. The theorem states this is the *only* obstruction.

**Example** (p. 87): A regular bipartite graph satisfies Hall's condition, so it has a complete matching. This implies the group coset result.

# Relationships
## Builds Upon
- **matching** and **complete-matching** — The objects involved
- **mengers-theorem** — One proof derives from Menger

## Enables
- **deficiency-version-halls-theorem** — Corollary 9
- **konigs-theorem** — Corollary 10
- **tuttes-1-factor-theorem** — Hall used in the proof

## Related
- **max-flow-min-cut-theorem** — Alternative proof source

# Common Errors
- **Error**: Only checking Hall's condition for small subsets
  **Correction**: The condition must hold for *every* $S \subset V_1$, including $V_1$ itself

# Common Confusions
- **Confusion**: Thinking Hall's theorem only applies to complete bipartite graphs
  **Clarification**: It applies to any bipartite graph; the graph need not be regular or complete

# Source Reference
Chapter III, Section III.3, pages 85-88. Theorem 7 with three proofs.

# Verification Notes
- Definition source: Direct theorem statement from p. 85
- Confidence rationale: Major theorem with three complete proofs
- Uncertainties: None
- Cross-reference status: Verified
