---
concept: System of Distinct Representatives
slug: system-of-distinct-representatives
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "SDR"
  - "transversal"
prerequisites:
  - matching
extends: []
related:
  - complete-matching
  - halls-theorem
contrasts_with: []
answers_questions:
  - "What is a system of distinct representatives?"
---

# Quick Definition
A system of distinct representatives (SDR) for a family $\mathcal{A} = \{A_1, \ldots, A_m\}$ of subsets of a set $X$ is a set $\{x_1, \ldots, x_m\}$ of distinct elements with $x_i \in A_i$.

# Core Definition
Given a family $\mathcal{A} = \{A_1, A_2, \ldots, A_m\}$ of subsets of a set $X$, a set $\{x_1, x_2, \ldots, x_m\}$ with $x_i \in A_i$ and $x_i \ne x_j$ for $i \ne j$ is called a set of distinct representatives of $\mathcal{A}$. This corresponds to a complete matching from $V_1 = \mathcal{A}$ to $V_2 = X$ in the natural bipartite graph where $A_i$ is joined to each $x \in A_i$ (Bollobás, p. 85).

# Prerequisites
- **Matching** — An SDR corresponds to a complete matching

# Key Properties
1. Each $A_i$ contributes exactly one representative
2. All representatives are distinct elements of $X$
3. Existence characterized by Hall's condition: $|\bigcup_{i \in F} A_i| \ge |F|$ for every $F \subset \{1, \ldots, m\}$ (Theorem 8)

# Construction / Recognition
1. Formulate as a bipartite graph with vertex classes $\mathcal{A}$ and $X$
2. Find a complete matching from $\mathcal{A}$ to $X$
3. The matched elements form the SDR

# Context & Application
The SDR formulation connects combinatorics of set systems to graph matching theory. Hall's theorem (Theorem 8) gives the necessary and sufficient condition.

# Examples
**Example** (p. 84): The problem of finding group elements $g_1, \ldots, g_n$ such that $\{g_1H, \ldots, g_nH\}$ gives all left cosets and $\{Hg_1, \ldots, Hg_n\}$ gives all right cosets reduces to finding an SDR.

# Relationships
## Builds Upon
- **matching** — SDR = complete matching

## Enables
- **halls-theorem** — Theorem 8 formulation

# Common Errors
- **Error**: Allowing repeated elements in the SDR
  **Correction**: All representatives must be *distinct*

# Common Confusions
- **Confusion**: Thinking any choice function gives an SDR
  **Clarification**: A choice function picks one element from each set; an SDR additionally requires distinctness

# Source Reference
Chapter III, Section III.3, pages 84-85. Theorem 8.

# Verification Notes
- Definition source: Direct from pp. 84-85
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
