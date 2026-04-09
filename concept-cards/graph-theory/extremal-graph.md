---
concept: Extremal Graph
slug: extremal-graph
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 175
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "extremal for n and H"
prerequisites:
  - extremal-number
  - graph
related:
  - turan-theorem
  - turan-graph
contrasts_with: []
answers_questions:
  - "What is an extremal graph?"
---

# Quick Definition
A graph G not containing H on n vertices with the largest possible number of edges (i.e., ex(n, H) edges) is called extremal for n and H.

# Core Definition
A graph G not containing H (G not superset H) on n vertices with ex(n, H) edges is called **extremal** for n and H. An extremal graph is edge-maximal with H not subset G. The converse is false: a graph may be edge-maximal without H yet have fewer than ex(n, H) edges. (Diestel, p. 164-165)

# Prerequisites
- **Extremal number** — ex(n, H) defines what "extremal" means
- **Graph** — Extremal graphs are graphs with specific properties

# Key Properties
1. Has exactly ex(n, H) edges
2. Is edge-maximal without H (but converse is false)
3. May not be unique (though for K^r it is: the Turan graph)
4. For K^r: the unique extremal graph is T^{r-1}(n)

# Examples
**Example** (p. 165, Fig. 7.1.1): Two graphs edge-maximal without P^3; only one is extremal.

# Relationships
## Related
- **Turan's theorem** — T^{r-1}(n) is the unique extremal graph for K^r

# Source Reference
Chapter 7, Section 7.1, pages 164-165 (pdf page 175).

# Verification Notes
- Confidence: HIGH — explicitly defined
