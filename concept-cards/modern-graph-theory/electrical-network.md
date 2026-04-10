---
concept: Electrical Network
slug: electrical-network
category: electrical-networks
subcategory: network-basics
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.1 Graphs and Electrical Networks"
extraction_confidence: high
aliases:
  - resistor network
prerequisites:
  - graph
  - multigraph
  - directed-graph
  - spanning-tree
extends: []
related:
  - ohms-law
  - kirchhoffs-current-law
  - kirchhoffs-potential-law
  - resistance-and-conductance
contrasts_with: []
answers_questions:
  - "How is an electrical network modelled as a graph?"
---

# Quick Definition

An electrical network is a graph (or multigraph) in which each edge is assigned a resistance. Currents and potentials in the network are governed by Ohm's law and Kirchhoff's laws.

# Core Definition

"A simple electrical network can be regarded as a graph in which each edge $e_i$ has been assigned a real number $r_i$, called its resistance" (Bollobás, p. 46). Edges are oriented to define current direction: $w_{ab} = -w_{ba}$ and $p_{ab} = -p_{ba}$. The fundamental problem is: given a current entering at source $s$ and leaving at sink $t$, find all edge currents and potential differences.

# Prerequisites

- **Graph** — The network is modelled as a graph
- **Multigraph** — Simplifications may require multiple edges
- **Directed graph** — Edges are oriented for current direction
- **Spanning tree** — Key to solving the network equations

# Key Properties

1. Each edge has a resistance $r_i$ (or conductance $1/r_i$)
2. Current $w_i$ and potential difference $p_i$ are related by Ohm's law: $w_i = p_i / r_i$
3. Kirchhoff's laws constrain the currents and potentials
4. The total resistance between source $s$ and sink $t$ is $r = p/w$
5. Solutions are unique (by the uniqueness argument on p. 49)

# Construction / Recognition

An electrical network is a weighted graph where weights represent resistances. The problem is solved by applying Kirchhoff's laws and Ohm's law.

# Context & Application

Electrical networks connect graph theory with physics. Bollobás notes that "virtually the only concept to be used is that of a spanning tree" (p. 46). The chapter develops the theory to solve current distribution problems and connects it to squared rectangles and algebraic graph theory.

# Examples

**Example** (pp. 47-48): Fig. II.1 shows a network with 5 resistors. The total resistance from $s$ to $t$ is computed to be $62/21$ by applying Kirchhoff's and Ohm's laws.

# Relationships

## Builds Upon
- **Graph**, **Multigraph**, **Directed graph**, **Spanning tree**

## Enables
- **Kirchhoff's theorem** — Current distribution via spanning trees
- **Squared rectangle** — Connection to network theory
- **Matrix-tree theorem** — Counting spanning trees via the Laplacian

## Related
- **Ohm's law**, **Kirchhoff's current law**, **Kirchhoff's potential law**

# Common Errors

- **Error**: Forgetting that edge orientation is arbitrary
  **Correction**: The orientation is a convention; negative current means current flows opposite to the chosen direction

# Common Confusions

- **Confusion**: Thinking network theory requires physics knowledge
  **Clarification**: The mathematical formulation uses only Kirchhoff's laws and linear algebra

# Source Reference

Chapter II: Electrical Networks, Section II.1, pages 46-53.

# Verification Notes

- Definition source: Direct from p. 46
- Confidence rationale: Explicitly described
- Uncertainties: None
- Cross-reference status: Verified
