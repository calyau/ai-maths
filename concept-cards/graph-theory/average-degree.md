---
concept: Average Degree
slug: average-degree

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 15
section: "1.2 The degree of a vertex"

extraction_confidence: high

aliases:
  - "d(G)"

prerequisites:
  - graph
  - degree
extends: []
related:
  - minimum-degree
  - maximum-degree
  - edge-density
  - handshaking-lemma
contrasts_with: []

answers_questions:
  - "What is the average degree of a graph?"
  - "What does d(G) mean?"
---

# Quick Definition
The average degree d(G) of a graph G is the sum of all vertex degrees divided by the number of vertices.

# Core Definition
The number d(G) := (1/|V|) * sum of d(v) over all v in V is the average degree of G. We have delta(G) <= d(G) <= Delta(G). The average degree quantifies globally what is measured locally by the vertex degrees: the number of edges of G per vertex (Diestel, p. 5).

# Prerequisites
- **Graph** — average degree is a graph property
- **Degree** — it averages all vertex degrees

# Key Properties
1. delta(G) <= d(G) <= Delta(G)
2. d(G) = 2 * epsilon(G) where epsilon(G) = |E|/|V| is the edge density
3. |E| = (1/2) * d(G) * |V| (from the Handshaking Lemma)

# Context & Application
Average degree is a global measure of edge density. It features prominently in Theorem 1.4.3 (Mader's theorem), which guarantees highly connected subgraphs from large average degree.

# Relationships
## Builds Upon
- **degree**

## Related
- **edge-density** — epsilon(G) = d(G)/2
- **handshaking-lemma** — connects sum of degrees to number of edges

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
