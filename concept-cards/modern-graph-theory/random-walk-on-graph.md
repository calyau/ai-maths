---
# === CORE IDENTIFICATION ===
concept: Random Walk on a Graph
slug: random-walk-on-graph

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
pdf_page: 300
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "RW on a graph"
  - "random walk"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - simple-random-walk
  - transition-probability-matrix
  - weighted-graph-random-walk
  - markov-chain
contrasts_with:
  - deterministic-walk

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a random walk on a graph?"
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
A random walk on a graph is a sequence of random variables $X_0, X_1, \ldots$ taking values in the vertex set, where each step moves to a neighbouring vertex chosen according to specified transition probabilities.

# Core Definition
A random walk on a graph is "precisely what its name says: a walk $X_0 X_1 \cdots$ obtained in a certain random fashion." Starting at $X_0$, the next vertex $X_1$ is chosen at random from among the neighbours of $X_0$, then $X_2$ is a random neighbour of $X_1$, and so on. More generally, on a weighted graph $(G, a)$ with positive weights $a_{xy}$ on edges, the transition probability from $x$ to $y$ is $P_{xy} = a_{xy}/A_x$ where $A_x = \sum_{y \in \Gamma(x)} a_{xy}$ (Bollobás, p. 300-303).

# Prerequisites
This is a foundational concept with no prerequisites within this source, though familiarity with basic graph theory (vertices, edges, neighbours) is assumed.

# Key Properties
1. The walk is a sequence of random variables $X_0, X_1, \ldots$ taking values in $V(G)$
2. The Markov property holds: the next state depends only on the current state
3. The transition probabilities are determined by the graph structure and edge weights
4. Finite Markov chains are precisely random walks on weighted directed graphs with loops
5. The walk is specified by an initial distribution and a transition probability matrix

# Construction / Recognition
## To Define a Random Walk on a Graph
1. Start with a graph $G$ (possibly weighted)
2. For each vertex $x$, compute the total weight $A_x = \sum_{y \in \Gamma(x)} a_{xy}$
3. Set the transition probability $P_{xy} = a_{xy}/A_x$ for each neighbour $y$ of $x$
4. Choose an initial vertex $X_0 = x_0$ (or initial distribution)
5. At each step, move from the current vertex to a neighbour according to the probabilities $P_{xy}$

# Context & Application
Random walks on graphs unify two important areas: combinatorics and probability theory. They are precisely the reversible finite Markov chains (when defined on weighted graphs), making them fundamental to both pure mathematics and applications. The study "really took off only in the last two decades" (as of 1998) due to the connection with electrical networks, combinatorial arguments, spectral methods, and harmonic analysis.

**Key applications:**
- Modelling diffusion and mixing processes
- Algorithmic graph exploration
- Estimating network properties via Monte Carlo methods
- Generating approximately random elements of large combinatorial structures

# Examples
**Example 1** (p. 300): The simplest form is a simple random walk on an unweighted graph: starting at $X_0$, each subsequent vertex is chosen uniformly at random from the neighbours of the current vertex.

**Example 2** (p. 302-303): On a weighted multigraph $(G, a)$, if at vertex $x$, one chooses an edge incident with $x$ at random according to edge weights, and traverses that edge to the other endpoint.

# Relationships
## Builds Upon
No internal prerequisites; builds on basic graph theory from earlier chapters.

## Enables
- **simple-random-walk** — The unweighted special case
- **hitting-time** — Key parameter of random walks
- **stationary-distribution** — Long-run behaviour of walks
- **escape-probability** — Probability of reaching one vertex before another

## Related
- **transition-probability-matrix** — Encodes the walk's dynamics
- **markov-chain** — Random walks are finite Markov chains

## Contrasts With
- Deterministic walks follow fixed rules rather than random choices

# Common Errors
- **Error**: Confusing a random walk on a graph with a random walk on $\mathbb{Z}$ (the classical drunkard's walk).
  **Correction**: A random walk on a graph is defined on any graph; the classical drunkard's walk is the special case on the path graph or lattice $\mathbb{Z}^d$.

# Common Confusions
- **Confusion**: Believing that random walks on graphs are "rather special finite Markov chains."
  **Clarification**: As Bollobás notes, "this is not the case: finite Markov chains are just random walks on weighted directed graphs, with loops allowed" (p. 300).

# Source Reference
Chapter IX: Random Walks on Graphs, introductory discussion, pages 295-303.

# Verification Notes
- Definition source: Direct from pp. 300-303
- Confidence rationale: Explicit definition and extensive discussion in source
- Uncertainties: None
- Cross-reference status: Verified against chapter structure
