---
concept: "Ohm's Law"
slug: ohms-law
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
aliases: []
prerequisites:
  - electrical-network
extends: []
related:
  - kirchhoffs-potential-law
  - kirchhoffs-current-law
  - resistance-and-conductance
contrasts_with: []
answers_questions:
  - "What is Ohm's law in the context of graph theory?"
---

# Quick Definition

Ohm's law states that the current $w_i$ through an edge of resistance $r_i$ with potential difference $p_i$ satisfies $w_i = p_i / r_i$.

# Core Definition

"If there is a potential difference $p_i$ between the endvertices of $e_i$, say $a_i$ and $b_i$, then an electrical current $w_i$ will flow in the edge $e_i$ from $a_i$ to $b_i$ according to Ohm's law: $w_i = p_i / r_i$" (Bollobás, p. 46).

# Prerequisites

- **Electrical network** — Ohm's law applies within electrical networks

# Key Properties

1. $w_i = p_i / r_i$ relates current, potential difference, and resistance
2. The total resistance $r = p/w$ for the entire network
3. If resistance is 0, the endvertices must have equal potential (short circuit)
4. If conductance is 0, the edge carries no current (cut)

# Construction / Recognition

For each edge, the current is determined by the potential difference and resistance.

# Context & Application

Ohm's law, together with Kirchhoff's laws, completely determines all currents and potentials in a network. The three laws together can be expressed in matrix form (Section II.3).

# Examples

**Example** (pp. 47-48): In Fig. II.1, Ohm's law gives $V_a = 1 \cdot e = e$ and $V_b = 2(1-e)$ for the computed current values.

# Relationships

## Builds Upon
- **Electrical network**

## Related
- **Kirchhoff's potential law**, **Kirchhoff's current law**, **Resistance and conductance**

# Common Errors

- **Error**: Confusing resistance and conductance in the formula
  **Correction**: $w = p/r = p \cdot c$ where $c = 1/r$ is the conductance

# Common Confusions

- **Confusion**: Thinking Ohm's law alone determines all currents
  **Clarification**: Ohm's law must be combined with Kirchhoff's laws to solve a network

# Source Reference

Chapter II: Electrical Networks, Section II.1, page 46.

# Verification Notes

- Definition source: Direct from p. 46
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
