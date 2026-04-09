---
concept: Vertex Expansion
slug: vertex-expansion
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "expanding a vertex to an edge"
prerequisites:
  - perfect-graph
extends: []
related:
  - perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "What is vertex expansion in perfect graph theory?"
---

# Quick Definition
Expanding a vertex x of G to an edge means adding a new vertex x' adjacent to x and all neighbours of x. Lemma 5.5.5 shows that expanding a vertex of a perfect graph yields a perfect graph.

# Core Definition
"Let G be a graph and x in G a vertex, and let G' be obtained from G by adding a vertex x' and joining it to x and all the neighbours of x. We say that G' is obtained from G by expanding the vertex x to an edge xx'" (Diestel, p. 129).

# Prerequisites
- **Perfect graph** -- Used in the proof of the perfect graph theorem

# Key Properties
1. x' gets the same neighbours as x, plus x itself
2. Preserves perfection: expanding a vertex of a perfect graph gives a perfect graph (Lemma 5.5.5)
3. Key technical tool in Lovasz's proof of the perfect graph theorem

# Relationships
## Enables
- **Perfect graph theorem** -- Vertex expansion is the key lemma

# Source Reference
Chapter 5, Section 5.5, Lemma 5.5.5, pages 129-130.

# Verification Notes
- Definition from p. 129
- Confidence: HIGH -- explicit definition with lemma
