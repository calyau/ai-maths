---
concept: Asymptotic Extremal Density
slug: asymptotic-extremal-density
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 178
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "Corollary 7.1.3"
  - "critical density"
prerequisites:
  - erdos-stone-theorem
  - extremal-number
related:
  - turan-theorem
  - proportional-edge-density
answers_questions:
  - "What is the asymptotic extremal density for a graph H?"
---

# Quick Definition
For every graph H with at least one edge, lim_{n->infinity} ex(n,H)/C(n,2) = (chi(H)-2)/(chi(H)-1). The asymptotic extremal density is determined by the chromatic number alone.

# Core Definition
**Corollary 7.1.3**: For every graph H with at least one edge,

lim_{n->infinity} ex(n, H) / C(n, 2) = (chi(H) - 2) / (chi(H) - 1).

The proof sandwiches ex(n,H) between t_{r-1}(n) (lower bound, from H not subset T^{r-1}(n)) and t_{r-1}(n) + epsilon*n^2 (upper bound, from Erdos-Stone). Then Lemma 7.1.4 gives convergence. (Diestel, pp. 167-168)

# Prerequisites
- **Erdos-Stone theorem** — The corollary follows from it
- **Extremal number** — The quantity whose limit is determined

# Key Properties
1. The limiting density depends ONLY on chi(H)
2. For bipartite H (chi = 2): density -> 0 (ex(n,H) = o(n^2))
3. For H with chi = 3: density -> 1/2
4. For H with chi = r: density -> (r-2)/(r-1)
5. The corollary "established the theorem as a meta-theorem for dense extremal graph theory"

# Relationships
## Builds Upon
- **Erdos-Stone theorem**

# Source Reference
Chapter 7, Section 7.1, Corollary 7.1.3, pages 167-168 (pdf pages 177-178).

# Verification Notes
- Confidence: HIGH — corollary with proof
