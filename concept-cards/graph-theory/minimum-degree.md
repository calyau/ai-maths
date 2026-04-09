---
concept: Minimum Degree
slug: minimum-degree

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
  - "delta(G)"

prerequisites:
  - graph
  - degree
extends: []
related:
  - maximum-degree
  - average-degree
contrasts_with:
  - maximum-degree

answers_questions:
  - "What is the minimum degree of a graph?"
  - "What does delta(G) mean?"
---

# Quick Definition
The minimum degree delta(G) of a graph G is the smallest degree among all its vertices.

# Core Definition
The number delta(G) := min { d(v) | v in V } is the minimum degree of G (Diestel, p. 5).

# Prerequisites
- **Graph** — minimum degree is a graph-level property
- **Degree** — it is the minimum of all vertex degrees

# Key Properties
1. delta(G) <= d(G) <= Delta(G) where d(G) is the average degree
2. Large minimum degree forces long paths and cycles (Proposition 1.3.1)
3. Large minimum degree does not by itself ensure high connectivity

# Context & Application
Minimum degree is one of the most commonly used graph invariants. Many fundamental results provide lower bounds on substructure based on minimum degree.

# Relationships
## Builds Upon
- **degree**

## Related
- **maximum-degree**, **average-degree**

## Contrasts With
- **maximum-degree** — the largest degree

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
