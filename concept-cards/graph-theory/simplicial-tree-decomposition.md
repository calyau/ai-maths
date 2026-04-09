---
concept: Simplicial Tree-Decomposition
slug: simplicial-tree-decomposition
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 336
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases: []
prerequisites:
  - tree-decomposition
extends:
  - tree-decomposition
related:
  - chordal-graph-characterization
contrasts_with: []
answers_questions:
  - "What is a simplicial tree-decomposition?"
---

# Quick Definition
A tree-decomposition is simplicial if all its separators V_{t1} cap V_{t2} induce complete subgraphs in G. Simplicial decompositions allow properties of parts to be lifted to G.

# Core Definition
The tree-decomposition (T, V) of G is *simplicial* if all the separators V_{t1} cap V_{t2} induce complete subgraphs in G. If all parts are k-colourable, then G is k-colourable. If all parts have no K^r minor, then G has no K^r minor (Diestel, p. 336).

# Prerequisites
- **Tree-decomposition** — Simplicial is a strengthening

# Key Properties
1. Properties like k-colourability lift from parts to the whole graph
2. G is chordal iff G has a tree-decomposition into complete parts (Proposition 12.3.11)
3. Any graph without K^5 minor has a supergraph with simplicial tree-decomposition into plane triangulations and Wagner graphs

# Relationships
## Builds Upon
- **Tree-decomposition** — Simplicial adds a completeness condition

## Enables
- Characterization of chordal graphs

# Source Reference
Chapter 12, Section 12.3, page 336.

# Verification Notes
- Definition from p. 336
- Confidence: HIGH — explicit definition
