---
concept: 3-Connected Case of Kuratowski's Theorem
slug: three-connected-planarity
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "Lemma 4.4.3"
prerequisites:
  - planar-graph
  - kuratowski-theorem
extends: []
related:
  - kuratowski-theorem
contrasts_with: []
answers_questions:
  - "Why is the 3-connected case the heart of Kuratowski's theorem?"
---

# Quick Definition
Every 3-connected graph without a K^5 or K_{3,3} minor is planar (Lemma 4.4.3). This is the central lemma in the proof of Kuratowski's theorem, from which the general case follows.

# Core Definition
**Lemma 4.4.3**: "Every 3-connected graph G without a K^5 or K_{3,3} minor is planar" (Diestel, p. 97).

# Prerequisites
- **Planar graph**, **Kuratowski's theorem**

# Key Properties
1. The proof is by induction on |G|, contracting an edge to maintain 3-connectedness
2. Uses Lemma 3.2.1 to find an edge whose contraction preserves 3-connectedness
3. The key step: vertices of the contracted graph around the contraction point lie on a cycle face boundary
4. The proof can be adapted to produce convex drawings

# Context & Application
This lemma is "the heart of the proof" (Diestel). The general Kuratowski theorem is reduced to this case by showing that edge-maximal graphs without TK^5 or TK_{3,3} are 3-connected (Lemma 4.4.5).

# Relationships
## Enables
- **Kuratowski's theorem** -- The general case follows from this

# Source Reference
Chapter 4, Section 4.4, Lemma 4.4.3, pages 97-99.

# Verification Notes
- Full proof pp. 97-99
- Confidence: HIGH
