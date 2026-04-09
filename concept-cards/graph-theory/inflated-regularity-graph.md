---
concept: Inflated Regularity Graph
slug: inflated-regularity-graph
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 194
section: "7.5 Applying the regularity lemma"
extraction_confidence: high
aliases:
  - "R_s"
prerequisites:
  - regularity-graph
related:
  - embedding-lemma
  - erdos-stone-theorem
answers_questions:
  - "What is the inflated regularity graph R_s?"
---

# Quick Definition
Given a regularity graph R and integer s, the inflated graph R_s is obtained by replacing each vertex with s copies and each edge with a complete bipartite graph between the copies.

# Core Definition
Given a regularity graph R and s in N, **R_s** is obtained by replacing every vertex V_i of R by a set V_i^s of s vertices, and every edge by a complete bipartite graph between the corresponding s-sets. For R = K^r, we have R_s = K_s^r. (Diestel, p. 184)

# Prerequisites
- **Regularity graph** — R_s is built from R

# Key Properties
1. R_s is the "blown-up" version of R
2. For R = K^r: R_s = K_s^r (complete r-partite with parts of size s)
3. The embedding lemma states: H subset R_s implies H subset G (under conditions)
4. Any graph H with chi(H) <= r and alpha(H) >= s can be found in R_s if K^r subset R

# Relationships
## Builds Upon
- **Regularity graph**

## Enables
- **Embedding lemma** — Subgraphs of R_s can be found in G
- **Erdos-Stone theorem** — K_s^r subset R_s when K^r subset R

# Source Reference
Chapter 7, Section 7.5, page 184 (pdf page 194).

# Verification Notes
- Confidence: HIGH — explicitly defined
