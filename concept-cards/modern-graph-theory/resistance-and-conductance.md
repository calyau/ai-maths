---
concept: Resistance and Conductance
slug: resistance-and-conductance
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
  - resistance
  - conductance
  - total resistance
prerequisites:
  - electrical-network
  - ohms-law
extends: []
related:
  - series-and-parallel-connection
  - star-triangle-transformation
contrasts_with: []
answers_questions:
  - "What is resistance and conductance in a graph-theoretic setting?"
---

# Quick Definition

Resistance $r$ of an edge is the ratio of potential difference to current ($r = p/w$). Conductance $c = 1/r$ is its reciprocal. The total resistance of a network is $r = p/w$ where $p$ is the potential difference between source and sink.

# Core Definition

Each edge $e_i$ has resistance $r_i$, and Ohm's law gives $w_i = p_i / r_i$ (Bollobás, p. 46). The conductance is the reciprocal of resistance; "the conductance of an edge of resistance 1 ohm is 1 mho" (p. 49). Key limiting cases: resistance 0 means the vertices are "shorted" ($V_a = V_b$); conductance 0 means the edge is "cut" (no current flows).

# Prerequisites

- **Electrical network** — Resistance is a network property
- **Ohm's law** — Defines the relationship $w = p/r$

# Key Properties

1. $c = 1/r$ — conductance is the reciprocal of resistance
2. For series connection: resistances add ($r = r_1 + r_2$)
3. For parallel connection: conductances add ($1/r = 1/r_1 + 1/r_2$)
4. Resistance 0 = short circuit ($V_a = V_b$)
5. Conductance 0 = open circuit (edge cut)
6. Increasing resistance does not decrease total resistance

# Construction / Recognition

Resistance is assigned to each edge; total resistance is computed from the network equations.

# Context & Application

Resistance and conductance are dual concepts. Bollobás notes that "conductances are just as natural as the resistances themselves, and indeed are more convenient in our presentation" (p. 49). The weighted matrix-tree theorem uses conductances as edge weights.

# Examples

**Example** (pp. 49-50): Two resistors $r_1, r_2$ in series: $r = r_1 + r_2$. In parallel: $r = r_1 r_2/(r_1 + r_2)$.

**Example** (p. 50): The total resistance of a cube (unit resistance per edge) across an edge is $7/12$.

# Relationships

## Builds Upon
- **Electrical network**, **Ohm's law**

## Enables
- **Series and parallel connection** — Combining resistances
- **Star-triangle transformation** — Network simplification
- **Matrix-tree theorem** — Uses conductances as weights

# Common Errors

- **Error**: Adding resistances for parallel connections
  **Correction**: For parallel: conductances add, i.e., $1/r = 1/r_1 + 1/r_2$

# Common Confusions

- **Confusion**: Confusing 0 resistance with 0 conductance
  **Clarification**: 0 resistance = short circuit (infinite conductance); 0 conductance = open circuit (infinite resistance)

# Source Reference

Chapter II: Electrical Networks, Section II.1, pages 46-50.

# Verification Notes

- Definition source: Synthesized from pp. 46-50
- Confidence rationale: Explicitly discussed with examples
- Uncertainties: None
- Cross-reference status: Verified
