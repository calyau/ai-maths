---
# === CORE IDENTIFICATION ===
concept: Balanced Graph
slug: balanced-graph

# === CLASSIFICATION ===
category: random-graphs
subcategory: subgraph-containment
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 239
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgraph-count-expectation
extends: []
related:
  - threshold-function
  - variance-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a balanced graph?"
  - "Which graphs have sharp thresholds for appearance in random graphs?"
---

# Quick Definition

A graph $F = G(k, \ell)$ is balanced if no subgraph has strictly larger average degree; equivalently, every subgraph with $k'$ vertices has at most $k'\ell/k$ edges.

# Core Definition

Following Erdos and Renyi, a graph $F = G(k, \ell)$ with $k$ vertices and $\ell$ edges is balanced if every subgraph with $k'$ vertices has at most $k'\ell/k$ edges. Equivalently, the average degree $2\ell/k$ is maximal among all subgraphs. Complete graphs, cycles, and trees are balanced (Bollobás, p. 239).

# Prerequisites

- **Subgraph count expectation** -- The threshold is determined by when $\mathbb{E}(X_F) \to \infty$

# Key Properties

1. Complete graphs $K_s$ are balanced
2. Cycles $C_k$ are balanced
3. Trees are balanced
4. Balanced graphs have a clean threshold for appearance: $p^*(n) = n^{-k/\ell}$
5. Not all graphs are balanced (e.g., a triangle with a pendant edge)

# Construction / Recognition

## To Check if $F = G(k, \ell)$ is Balanced
1. For each subgraph $F'$ with $k'$ vertices and $\ell'$ edges
2. Verify $\ell'/k' \le \ell/k$
3. If all subgraphs satisfy this, $F$ is balanced

# Context & Application

**Theorem 7** (Bollobás, p. 239): If $F$ is balanced with $k$ vertices and $\ell$ edges, then $p(n)n^{k/\ell} \to 0$ implies almost no $G_{n,p}$ contains $F$, and $p(n)n^{k/\ell} \to \infty$ implies almost every $G_{n,p}$ contains $F$. The threshold function for containment of balanced $F$ is $n^{-k/\ell}$.

# Examples

**Example** (p. 239, Fig. VII.1): The first two graphs shown are balanced; the second two are not. A graph consisting of a triangle attached to a single edge is unbalanced because the triangle subgraph has average degree $2 > 2 \cdot 4/4 = 2$.

# Relationships

## Builds Upon
- **Subgraph count expectation** -- Determines the threshold

## Enables
- **Threshold function** -- Balanced graphs have $n^{-k/\ell}$ as threshold

## Related
- **Variance method** -- Used to prove the upper threshold
- **Threshold function** -- Balanced graphs have clean thresholds

## Contrasts With
- None

# Common Errors

- **Error**: Assuming all graphs are balanced
  **Correction**: A graph with a denser subgraph is not balanced; the threshold for unbalanced graphs depends on the densest subgraph

# Common Confusions

- **Confusion**: Confusing balanced with regular
  **Clarification**: Balanced refers to average degree of subgraphs, not degree regularity of vertices

# Source Reference

Chapter VII: Random Graphs, Section VII.3, Theorem 7, pages 239--240.

# Verification Notes

- Definition source: Direct from p. 239
- Confidence rationale: Explicit definition with theorem
- Uncertainties: None
- Cross-reference status: Verified
