---
concept: Proportional Edge Density
slug: proportional-edge-density
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 173
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "edge density (proportion)"
  - "dense graph"
  - "sparse graph"
prerequisites:
  - graph
  - edge
  - edge-density
related:
  - extremal-number
  - turan-theorem
  - erdos-stone-theorem
  - density-of-pair
contrasts_with:
  - edge-density
answers_questions:
  - "What makes a graph dense or sparse?"
  - "What is the proportional edge density?"
---

# Quick Definition
The proportional edge density of a graph G is ||G|| / C(|G|, 2), the proportion of potential edges actually present. Graphs with about n^2 edges are dense; those with about n edges are sparse.

# Core Definition
The number ||G|| / C(|G|, 2), the proportion of its potential edges that G actually has, is the **edge density** of G (in the proportional sense). Graphs with a number of edges about quadratic in their number of vertices are called **dense**; those with a linear number are called **sparse**. (Diestel, p. 163)

Note: This is distinct from epsilon(G) = ||G||/|G| (the ratio of edges to vertices from Chapter 1).

# Prerequisites
- **Graph**, **Edge** — Basic graph concepts
- **Edge density** — The simpler ratio epsilon(G) = ||G||/|G| from Ch 1

# Key Properties
1. Values between 0 and 1
2. Dense graphs: density bounded away from 0 as n grows
3. Sparse graphs: density tends to 0
4. The critical density for forcing H as a subgraph is (chi(H)-2)/(chi(H)-1) (Corollary 7.1.3)
5. Complete bipartite graphs can have density 1/4 without containing any odd cycle

# Context & Application
The distinction between dense and sparse extremal graph theory is fundamental. Section 7.1 (subgraphs) deals with dense problems where quadratic edge counts are needed. Section 7.2 (minors) deals with sparse problems where linear edge counts suffice.

# Relationships
## Related
- **Extremal number** — ex(n,H)/C(n,2) is the critical proportional density
- **Density of pair** — Local density concept used in the regularity lemma

## Contrasts With
- **Edge density** — epsilon(G) = ||G||/|G| is a different (non-normalized) density

# Source Reference
Chapter 7, introduction, page 163 (pdf page 173).

# Verification Notes
- Confidence: HIGH — explicitly defined in the chapter introduction
