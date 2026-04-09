---
concept: Independent Set
slug: independent-set

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "stable set"
  - "independent"

prerequisites:
  - graph
  - adjacent
extends: []
related:
  - complete-graph
  - complement
contrasts_with:
  - complete-graph

answers_questions:
  - "What is an independent set?"
  - "What does independent mean for vertices or edges?"
---

# Quick Definition
A set of vertices or edges is independent (or stable) if no two of its elements are adjacent.

# Core Definition
Pairwise non-adjacent vertices or edges are called independent. More formally, a set of vertices or of edges is independent (or stable) if no two of its elements are adjacent (Diestel, p. 3).

# Prerequisites
- **Graph** — independent sets exist within a graph
- **Adjacent** — independence is defined as the absence of adjacency

# Key Properties
1. An independent set of vertices has no edges between any pair of its elements
2. An independent set of edges has no two edges sharing an endpoint (this is also called a matching)
3. The empty set and any singleton are trivially independent
4. Every subset of an independent set is independent

# Construction / Recognition
A set S of vertices is independent if and only if no edge of G has both endpoints in S.

# Context & Application
Independent sets are central to many graph-theoretic problems, including graph coloring (where each color class must be independent).

# Relationships
## Builds Upon
- **graph**, **adjacent**

## Contrasts With
- **complete-graph** — all vertices pairwise adjacent (the opposite extreme)

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
