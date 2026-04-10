---
concept: Cut Defined by a Tree Edge
slug: cut-defined-by-tree-edge
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
  - "fundamental cut"
  - "U_F(e)"
prerequisites:
  - spanning-forest
extends: []
related:
  - internal-activity
  - cycle-defined-by-chord
contrasts_with:
  - cycle-defined-by-chord
answers_questions:
  - "What distinguishes internally active from externally active edges?"
---

# Quick Definition
For a spanning forest $F$ and an edge $e_i \in E(F)$, the cut $U_F(e_i) = \{e_j \in E(G) : (F - e_i) + e_j \text{ is a spanning forest}\}$ is the set of edges that can replace $e_i$.

# Core Definition
"For $e_i \in E(F)$ we call $U_F(e_i) = \{e_j \in E(G) : (F - e_i) + e_j \text{ is a spanning forest}\}$ the cut defined by $e_i$" (Bollobás, p. 356). An edge $e_i$ is internally active iff it is the smallest edge of $U_F(e_i)$.

# Prerequisites
- **Spanning forest** — Cuts are defined relative to a forest

# Key Properties
1. $U_F(e_i)$ always contains $e_i$ itself
2. Removing $e_i$ disconnects $F$; elements of $U_F(e_i)$ reconnect it
3. $e_i$ is internally active iff $e_i = \min U_F(e_i)$

# Relationships
## Builds Upon
- **spanning-forest**

## Enables
- **internal-activity** — Defined via cuts

## Contrasts With
- **cycle-defined-by-chord** — For edges not in $F$

# Source Reference
Chapter X, Section X.5, page 356.

# Verification Notes
- Definition source: Direct from p. 356
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
