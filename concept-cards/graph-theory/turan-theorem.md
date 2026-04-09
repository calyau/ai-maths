---
concept: "Tur\u00E1n's Theorem"
slug: turan-theorem
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
  - "Turan's theorem"
  - "Theorem 7.1.1"
prerequisites:
  - extremal-number
  - turan-graph
related:
  - erdos-stone-theorem
  - edge-density
  - vertex-duplication
answers_questions:
  - "How does edge density relate to the existence of subgraphs (Turan's theorem)?"
  - "What is the maximum number of edges in a K^r-free graph?"
---

# Quick Definition
Turan's theorem states that for all r > 1, every K^r-free graph with n vertices and ex(n, K^r) edges is the Turan graph T^{r-1}(n); in particular, ex(n, K^r) = t_{r-1}(n).

# Core Definition
**Theorem 7.1.1** (Turan 1941): For all integers r, n with r > 1, every graph G not containing K^r with n vertices and ex(n, K^r) edges is a T^{r-1}(n).

Two proofs are given:
- **First proof** (induction on n): Uses a K^{r-1} subgraph and the induction hypothesis to show ||G|| <= t_{r-1}(n), with equality forcing the Turan structure.
- **Second proof** (vertex duplication): If G is not complete multipartite, there exist y_1, x, y_2 with y_1x, xy_2 not edges but y_1y_2 an edge; duplicating x produces a K^r-free graph with more edges, contradiction. (Diestel, pp. 165-167)

# Prerequisites
- **Extremal number** — The theorem determines ex(n, K^r)
- **Turan graph** — The unique extremal graph

# Key Properties
1. THE foundational result of extremal graph theory
2. Determines ex(n, K^r) = t_{r-1}(n) exactly
3. The extremal graph is unique: T^{r-1}(n)
4. t_{r-1}(n) <= (1/2)n^2(r-2)/(r-1), so ex(n, K^r) is about (r-2)/(2(r-1)) * n^2
5. Adding epsilon*n^2 edges beyond this forces not just K^r but K_s^r (Erdos-Stone theorem)

# Construction / Recognition
## Vertex Duplication (Second Proof Technique)
1. Given edge-maximal K^r-free graph G
2. If not complete multipartite, find y_1, x, y_2 with the required non-adjacency pattern
3. Delete lower-degree vertices, duplicate higher-degree vertex
4. Obtain K^r-free graph with more edges, contradicting extremality

# Context & Application
Turan's theorem sparked the entire field of extremal graph theory. It serves as a model for countless similar results. The Erdos-Stone theorem extends it to all graphs H, showing that the asymptotic extremal density is determined by chi(H).

# Examples
**Example** (p. 166, Fig. 7.1.3): Illustration of the inductive equation for r = 5, n = 14, showing the decomposition into a K^{r-1} and the remaining graph.

# Relationships
## Builds Upon
- **Extremal number**, **Turan graph**

## Enables
- **Erdos-Stone theorem** — Extends Turan's result beyond complete graphs
- Proof of **Theorem 9.2.2** — Used in the Ramsey theory chapter

## Related
- **Vertex duplication** — A proof technique introduced here

# Common Confusions
- **Confusion**: Thinking edge-maximality implies extremality
  **Clarification**: A graph can be edge-maximal without K^r but have fewer than ex(n, K^r) edges (Fig. 7.1.1)

# Source Reference
Chapter 7, Section 7.1, Theorem 7.1.1, pages 165-167 (pdf pages 175-177). Two complete proofs given.

# Verification Notes
- Confidence: HIGH — the central theorem of the section with two proofs
