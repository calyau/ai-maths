---
concept: Complete Matching
slug: complete-matching
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
  - "complete matching from V₁ to V₂"
prerequisites:
  - matching
extends:
  - matching
related:
  - halls-theorem
  - system-of-distinct-representatives
contrasts_with:
  - perfect-matching
  - maximum-matching
answers_questions:
  - "How do I find a maximum matching in a bipartite graph?"
---

# Quick Definition
A complete matching from $V_1$ to $V_2$ in a bipartite graph is a matching of $|V_1|$ independent edges, each incident with exactly one vertex of $V_1$.

# Core Definition
In a bipartite graph with vertex classes $V_1$ and $V_2$, a complete matching from $V_1$ to $V_2$ is a set of $|V_1|$ independent edges such that each vertex in $V_1$ is incident with exactly one of these edges. This corresponds to a system of distinct representatives: each vertex in $V_1$ is "matched" to a distinct vertex in $V_2$ (Bollobás, p. 85).

# Prerequisites
- **Matching** — A complete matching is a special matching

# Key Properties
1. Covers every vertex in $V_1$
2. Requires $|V_1| \le |V_2|$
3. Exists iff Hall's condition holds: $|\Gamma(S)| \ge |S|$ for every $S \subset V_1$
4. If $|V_1| = |V_2|$, a complete matching from $V_1$ to $V_2$ is a perfect matching

# Construction / Recognition
1. Check Hall's condition: for every $S \subset V_1$, verify $|\Gamma(S)| \ge |S|$
2. If satisfied, a complete matching exists (by Hall's theorem)
3. Can be found using augmenting path methods or max-flow

# Context & Application
Complete matchings solve the assignment problem: assigning each element of one set to a distinct element of another. The marriage problem formulation asks when all girls can find husbands.

# Examples
**Example** (p. 85): Given $m$ girls and $n$ boys, a complete matching from the girls to the boys means every girl is married to a boy she knows.

# Relationships
## Builds Upon
- **matching** — Complete matching is a specialized matching

## Enables
- **halls-theorem** — Characterizes when complete matchings exist

## Contrasts With
- **perfect-matching** — A complete matching need not cover $V_2$
- **maximum-matching** — A maximum matching may not be complete

# Common Errors
- **Error**: Thinking a complete matching must cover both vertex classes
  **Correction**: A complete matching from $V_1$ to $V_2$ covers all of $V_1$ but may leave vertices of $V_2$ uncovered

# Common Confusions
- **Confusion**: Confusing "complete matching" with "perfect matching"
  **Clarification**: A complete matching covers one class; a perfect matching covers both

# Source Reference
Chapter III, Section III.3, page 85.

# Verification Notes
- Definition source: Direct from p. 85
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
