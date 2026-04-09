---
concept: Forest
slug: forest

category: trees-and-forests
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 23
section: "1.5 Trees and forests"

extraction_confidence: high

aliases:
  - "acyclic graph"

prerequisites:
  - graph
  - cycle
extends: []
related:
  - tree
contrasts_with:
  - tree

answers_questions:
  - "What is a forest?"
---

# Quick Definition
A forest is an acyclic graph (a graph containing no cycles). Its components are trees.

# Core Definition
An acyclic graph, one not containing any cycles, is called a forest. A connected forest is called a tree. Thus, a forest is a graph whose components are trees (Diestel, p. 13).

# Prerequisites
- **Graph** — a forest is a graph
- **Cycle** — a forest is defined by the absence of cycles

# Key Properties
1. Every component of a forest is a tree
2. A forest on n vertices with k components has n - k edges
3. A connected forest is a tree

# Relationships
## Builds Upon
- **graph**, **cycle** (by its absence)

## Related
- **tree** — a connected forest

## Contrasts With
- **tree** — a tree is connected; a forest need not be

# Source Reference
Chapter 1: The Basics, Section 1.5, page 13 (pdf p. 23).

# Verification Notes
- Direct from p. 13
- Confidence: HIGH
