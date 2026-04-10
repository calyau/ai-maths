---
concept: Tutte Polynomial
slug: tutte-polynomial
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 340
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "T_G(x,y)"
  - "T(G; x, y)"
  - "dichromate"
  - "Tutte-Whitney polynomial"
prerequisites: []
extends:
  - rank-generating-polynomial
related:
  - chromatic-polynomial-from-tutte
  - flow-polynomial
  - deletion-contraction
  - universal-polynomial-of-graphs
  - dichromatic-polynomial
contrasts_with:
  - chromatic-polynomial
answers_questions:
  - "What is the Tutte polynomial?"
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
  - "What must I know before understanding the Tutte polynomial?"
  - "What distinguishes the chromatic polynomial from the Tutte polynomial?"
---

# Quick Definition
The Tutte polynomial $T_G(x,y)$ of a multigraph $G = (V,E)$ is a two-variable polynomial encoding extensive structural information about $G$, defined as $T_G(x,y) = \sum_{F \subset E} (x-1)^{r(E)-r(F)}(y-1)^{n(F)}$.

# Core Definition
The Tutte polynomial is $T_G(x,y) = S(G; x-1, y-1) = \sum_{F \subset E}(x-1)^{r(E)-r(F)}(y-1)^{n(F)}$ (Bollobás, p. 343, equation (1)), where $S$ is the rank-generating polynomial, $r(F) = |V| - k(F)$ is the rank and $n(F) = |F| - r(F)$ is the nullity. "This polynomial, a considerable generalization of the chromatic polynomial, was constructed by Tutte in 1954" (p. 340).

# Prerequisites
This is a foundational concept for Chapter X. It builds on basic graph theory: rank, nullity, spanning subgraphs, deletion and contraction. First mentioned in Chapter V (p. 158) as a "substantial generalization of the chromatic polynomial."

# Key Properties
1. Recursive: $T_G = x T_{G-e}$ (bridge), $T_G = y T_{G-e}$ (loop), $T_G = T_{G-e} + T_{G/e}$ (otherwise)
2. $T_{E_n} = 1$ for the empty $n$-graph
3. Multiplicative: $T_{G_1 \cup G_2} = T_{G_1} \cdot T_{G_2}$ when $G_1, G_2$ share at most one vertex
4. $\deg_x T_G = r(G)$, $\deg_y T_G = n(G)$
5. $T(K_2) = x$, $T(L) = y$ where $L$ is the loop graph
6. If $e$ is a bridge or loop: $T_{G-e} = T_{G/e}$
7. Encodes chromatic polynomial, flow polynomial, number of spanning trees, reliability, and statistical mechanics partition functions

# Construction / Recognition
## To Compute $T_G$ by Deletion-Contraction
1. If $G$ has no edges, $T_G = 1$
2. If $e$ is a bridge: $T_G = x \cdot T_{G-e}$
3. If $e$ is a loop: $T_G = y \cdot T_{G-e}$
4. Otherwise: $T_G = T_{G-e} + T_{G/e}$
5. Apply recursively until all graphs have no edges

# Context & Application
The Tutte polynomial is "the best known member of a small family of equivalent polynomials" and "gives us much more information about our graph than" the chromatic polynomial, characteristic polynomial, or minimal polynomial (p. 340). It connects graph theory to knot theory (Jones polynomial), statistical mechanics (Potts model, random cluster model), and coding theory. "During the process much less information is lost about the graph than in the case of the chromatic polynomial" (p. 340).

# Examples
**Example** (Exercise 1): $T_{C_n}(x,y) = y + x + x^2 + \cdots + x^{n-1}$ for the $n$-cycle.

**Example** (Exercise 2): $T_{I_k}(x,y) = x + y + y^2 + \cdots + y^{k-1}$ for the thick edge $I_k$.

# Relationships
## Builds Upon
- **rank-generating-polynomial** — $T_G(x,y) = S(G; x-1, y-1)$

## Enables
- **chromatic-polynomial-from-tutte** — $p_G(x) = (-1)^{r(G)} x^{k(G)} T_G(1-x, 0)$
- **flow-polynomial** — $q_G(k) = (-1)^{n(G)} T_G(0, 1-k)$
- **special-values-tutte-polynomial** — Enumerates spanning trees, forests, etc.
- **jones-polynomial** — Related for alternating links
- **partition-function-potts-model** — Simple transform of Tutte polynomial

## Related
- **universal-polynomial-of-graphs** — Lifts to a 5-variable polynomial
- **deletion-contraction** — The recursive structure

## Contrasts With
- **chromatic-polynomial** — The chromatic polynomial is a specialization $T_G(1-x, 0)$

# Common Errors
- **Error**: Applying deletion-contraction to loops incorrectly, computing $T_{G/e}$ separately.
  **Correction**: If $e$ is a loop, $G/e = G-e$, so $T_G = y T_{G-e}$ (no separate contraction needed).

# Common Confusions
- **Confusion**: Thinking the chromatic polynomial and Tutte polynomial are the same.
  **Clarification**: The chromatic polynomial is a specific evaluation of the Tutte polynomial at $y = 0$ (suitably normalized). The Tutte polynomial carries much more information.

# Source Reference
Chapter X: The Tutte Polynomial, Section X.1, pages 340-345. Equation (1). Also briefly introduced in Chapter V, p. 158.

# Verification Notes
- Definition source: Direct from equation (1), p. 343
- Confidence rationale: Explicit definition with formula; central object of Chapter X
- Uncertainties: None
- Cross-reference status: Verified; re-extracted from Ch X with Ch V content preserved
