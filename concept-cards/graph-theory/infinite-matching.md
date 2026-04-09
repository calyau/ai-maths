---
concept: Infinite Matching Theory
slug: infinite-matching
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 232
section: "8.4 Connectivity and matching"
extraction_confidence: medium
aliases: []
prerequisites:
  - infinite-graph
  - matching
  - infinite-mengers-theorem
extends:
  - matching
related: []
contrasts_with: []
answers_questions:
  - "How do matching theorems extend to infinite graphs?"
---

# Quick Definition
Infinite matching theory extends König's, Hall's, and Tutte's theorems to infinite graphs using Erdős-Menger-type reformulations that replace cardinality comparisons with "matchability" conditions.

# Core Definition
The key insight is that in infinite graphs, comparing cardinalities is insufficient. Instead, the marriage condition is reformulated: S obstructs a matching of A if S is not matchable to N(S) but N(S) is matchable to S (Corollary 8.4.9). Similarly, Tutte's condition is reformulated using matchability of factor-critical components (Theorem 8.4.11) (Diestel, pp. 232-236).

# Prerequisites
- **Infinite graph** — The setting
- **Matching** — The finite theory being extended
- **Infinite Menger's theorem** — The foundation for infinite matching

# Key Properties
1. Infinite König's theorem (8.4.8): every bipartite graph has a matching and vertex cover where the cover consists of one vertex from each matching edge
2. Infinite Hall's theorem (Corollary 8.4.9): reformulated using matchability
3. Infinite Tutte's theorem (8.4.11): 1-factor iff factor-critical components are matchable to S for every S
4. Steffens' theorem (8.4.10): countable graph has 1-factor iff every partial matching has augmenting path

# Relationships
## Builds Upon
- **Matching** — The finite theory
- **Infinite Menger's theorem** — The foundation

# Source Reference
Chapter 8, Section 8.4, pages 232-236.

# Verification Notes
- Synthesized from multiple theorems in Section 8.4
- Confidence: MEDIUM — synthesis across multiple results
