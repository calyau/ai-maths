---
concept: Maximum Degree
slug: maximum-degree

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
  - "Delta(G)"

prerequisites:
  - graph
  - degree
extends: []
related:
  - minimum-degree
  - average-degree
contrasts_with:
  - minimum-degree

answers_questions:
  - "What is the maximum degree of a graph?"
  - "What does Delta(G) mean?"
---

# Quick Definition
The maximum degree Delta(G) of a graph G is the largest degree among all its vertices.

# Core Definition
The number Delta(G) := max { d(v) | v in V } is the maximum degree of G (Diestel, p. 5).

# Prerequisites
- **Graph** — maximum degree is a graph-level property
- **Degree** — it is the maximum of all vertex degrees

# Key Properties
1. delta(G) <= d(G) <= Delta(G)
2. For a graph on n vertices, Delta(G) <= n - 1
3. Delta(G) = n - 1 if and only if G has a vertex adjacent to all others

# Relationships
## Builds Upon
- **degree**

## Contrasts With
- **minimum-degree** — the smallest degree

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
