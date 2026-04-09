---
concept: "K\u0151v\u00E1ri-S\u00F3s-Tur\u00E1n Theorem"
slug: kovari-sos-turan-theorem
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
aliases:
  - "Kovari-Sos-Turan theorem"
  - "Zarankiewicz problem upper bound"
prerequisites:
  - extremal-number
related:
  - turan-theorem
  - erdos-stone-theorem
answers_questions:
  - "What is the extremal number for complete bipartite graphs?"
---

# Quick Definition
The extremal number for K_{r,r} satisfies ex(n, K_{r,r}) <= c*n^{2-1/r} for a constant c depending on r, providing an upper bound for the Zarankiewicz problem.

# Core Definition
For suitable constants c_1, c_2 depending on r:
c_1 * n^{2 - 2/(r+1)} <= ex(n, K_{r,r}) <= c_2 * n^{2-1/r}.

The lower bound comes from random graphs; the upper bound is proved in Exercise 11 via a counting argument on the degrees in a bipartite graph. (Diestel, p. 169)

# Prerequisites
- **Extremal number** — The theorem bounds ex(n, K_{r,r})

# Key Properties
1. For bipartite H, ex(n, H) is subquadratic (o(n^2))
2. The exact growth rate of ex(n, K_{r,r}) remains open for most r
3. The upper bound n^{2-1/r} is believed to give the correct order of magnitude

# Relationships
## Builds Upon
- **Extremal number**

## Related
- **Turan's theorem** — The complete graph analogue
- **Erdos-Stone theorem** — Gives 0 as the limiting density for bipartite H

# Source Reference
Chapter 7, Section 7.1, page 169 (pdf page 179). Exercise 11.

# Verification Notes
- The bound is stated in the text but the proof is left to Exercise 11
- Confidence: MEDIUM — bounds stated without proof in main text
