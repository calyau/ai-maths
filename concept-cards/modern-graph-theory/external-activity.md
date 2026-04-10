---
concept: External Activity
slug: external-activity
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 356
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "externally active edge"
prerequisites:
  - tutte-polynomial
extends: []
related:
  - internal-activity
  - spanning-tree-expansion
contrasts_with:
  - internal-activity
answers_questions:
  - "What distinguishes internally active from externally active edges?"
---

# Quick Definition
An edge $e_j$ NOT in a spanning forest $F$ is externally active if $e_j$ is the smallest edge of the cycle $Z_F(e_j)$ it defines.

# Core Definition
"Call $e_j \in E(G) - E(F)$ externally active if $e_j$ is the smallest edge of the cycle it defines, that is, if $i \geq j$ whenever $e_i \in Z_F(e_j)$" (Bollobás, p. 356). The cycle $Z_F(e_j)$ is the unique cycle formed by adding $e_j$ to $F$.

# Prerequisites
- **Tutte polynomial** — External activity appears in the spanning tree expansion

# Key Properties
1. Only applies to edges NOT in the spanning forest
2. $e_j$ is externally active iff it is the smallest edge in its fundamental cycle
3. If $e$ is a loop: always externally active
4. The coefficient of $y^j$ in $T_G(0,y)$ counts forests with external activity $j$

# Construction / Recognition
1. Fix an ordering $e_1, \ldots, e_m$ of edges
2. For a spanning forest $F$ and $e_j \notin E(F)$:
3. Compute the cycle $Z_F(e_j)$ (the unique cycle in $F + e_j$)
4. $e_j$ is externally active iff $e_j$ is the smallest element of $Z_F(e_j)$

# Examples
**Example** (Fig. X.2, p. 357): Edges $e_2, e_3$ are externally active.

# Relationships
## Builds Upon
- **tutte-polynomial**

## Enables
- **spanning-tree-expansion**

## Contrasts With
- **internal-activity** — For edges IN the forest

# Source Reference
Chapter X, Section X.5, page 356.

# Verification Notes
- Definition source: Direct from p. 356
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
