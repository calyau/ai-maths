---
concept: Chordal Graph Characterization
slug: chordal-graph-characterization
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
  - simplicial-tree-decomposition
extends: []
related:
  - tree-width
contrasts_with: []
answers_questions:
  - "How are chordal graphs characterized by tree-decompositions?"
---

# Quick Definition
G is chordal if and only if G has a tree-decomposition into complete parts (Proposition 12.3.11). Consequently, tw(G) = min{omega(H) - 1 : G subset H, H chordal} (Corollary 12.3.12).

# Core Definition
**Proposition 12.3.11**: G is chordal if and only if G has a tree-decomposition into complete parts (Diestel, p. 336). **Corollary 12.3.12**: tw(G) = min{omega(H) - 1 : G subset H, H chordal} (Diestel, p. 336).

# Prerequisites
- **Tree-decomposition** — The structural framework
- **Simplicial tree-decomposition** — Decomposition into complete parts is simplicial

# Key Properties
1. G is chordal iff every induced cycle has a chord
2. Chordal graphs have tree-decompositions into cliques
3. Tree-width can be computed via chordal supergraphs

# Relationships
## Related
- **Tree-width** — tw(G) = min{omega(H)-1 : H chordal supergraph}

# Source Reference
Chapter 12, Section 12.3, page 336 (Proposition 12.3.11, Corollary 12.3.12).

# Verification Notes
- Statements from p. 336
- Confidence: HIGH — explicit propositions
