---
concept: Markov Chain
slug: markov-chain
category: random-walks
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 302
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "finite Markov chain"
  - "discrete-time Markov chain"
prerequisites: []
extends: []
related:
  - random-walk-on-graph
  - transition-probability-matrix
  - stationary-distribution
contrasts_with: []
answers_questions:
  - "What is a random walk on a graph?"
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
A (discrete-time) Markov chain on a finite or countable set $V$ is a sequence of random variables $X_0, X_1, \ldots$ such that the probability of $X_{t+1} = x_{t+1}$ given the entire past depends only on $x_t$ and $x_{t+1}$ (the Markov property).

# Core Definition
"A (discrete-time) Markov chain on a finite or countable set $V$ of states is a sequence of random variables $X_0, X_1, \ldots$ taking values in $V$ such that for all $x_0, \ldots, x_{t+1} \in V$, the probability of $X_{t+1} = x_{t+1}$, conditional on $X_0 = x_0, \ldots, X_t = x_t$, depends only on $x_t$ and $x_{t+1}$" (Bollobás, p. 302).

# Prerequisites
Foundational concept.

# Key Properties
1. Markov property: the future depends on the past only through the present
2. Finite Markov chains are random walks on weighted directed graphs with loops
3. Reversible finite Markov chains are random walks on weighted undirected graphs
4. Ergodic chains have unique stationary distributions

# Relationships
## Related
- **random-walk-on-graph** — Random walks are Markov chains
- **transition-probability-matrix** — Encodes the chain
- **stationary-distribution** — Long-run distribution

# Source Reference
Chapter IX, Section IX.2, page 302.

# Verification Notes
- Definition source: Direct from p. 302
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
