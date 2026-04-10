---
# === CORE IDENTIFICATION ===
concept: Simple Random Walk
slug: simple-random-walk

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
section: "IX.3 Hitting Times and Commute Times"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "SRW"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - random-walk-on-graph
extends:
  - random-walk-on-graph
related:
  - transition-probability-matrix
  - stationary-distribution
contrasts_with:
  - lazy-random-walk
  - weighted-graph-random-walk

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple random walk on a graph?"
  - "How does a simple random walk differ from a general random walk?"
---

# Quick Definition
A simple random walk (SRW) on a graph $G$ is a random walk where, at each step, we move to a uniformly random neighbour: the transition probability from $x$ to $y$ is $P_{xy} = 1/d(x)$ if $xy \in E(G)$, and $0$ otherwise.

# Core Definition
The simple random walk on a fixed graph $G$ with $n$ vertices and $m$ edges has transition probability matrix $P = (P_{xy})$, where $P_{xy} = 1/d(x)$ if $xy \in E(G)$. "In fact, by doing this, we lose no generality: all the results can be translated instantly to the case of general conductances" (Bollobás, p. 310).

# Prerequisites
- **Random walk on a graph** — The SRW is the simplest special case of a random walk on a graph

# Key Properties
1. Transition probability $P_{xy} = 1/d(x)$ for each neighbour $y$ of $x$
2. The stationary distribution is $\pi_x = d(x)/2m$
3. Satisfies detailed balance: $\pi_x P_{xy} = \pi_y P_{yx} = 1/2m$ for each edge $xy$
4. On a non-bipartite connected graph, converges to the stationary distribution
5. Each edge transmits probability $1/2m$ in either direction under the stationary distribution

# Construction / Recognition
## To Run a Simple Random Walk
1. Start at vertex $X_0 = x_0$
2. At vertex $x$, list all $d(x)$ neighbours
3. Choose one neighbour uniformly at random
4. Move to that neighbour; this is $X_{t+1}$
5. Repeat from step 2

# Context & Application
The SRW is the default random walk studied throughout Chapter IX. It corresponds to a random walk on the electrical network where each edge has conductance 1 (or equivalently, resistance 1). Despite its simplicity, "all the results can be translated instantly to the case of general conductances" (p. 310).

# Examples
**Example** (p. 315-316): On the graph $G_0$ with three vertices $s, t, u$ where $s$ is joined to $u$ by $k$ edges and $u$ is joined to $t$ by $\ell$ edges, the SRW starting at $u$ reaches $s$ before $t$ with probability $k/(k+\ell)$.

# Relationships
## Builds Upon
- **random-walk-on-graph** — SRW is the unweighted special case

## Enables
- **hitting-time** — Defined for SRW
- **commute-time** — Defined for SRW
- **fosters-theorem** — Stated for SRW
- **conductance-of-graph** — Related to SRW convergence

## Related
- **stationary-distribution** — SRW has $\pi_x = d(x)/2m$

## Contrasts With
- **lazy-random-walk** — At each step, stay with probability $1/2$
- **weighted-graph-random-walk** — Uses non-uniform edge weights

# Common Errors
- **Error**: Assuming the SRW always converges to its stationary distribution.
  **Correction**: On bipartite graphs, the SRW does not converge; it oscillates between the two parts.

# Common Confusions
- **Confusion**: Thinking SRW on a graph is less general than general Markov chains.
  **Clarification**: Any reversible finite Markov chain can be realized as a random walk on a weighted graph, and all SRW results extend to general conductances.

# Source Reference
Chapter IX: Random Walks on Graphs, Sections IX.2-IX.3, pages 303-310.

# Verification Notes
- Definition source: Direct from p. 310, with context from pp. 300-303
- Confidence rationale: Explicit definition and notation established in source
- Uncertainties: None
- Cross-reference status: Verified
