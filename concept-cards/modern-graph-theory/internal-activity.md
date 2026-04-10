---
concept: Internal Activity
slug: internal-activity
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
  - "internally active edge"
prerequisites:
  - tutte-polynomial
extends: []
related:
  - external-activity
  - spanning-tree-expansion
contrasts_with:
  - external-activity
answers_questions:
  - "What distinguishes internally active from externally active edges?"
---

# Quick Definition
An edge $e_i$ in a spanning forest $F$ is internally active if $e_i$ is the smallest edge of the cut $U_F(e_i)$ it defines (with respect to a given edge ordering).

# Core Definition
"Call an edge $e_i \in E(F)$ an internally active edge (of $F$, with respect to the ordering of the edges of $G$) if $e_i$ is the smallest edge of the cut it defines. Thus $e_i \in E(F)$ is internally active if $i \leq j$ whenever $e_j \in U_F(e_i)$" (Bollobás, p. 356). The cut $U_F(e_i)$ consists of all edges that could replace $e_i$ in $F$ while preserving the spanning forest property.

# Prerequisites
- **Tutte polynomial** — Internal activity appears in the spanning tree expansion

# Key Properties
1. Only applies to edges IN the spanning forest
2. $e_i$ is internally active iff it is the smallest edge in its fundamental cut
3. The number of internally active edges is the internal activity of $F$
4. If $e$ is a bridge: always internally active (it is in every spanning forest)
5. The coefficient of $x^i$ in $T_G(x,0)$ counts forests with internal activity $i$

# Construction / Recognition
1. Fix an ordering $e_1, \ldots, e_m$ of edges
2. For a spanning forest $F$ and an edge $e_i \in E(F)$:
3. Compute the cut $U_F(e_i) = \{e_j : (F - e_i) + e_j \text{ is a spanning forest}\}$
4. $e_i$ is internally active iff $e_i$ is the smallest element of $U_F(e_i)$

# Context & Application
Internal activity is one of two types of "activity" that determine the spanning tree expansion of the Tutte polynomial. Each spanning forest contributes $x^i y^j$ where $i$ is the internal activity and $j$ is the external activity.

# Examples
**Example** (Fig. X.2, p. 357): In the spanning tree shown, edges $e_1$, $e_7$, $e_9$ are internally active (each is the smallest in its fundamental cut).

# Relationships
## Builds Upon
- **tutte-polynomial**

## Enables
- **spanning-tree-expansion** — $T_G = \sum t_{ij} x^i y^j$

## Contrasts With
- **external-activity** — For edges NOT in the forest

# Common Confusions
- **Confusion**: Thinking internal activity is a property of the edge alone.
  **Clarification**: Internal activity depends on the spanning forest AND the edge ordering. The same edge may be active in one forest but not another.

# Source Reference
Chapter X, Section X.5, page 356.

# Verification Notes
- Definition source: Direct from p. 356
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
