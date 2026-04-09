---
concept: Vertex Duplication
slug: vertex-duplication
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 177
section: "7.1 Subgraphs"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
  - vertex
  - edge
related:
  - turan-theorem
answers_questions:
  - "What is vertex duplication?"
---

# Quick Definition
Duplicating a vertex v in G means adding a new vertex v' and joining it to exactly the neighbours of v (but not to v itself).

# Core Definition
By **duplicating** a vertex v in G we mean adding to G a new vertex v' and joining it to exactly the neighbours of v (but not to v itself). This operation preserves the absence of K^r (if v was not in a K^{r-1}) and changes the edge count by d(v) - d(x) when replacing x with a duplicate of v. (Diestel, p. 166)

# Prerequisites
- **Graph**, **Vertex**, **Edge**

# Key Properties
1. The new vertex v' has the same neighbourhood as v (minus v itself)
2. If G has no K^r and v is not in a K^{r-1} with v', then the new graph also has no K^r
3. Used in the second proof of Turan's theorem to show extremal graphs are complete multipartite

# Relationships
## Enables
- **Turan's theorem** — Key technique in the second proof

# Source Reference
Chapter 7, Section 7.1, page 166 (pdf page 177).

# Verification Notes
- Confidence: HIGH — explicitly defined operation
