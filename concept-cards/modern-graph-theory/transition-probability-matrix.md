---
# === CORE IDENTIFICATION ===
concept: Transition Probability Matrix
slug: transition-probability-matrix

# === CLASSIFICATION ===
category: random-walks
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 302
section: "IX.2 Electrical Networks and Random Walks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "stochastic matrix"
  - "transition matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-walk-on-graph
extends: []
related:
  - stationary-distribution
  - mixing-rate
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are random walk dynamics encoded in a matrix?"
---

# Quick Definition
The transition probability matrix $P = (P_{xy})$ of a random walk on a weighted graph $(G, a)$ is the $n \times n$ matrix where $P_{xy} = a_{xy}/A_x$ if $x$ is joined to $y$, and $0$ otherwise.

# Core Definition
Given a weighted graph $(G, a)$, for every vertex $x \in V(G)$, let $A_x = \sum_{y \in \Gamma(x)} a_{xy}$, and define $P_{xy} = a_{xy}/A_x$ if $x$ is joined to $y$ by an edge or loop, and $P_{xy} = 0$ otherwise. "Thus $P = (P_{xy})$ is an $n \times n$ matrix with non-negative entries in which each row-sum is 1" (Bollobás, p. 302).

# Prerequisites
- **Random walk on a graph** — The transition matrix encodes the walk's dynamics

# Key Properties
1. Non-negative entries: $P_{xy} \geq 0$ for all $x, y$
2. Row-stochastic: $\sum_y P_{xy} = 1$ for every $x$
3. For a simple random walk: $P_{xy} = 1/d(x)$ if $xy \in E(G)$
4. For a regular graph: $P = A/d$ where $A$ is the adjacency matrix
5. Powers $P^t$ give $t$-step transition probabilities

# Construction / Recognition
1. Start with weighted graph $(G, a)$
2. For each vertex $x$, compute $A_x = \sum_{y \in \Gamma(x)} a_{xy}$
3. Set $P_{xy} = a_{xy}/A_x$ for neighbours, $0$ otherwise
4. Verify all row sums equal $1$

# Context & Application
The transition probability matrix is the fundamental object encoding a random walk. The distribution after $t$ steps from initial distribution $\mathbf{p}$ is $\mathbf{p}P^t$. The eigenvalues of $P$ determine the mixing rate and convergence properties.

# Examples
**Example** (p. 302): For a simple graph, $P_{xy} = 1/d(x)$ when $xy \in E(G)$, and $P_{xy} = 0$ otherwise.

# Relationships
## Builds Upon
- **random-walk-on-graph** — Defines the walk

## Enables
- **stationary-distribution** — Found as left eigenvector of $P$
- **mixing-rate** — Determined by eigenvalues of $P$

## Related
- **simple-random-walk** — Has $P = D^{-1}A$ where $D$ is the degree matrix

# Common Errors
- **Error**: Confusing row-stochastic with column-stochastic matrices.
  **Correction**: In this convention, rows sum to 1; the distribution evolves as $\mathbf{p}_{t+1} = \mathbf{p}_t P$.

# Common Confusions
- **Confusion**: Thinking $P$ must be symmetric.
  **Clarification**: $P$ is generally not symmetric. For a simple random walk, $P_{xy} = 1/d(x)$ while $P_{yx} = 1/d(y)$, which differ unless $d(x) = d(y)$.

# Source Reference
Chapter IX: Random Walks on Graphs, Section IX.2, pages 302-303.

# Verification Notes
- Definition source: Direct from p. 302
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
