---
concept: Random Walk on a Weighted Graph
slug: weighted-graph-random-walk
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
aliases: []
prerequisites:
  - random-walk-on-graph
extends:
  - random-walk-on-graph
related:
  - random-walk-on-electrical-network
  - detailed-balance-equations
contrasts_with:
  - simple-random-walk
answers_questions:
  - "What is a random walk on a graph?"
---

# Quick Definition
A random walk on a weighted graph $(G, a)$ moves from vertex $x$ to neighbour $y$ with probability $P_{xy} = a_{xy}/A_x$, where $a_{xy}$ is the edge weight and $A_x = \sum_{z \in \Gamma(x)} a_{xz}$.

# Core Definition
"Given a weighted graph $(G, a)$, for every vertex $x \in V(G)$, let $A_x = \sum_{y \in \Gamma(x)} a_{xy}$, and for $x, y \in V(G)$, define $P_{xy} = a_{xy}/A_x$ if $x$ is joined to $y$, $0$ otherwise" (Bollobás, p. 302). "A random walk defined by a weighted graph is a Markov chain on $V = V(G)$ with transition probability matrix $(P_{xy})$."

# Prerequisites
- **Random walk on a graph** — Weighted walks generalize the basic definition

# Key Properties
1. Each edge weight $a_{xy} > 0$ determines the transition probabilities
2. Every reversible finite Markov chain is an RW on a weighted graph (with loops)
3. On multigraphs: choose an edge at random (proportional to weight), then traverse it
4. Satisfies detailed balance with $\pi_x = A_x / \sum_z A_z$

# Context & Application
The weighted graph formulation unifies random walks and reversible Markov chains. "At the first sight, random walks on graphs seem to be rather special finite Markov chains, but this is not the case: finite Markov chains are just random walks on weighted directed graphs" (p. 300).

# Relationships
## Extends
- **random-walk-on-graph**

## Related
- **random-walk-on-electrical-network** — Special case with conductance weights

## Contrasts With
- **simple-random-walk** — Uniform weights

# Source Reference
Chapter IX, Section IX.2, pages 302-303.

# Verification Notes
- Definition source: Direct from p. 302
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
