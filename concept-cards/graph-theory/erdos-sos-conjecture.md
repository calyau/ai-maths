---
concept: "Erd\u0151s-S\u00F3s Conjecture"
slug: erdos-sos-conjecture
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 179
section: "7.1 Subgraphs"
extraction_confidence: medium
aliases: []
prerequisites:
  - extremal-number
related:
  - turan-theorem
answers_questions:
  - "What is the conjectured extremal number for trees?"
---

# Quick Definition
The Erdos-Sos conjecture (1963) asserts that ex(n, T) <= (1/2)(k-1)n for all trees T with k >= 2 edges; as a general bound for all n, this is best possible for every T.

# Core Definition
Erdos and Sos conjectured in 1963 that ex(n, T) <= (1/2)(k-1)n for all trees with k >= 2 edges. If H is a forest, then H subset G as soon as epsilon(G) is large enough, so ex(n, H) is at most linear in n. The conjecture is verified for stars (trivial) and paths (Erdos-Gallai 1959). (Diestel, p. 169)

# Prerequisites
- **Extremal number** — The conjecture bounds ex(n, T)

# Key Properties
1. Linear bound on ex(n, T) for all trees
2. Best possible for each T as a general bound over all n
3. Verified for special cases: stars, paths, approximately for large k

# Source Reference
Chapter 7, Section 7.1, page 169 (pdf page 179).

# Verification Notes
- Confidence: MEDIUM — conjecture mentioned without proof
