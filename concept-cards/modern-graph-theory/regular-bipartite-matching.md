---
concept: Regular Bipartite Graph Has Complete Matching
slug: regular-bipartite-matching
category: matchings
subcategory: structural-results
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases: []
prerequisites:
  - halls-theorem
extends: []
related:
  - complete-matching
contrasts_with: []
answers_questions:
  - "Does a regular bipartite graph have a perfect matching?"
---

# Quick Definition
Every regular bipartite graph satisfies Hall's condition and therefore has a complete matching (and by symmetry, a perfect matching).

# Core Definition
A regular bipartite graph satisfies the conditions of Hall's theorem, so it has a complete matching. This is because if $G$ is $d$-regular with classes $V_1, V_2$, then for any $S \subset V_1$, the edges from $S$ number $d|S|$, and each vertex of $\Gamma(S)$ has degree $d$, so $|\Gamma(S)| \ge |S|$ (Bollobás, p. 87).

# Prerequisites
- **Hall's theorem** — The regular case satisfies Hall's condition automatically

# Key Properties
1. Regular bipartite graph with equal classes has a perfect matching
2. Implies the coset result: group elements forming both left and right coset representatives exist

# Context & Application
A clean application of Hall's theorem; also implies group-theoretic results.

# Examples
**Example** (p. 87): The bipartite graph on left/right cosets of a subgroup $H$ is regular, so an SDR exists.

# Relationships
## Builds Upon
- **halls-theorem** — Condition automatically satisfied

# Source Reference
Chapter III, Section III.3, page 87.

# Verification Notes
- Definition source: Direct from p. 87
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
