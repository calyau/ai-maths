---
concept: Cycle Defined by a Chord
slug: cycle-defined-by-chord
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 356
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "fundamental cycle"
  - "Z_F(e)"
prerequisites:
  - spanning-forest
extends: []
related:
  - external-activity
  - cut-defined-by-tree-edge
contrasts_with:
  - cut-defined-by-tree-edge
answers_questions:
  - "What distinguishes internally active from externally active edges?"
---

# Quick Definition
For a spanning forest $F$ and a chord $e_j \in E(G) - E(F)$, the cycle $Z_F(e_j)$ is the unique cycle in $F + e_j$; $e_j$ is externally active iff it is the smallest edge of $Z_F(e_j)$.

# Core Definition
"For $e_i \in E(G) - E(F)$, the cycle defined by $e_i$ is the unique cycle of $F + e_i$; we write $Z_F(e_i)$ for the edge set of this cycle" (Bollobás, p. 356).

# Prerequisites
- **Spanning forest** — Cycles are defined relative to a forest

# Key Properties
1. Adding any non-forest edge to $F$ creates exactly one cycle
2. $Z_F(e_j)$ always contains $e_j$
3. $e_j$ is externally active iff $e_j = \min Z_F(e_j)$

# Relationships
## Builds Upon
- **spanning-forest**

## Enables
- **external-activity** — Defined via cycles

## Contrasts With
- **cut-defined-by-tree-edge** — For edges in $F$

# Source Reference
Chapter X, Section X.5, page 356.

# Verification Notes
- Definition source: Direct from p. 356
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
