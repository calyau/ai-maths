---
concept: Sparse Extremal Graph Theory
slug: sparse-extremal-graph-theory
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 173
section: "7.2 Minors"
extraction_confidence: high
aliases:
  - "sparse extremal theory"
prerequisites:
  - graph
  - edge-density
related:
  - mader-theorem-topological-minors
  - kostochka-theorem
  - proportional-edge-density
contrasts_with:
  - dense-extremal-graph-theory
answers_questions:
  - "What is sparse extremal graph theory?"
---

# Quick Definition
Sparse extremal graph theory studies how a linear number of edges (relative to vertices) forces the containment of a given graph as a minor or topological minor.

# Core Definition
If we are looking for ways to ensure by global assumptions that a graph G contains some given graph H as a minor (or topological minor), it suffices to raise ||G|| above some linear function of |G|, i.e., to make epsilon(G) large enough. The precise value of epsilon needed to force a desired minor or topological minor is the topic of Section 7.2. (Diestel, p. 163)

# Prerequisites
- **Graph** — Graphs with linear edge counts
- **Edge density** — epsilon(G) = ||G||/|G| is the key parameter

# Key Properties
1. Linear number of edges suffices for minors
2. cr^2 average degree forces TK^r (Theorem 7.2.1)
3. cr*sqrt(log r) average degree forces K^r minor (Theorem 7.2.2)
4. Contrasts with dense extremal theory where quadratic edge counts are needed for subgraphs

# Relationships
## Contrasts With
- **Dense extremal graph theory** — Needs quadratic edges for subgraphs

# Source Reference
Chapter 7, introduction, page 163 (pdf page 173). Section 7.2.

# Verification Notes
- Confidence: HIGH — framework explicitly described in chapter introduction
