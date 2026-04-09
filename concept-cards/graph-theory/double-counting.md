---
concept: Double Counting
slug: double-counting
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "counting in two ways"
prerequisites:
  - euler-formula
extends: []
related:
  - edge-bound-planar
contrasts_with: []
answers_questions:
  - "What is double counting in combinatorics?"
---

# Quick Definition
Double counting is a proof technique that counts the edges of a bipartite incidence graph in two ways (by each side's degrees). Used in the proof of Corollary 4.2.10 to derive m <= 3n - 6.

# Core Definition
The proof of Corollary 4.2.10 uses a bipartite graph on E(G) U F(G) with edge set {ef | e is on boundary of f}. This graph has 2|E(G)| = 3|F(G)| edges, yielding 2m = 3l, which combined with Euler's formula gives m = 3n - 6 (Diestel, p. 91).

# Prerequisites
- **Euler's formula**

# Key Properties
1. Count edges of a bipartite incidence structure from both sides
2. Each edge of G is incident with exactly 2 faces (in a triangulation)
3. Each face boundary has exactly 3 edges (in a triangulation)
4. Therefore 2m = 3l; with Euler's formula: m = 3n - 6

# Context & Application
Diestel highlights double counting as "a technique widely used in combinatorics" (Notes, p. 109). It appears in the edge bound proof and is used throughout later chapters.

# Relationships
## Enables
- **Edge bound** m <= 3n - 6

# Source Reference
Chapter 4, Section 4.2, Corollary 4.2.10, page 91. Notes, page 109.

# Verification Notes
- Technique from p. 91
- Confidence: HIGH
