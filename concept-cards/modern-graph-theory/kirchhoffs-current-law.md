---
concept: "Kirchhoff's Current Law"
slug: kirchhoffs-current-law
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
  - KCL
  - current conservation
prerequisites:
  - electrical-network
extends: []
related:
  - kirchhoffs-potential-law
  - ohms-law
contrasts_with:
  - kirchhoffs-potential-law
answers_questions:
  - "What is Kirchhoff's current law?"
---

# Quick Definition

Kirchhoff's current law states that the total current outflow from any vertex is zero: $w_{ab} + w_{ac} + \cdots + w_{au} + w_{a\infty} = 0$, where $w_{a\infty}$ is the current leaving the network at $a$.

# Core Definition

"Kirchhoff's current law postulates that the total current outflow from any point is 0: $w_{ab} + w_{ac} + \cdots + w_{au} + w_{a\infty} = 0$" (Bollobás, p. 47). For vertices not connected to external points, $w_{ab} + w_{ac} + \cdots + w_{au} = 0$. In matrix form: $B\mathbf{w} = \mathbf{0}$.

# Prerequisites

- **Electrical network** — The law governs networks

# Key Properties

1. Conservation of current at each vertex
2. For internal vertices: current in = current out
3. External vertices have $w_{a\infty} \neq 0$ (sources and sinks)
4. In matrix form: $B\mathbf{w} = \mathbf{0}$ where $B$ is the incidence matrix
5. The current vector $\mathbf{w}$ lies in the cycle space

# Construction / Recognition

At each vertex, verify that the algebraic sum of all currents (including external) equals zero.

# Context & Application

Kirchhoff's current law, together with Ohm's law and the potential law, completely determines all currents in a network. The current law is equivalent to saying the current vector belongs to the cycle space of the graph.

# Examples

**Example** (pp. 47-48): In Fig. II.1, if unit current enters at $s$ and exits at $t$, then at each internal vertex the currents sum to zero, determining the values $e$ and $f$.

# Relationships

## Builds Upon
- **Electrical network**

## Related
- **Kirchhoff's potential law** — The companion law
- **Ohm's law** — Relates current to potential

## Contrasts With
- **Kirchhoff's potential law** — Current law concerns vertices; potential law concerns cycles

# Common Errors

- **Error**: Forgetting to account for external current $w_{a\infty}$
  **Correction**: At source and sink vertices, external current must be included

# Common Confusions

- **Confusion**: Thinking the current law only applies to interior vertices
  **Clarification**: It applies to all vertices; at external vertices, the external current term $w_{a\infty}$ accounts for current entering/leaving the network

# Source Reference

Chapter II: Electrical Networks, Section II.1, page 47.

# Verification Notes

- Definition source: Direct from p. 47
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
