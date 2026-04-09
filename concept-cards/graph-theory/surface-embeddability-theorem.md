---
concept: Surface Embeddability Theorem
slug: surface-embeddability-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 352
section: "12.5 The graph minor theorem"
extraction_confidence: high
aliases:
  - "generalized Kuratowski theorem"
  - "Corollary 12.5.3"
prerequisites:
  - graph-minor-theorem
  - wqo-bounded-tree-width
  - grid-theorem
extends: []
related:
  - kuratowski-set
contrasts_with: []
answers_questions:
  - "Is embeddability in a surface characterized by finitely many forbidden minors?"
---

# Quick Definition
For every surface S, there exists a finite set of graphs H_1, ..., H_n such that a graph is embeddable in S if and only if it contains none of them as a minor (Corollary 12.5.3).

# Core Definition
**Corollary 12.5.3**: For every surface S there exists a finite set of graphs H_1, ..., H_n such that a graph is embeddable in S if and only if it contains none of H_1, ..., H_n as a minor (Diestel, p. 352).

# Prerequisites
- **Graph minor theorem** — Or more directly: the bounded tree-width WQO and grid theorem
- **WQO for bounded tree-width** — Graphs in K_{P(S)} have bounded tree-width
- **Grid theorem** — Graphs in K_{P(S)} have no large grid minors

# Key Properties
1. The proof does not need the full graph minor theorem
2. Key step: graphs minimal with respect to not embedding in S have bounded tree-width
3. Then Theorem 12.3.7 (WQO for bounded tree-width) gives finiteness
4. For the sphere: K_P = {K^5, K_{3,3}} (Kuratowski). For the projective plane: 35 forbidden minors

# Source Reference
Chapter 12, Section 12.5, pages 352-357 (Corollary 12.5.3, Lemma 12.5.4).

# Verification Notes
- Statement from p. 352, direct proof on pp. 353-357
- Confidence: HIGH — named corollary with complete proof
