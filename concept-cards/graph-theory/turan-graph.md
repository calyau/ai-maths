---
concept: "Tur\u00E1n Graph"
slug: turan-graph
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
  - "T^{r-1}(n)"
  - "Turan graph"
prerequisites:
  - graph
  - edge
related:
  - turan-theorem
  - extremal-number
  - erdos-stone-theorem
answers_questions:
  - "What is the Turan graph?"
  - "What is the densest K^r-free graph?"
---

# Quick Definition
The Turan graph T^{r-1}(n) is the unique complete (r-1)-partite graph on n vertices whose partition sets differ in size by at most 1. It is the extremal graph for K^r.

# Core Definition
The unique complete (r-1)-partite graph on n >= r-1 vertices whose partition sets differ in size by at most 1 is called the **Turan graph**, denoted T^{r-1}(n). Its number of edges is denoted t_{r-1}(n). For n < r-1, T^{r-1}(n) = K^n by convention. (Diestel, p. 165)

# Prerequisites
- **Graph** — Turan graphs are specific multipartite graphs

# Key Properties
1. Complete (r-1)-partite with partition sets as equal as possible
2. Unique for each n and r
3. Contains no K^r subgraph
4. Has the maximum number of edges among K^r-free graphs on n vertices (Turan's theorem)
5. t_{r-1}(n) <= (1/2) n^2 (r-2)/(r-1), with equality when (r-1) divides n
6. Dense: approximately n^2 edges in order of magnitude

# Construction / Recognition
## To Construct T^{r-1}(n)
1. Distribute n vertices into r-1 groups as evenly as possible (sizes differ by at most 1)
2. Connect every pair of vertices in different groups
3. No edges within groups

# Examples
**Example** (p. 165, Fig. 7.1.2): The Turan graph T^3(8), which is a complete 3-partite graph on 8 vertices with partition sets of sizes 3, 3, 2.

# Relationships
## Enables
- **Turan's theorem** — T^{r-1}(n) is the unique extremal graph
- **Erdos-Stone theorem** — t_{r-1}(n) is the threshold for K_s^r subgraphs

# Source Reference
Chapter 7, Section 7.1, page 165 (pdf page 175). See Fig. 7.1.2.

# Verification Notes
- Confidence: HIGH — explicitly defined with figure
