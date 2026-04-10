---
concept: "Kirchhoff's Theorem on Spanning Trees and Currents"
slug: kirchhoffs-theorem-spanning-trees
category: electrical-networks
subcategory: network-theory
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.1 Graphs and Electrical Networks"
extraction_confidence: high
aliases:
  - "Kirchhoff's current-tree theorem"
prerequisites:
  - electrical-network
  - spanning-tree
  - kirchhoffs-current-law
  - kirchhoffs-potential-law
extends: []
related:
  - matrix-tree-theorem
contrasts_with: []
answers_questions:
  - "How does the current in an edge relate to spanning trees?"
---

# Quick Definition

Kirchhoff's theorem states that in a unit-resistance network, the current in an edge $ab$ is $w_{ab} = \{N(s,a,b,t) - N(s,b,a,t)\}/N$, where $N$ is the total number of spanning trees and $N(s,a,b,t)$ counts spanning trees where the $s$-$t$ path passes through $a$ then $b$.

# Core Definition

"**Theorem 1.** Given an edge $ab$, denote by $N(s, a, b, t)$ the number of spanning trees of $G$ in which the (unique) path from $s$ to $t$ contains $a$ and $b$, in this order. [...] Write $N$ for the total number of spanning trees. Finally, let $w_{ab} = \{N(s, a, b, t) - N(s, b, a, t)\}/N$" (Bollobás, p. 52). The distribution $w_{ab}$ satisfies both Kirchhoff laws.

Theorem 2 generalizes to arbitrary conductances: $w_{ab} = \{N^*(s,a,b,t) - N^*(s,b,a,t)\}/N^*$ where $N^*$ uses weighted spanning trees (weight = product of edge conductances).

# Prerequisites

- **Electrical network** — The theorem describes current distribution
- **Spanning tree** — Currents are expressed via spanning tree counts
- **Kirchhoff's current law** — The solution must satisfy this
- **Kirchhoff's potential law** — The solution must satisfy this

# Key Properties

1. Current in each edge is a ratio of spanning tree counts
2. The proof uses the "thicket" (2-component forest) technique and double counting
3. Generalizes to weighted networks (Theorem 2) using conductance-weighted spanning trees
4. If conductances are rational, all currents are rational (Corollary 3)

# Construction / Recognition

To compute the current in edge $ab$:
1. Count spanning trees where the $s$-$t$ path goes through $a$ then $b$
2. Count spanning trees where it goes through $b$ then $a$
3. Subtract and divide by the total number of spanning trees

# Context & Application

This theorem provides the theoretical foundation for electrical network analysis using graph theory. It shows that current distribution is fundamentally about spanning tree structure. The result connects to the matrix-tree theorem.

# Examples

**Example** (pp. 52-53): The proof decomposes the problem by summing over all spanning trees $T$, each contributing a unit current along its unique $s$-$t$ path.

# Relationships

## Builds Upon
- **Electrical network**, **Spanning tree**, **Kirchhoff's laws**

## Enables
- **Matrix-tree theorem** — Related counting of spanning trees

## Related
- **Principle of superposition** — The proof superimposes single-tree currents

# Common Errors

- **Error**: Forgetting to subtract $N(s,b,a,t)$ from $N(s,a,b,t)$
  **Correction**: Current direction matters; the formula accounts for both directions

# Common Confusions

- **Confusion**: Thinking this only works for unit-resistance networks
  **Clarification**: Theorem 2 extends it to arbitrary conductances using weighted spanning trees

# Source Reference

Chapter II: Electrical Networks, Section II.1, Theorems 1-2, pages 52-53.

# Verification Notes

- Definition source: Direct theorem statement from p. 52
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
