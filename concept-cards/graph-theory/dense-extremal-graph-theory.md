---
concept: Dense Extremal Graph Theory
slug: dense-extremal-graph-theory
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
  - "dense extremal theory"
prerequisites:
  - graph
  - proportional-edge-density
related:
  - turan-theorem
  - erdos-stone-theorem
  - regularity-lemma
contrasts_with:
  - sparse-extremal-graph-theory
answers_questions:
  - "What is dense extremal graph theory?"
---

# Quick Definition
Dense extremal graph theory studies what edge density (quadratic in n) is needed to force a given graph H as a subgraph. The Erdos-Stone theorem is the fundamental result.

# Core Definition
If we ask what global assumptions might imply the existence of some given graph H as a subgraph, it will not help to raise invariants like epsilon or chi (unless H is bipartite). Unless H is bipartite, any function f such that f(n) edges force an H subgraph must grow quadratically with n. The question of exactly which edge density forces a given subgraph is the archetypal extremal graph problem. (Diestel, p. 163)

# Prerequisites
- **Graph** — Dense graphs with quadratic edge counts
- **Proportional edge density** — The density ||G||/C(|G|,2)

# Key Properties
1. Quadratic edge counts needed for non-bipartite subgraphs
2. Turan's theorem: exact answer for H = K^r
3. Erdos-Stone theorem: asymptotic answer for all H
4. The regularity lemma is the key modern proof technique

# Relationships
## Contrasts With
- **Sparse extremal graph theory** — Needs only linear edges for minors

# Source Reference
Chapter 7, introduction, page 163 (pdf page 173). Section 7.1.

# Verification Notes
- Confidence: HIGH — framework explicitly described
