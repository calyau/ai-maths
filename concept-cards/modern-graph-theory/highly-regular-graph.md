---
# === CORE IDENTIFICATION ===
concept: Highly Regular Graph
slug: highly-regular-graph

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: highly-symmetric-graphs
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 278
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjacency-matrix
extends: []
related:
  - strongly-regular-graph
  - collapsed-adjacency-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a highly regular graph?"
---

# Quick Definition

A connected graph $G$ is highly regular with collapsed adjacency matrix $C = (c_{ij})$ if for every vertex $x$ there is a partition of $V$ into sets $V_1 = \{x\}, V_2, \ldots, V_p$ such that each vertex in $V_j$ is adjacent to exactly $c_{ij}$ vertices in $V_i$.

# Core Definition

A connected graph $G$ is highly regular with collapsed adjacency matrix $C = (c_{ij})$ if for every vertex $x \in V$ there is a partition $V_1 = \{x\}, V_2, \ldots, V_p$ such that each $y \in V_j$ is adjacent to exactly $c_{ij}$ vertices in $V_i$. The key result: $\pi_r A = C\pi_r$ (Theorem 15), meaning $A$ and $C$ have the same minimal polynomial and hence the same eigenvalues (Bollobas, pp. 278--280).

# Prerequisites

- **Adjacency matrix** -- The algebraic framework

# Key Properties

1. $G$ is necessarily regular
2. Each column sum of $C$ equals $k$ (the degree)
3. Eigenvalues of $A$ are exactly the eigenvalues of $C$ (Theorem 15)
4. The collapsed matrix $C$ is much smaller than $A$

# Construction / Recognition

## To Check High Regularity
1. For each vertex $x$, find a partition $V_1 = \{x\}, V_2, \ldots, V_p$
2. For each vertex $y \in V_j$, count adjacencies to $V_i$
3. Verify the count depends only on $i, j$ and not on $y$

# Context & Application

Highly regular graphs generalize strongly regular graphs (which have $p = 3$). The collapsed adjacency matrix enables spectral analysis without computing the full $n \times n$ spectrum.

# Examples

**Example** (p. 278, Fig. VIII.11): The pentagon, cube, and Petersen graph with their collapsed matrices.

# Relationships

## Builds Upon
- **Adjacency matrix**

## Enables
- **Strongly regular graph** -- The case $p = 3$
- **Collapsed adjacency matrix** -- The reduced spectral tool

## Related
- **Collapsed adjacency matrix** -- The defining structure

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all regular graphs are highly regular
  **Correction**: High regularity requires a specific partition property far beyond mere degree regularity

# Common Confusions

- **Confusion**: Confusing high regularity with vertex-transitivity
  **Clarification**: High regularity is a combinatorial condition; vertex-transitivity is a group-theoretic one

# Source Reference

Chapter VIII, Section VIII.3, pages 278--280. Theorems 15--16.

# Verification Notes

- Definition source: Direct from p. 278
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
