---
concept: "Kirchhoff's Potential Law"
slug: kirchhoffs-potential-law
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
  - "Kirchhoff's voltage law"
  - KVL
prerequisites:
  - electrical-network
  - cycle
extends: []
related:
  - kirchhoffs-current-law
  - ohms-law
contrasts_with:
  - kirchhoffs-current-law
answers_questions:
  - "What is Kirchhoff's potential law?"
---

# Quick Definition

Kirchhoff's potential (voltage) law states that the potential differences around any cycle sum to zero: $p_{x_1 x_2} + p_{x_2 x_3} + \cdots + p_{x_k x_1} = 0$.

# Core Definition

"Kirchhoff's potential (or voltage) law states that the potential differences round any cycle $x_1 x_2 \cdots x_k$ sum to 0: $p_{x_1 x_2} + p_{x_2 x_3} + \cdots + p_{x_{k-1} x_k} + p_{x_k x_1} = 0$" (Bollobás, p. 47). Equivalently, one can assign absolute potentials $V_a, V_b, \ldots$ to vertices so that $p_{ab} = V_a - V_b$.

# Prerequisites

- **Electrical network** — The law governs networks
- **Cycle** — The law concerns potential differences around cycles

# Key Properties

1. Potential differences around any cycle sum to zero
2. Equivalent to the existence of well-defined vertex potentials
3. In matrix form: $C^t \mathbf{p} = \mathbf{0}$ where $C$ is the fundamental cycle matrix
4. If the network is connected, one potential can be fixed arbitrarily

# Construction / Recognition

Assign potentials to vertices; verify that for each edge $ab$, $p_{ab} = V_a - V_b$.

# Context & Application

Together with Kirchhoff's current law and Ohm's law, this completely determines the electrical behaviour of a network. The potential law can be rewritten as a constraint on currents using Ohm's law.

# Examples

**Example** (pp. 47-48): In the network of Fig. II.1, potentials $V_t = 0$, $V_a = e$, $V_b = 2(1-e)$, $V_s = 6e + 5f$ satisfy the potential law.

# Relationships

## Builds Upon
- **Electrical network**, **Cycle**

## Related
- **Kirchhoff's current law** — The other Kirchhoff law
- **Ohm's law** — Relates potential to current

## Contrasts With
- **Kirchhoff's current law** — Voltage law concerns cycles; current law concerns vertices

# Common Errors

- **Error**: Applying the potential law to a path instead of a cycle
  **Correction**: The law applies only to closed loops (cycles)

# Common Confusions

- **Confusion**: Thinking absolute potentials are intrinsic
  **Clarification**: Only potential differences are physically meaningful; one potential can be set arbitrarily

# Source Reference

Chapter II: Electrical Networks, Section II.1, page 47.

# Verification Notes

- Definition source: Direct from p. 47
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
