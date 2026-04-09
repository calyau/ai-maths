---
concept: Bipartite Extremal Numbers
slug: bipartite-extremal-number
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
extraction_confidence: high
aliases:
  - "Zarankiewicz problem"
prerequisites:
  - extremal-number
  - asymptotic-extremal-density
related:
  - kovari-sos-turan-theorem
  - erdos-stone-theorem
answers_questions:
  - "What is the extremal number for bipartite graphs?"
---

# Quick Definition
For bipartite H, Corollary 7.1.3 gives lim ex(n,H)/C(n,2) = 0, meaning ex(n,H) = o(n^2). For complete bipartite K_{r,r}, the bounds are c_1*n^{2-2/(r+1)} <= ex(n, K_{r,r}) <= c_2*n^{2-1/r}.

# Core Definition
For bipartite graphs H (chi(H) = 2), the asymptotic extremal density is 0 by Corollary 7.1.3. This means ex(n,H) grows subquadratically. The Zarankiewicz problem asks for the exact growth rate. For H = K_{r,r}: the lower bound c_1*n^{2-2/(r+1)} comes from random graphs, and the upper bound c_2*n^{2-1/r} from a counting argument (Exercise 11). For forests, ex(n,H) is at most linear in n. (Diestel, p. 169)

# Prerequisites
- **Extremal number** — ex(n,H) for bipartite H
- **Asymptotic extremal density** — The limit is 0 for bipartite H

# Key Properties
1. ex(n,H) = o(n^2) for all bipartite H
2. For K_{r,r}: subquadratic but super-linear
3. The exact exponent is not known for most r
4. For forests: ex(n,T) is O(n)

# Source Reference
Chapter 7, Section 7.1, page 169 (pdf page 179).

# Verification Notes
- Confidence: HIGH — bounds explicitly stated
