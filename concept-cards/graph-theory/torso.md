---
concept: Torso
slug: torso
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 349
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases: []
prerequisites:
  - tree-decomposition
extends:
  - tree-decomposition
related:
  - excluded-kn-structure-theorem
contrasts_with: []
answers_questions:
  - "What is a torso of a tree-decomposition?"
---

# Quick Definition
The torso H_t of a part V_t in a tree-decomposition is the graph obtained from G[V_t] by adding all edges xy where x, y are in V_t cap V_{t'} for some neighbour t' of t in T. If the decomposition is simplicial, torsos equal parts.

# Core Definition
The *torsos* of a tree-decomposition (T, (V_t)_{t in T}) of G are the graphs H_t (t in T) obtained from G[V_t] by adding all the edges xy such that x, y in V_t cap V_{t'} for some neighbour t' of t in T (Diestel, p. 349).

# Prerequisites
- **Tree-decomposition** — Torsos are defined from tree-decompositions

# Key Properties
1. Torsos "complete" the separators to cliques
2. In the excluded K^n structure theorem, torsos are nearly embeddable in bounded-genus surfaces
3. If the decomposition is simplicial, torsos equal the induced subgraphs G[V_t]

# Relationships
## Builds Upon
- **Tree-decomposition** — Torsos are derived from decompositions

## Related
- **Excluded K^n structure theorem** — Constrains torso structure

# Source Reference
Chapter 12, Section 12.4, page 349.

# Verification Notes
- Definition from p. 349
- Confidence: HIGH — explicit definition
