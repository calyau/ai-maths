---
concept: Principle of Superposition
slug: principle-of-superposition
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
  - superposition principle
prerequisites:
  - electrical-network
  - kirchhoffs-current-law
  - kirchhoffs-potential-law
extends: []
related:
  - ohms-law
contrasts_with: []
answers_questions:
  - "What is the principle of superposition for electrical networks?"
---

# Quick Definition

The principle of superposition states that any combination of solutions to Kirchhoff's equations is again a solution. This implies that multi-source problems can be decomposed into single-source problems, and that solutions are unique.

# Core Definition

"Kirchhoff's equations are linear and homogeneous in all currents and potential differences. This implies the so-called principle of superposition: any combination of solutions is again a solution" (Bollobás, p. 49). Uniqueness follows: "the difference of two distinct solutions is a flow in which no current enters or leaves the network at any point," which leads to a contradiction.

# Prerequisites

- **Electrical network** — The principle applies to networks
- **Kirchhoff's current law** — One of the governing equations
- **Kirchhoff's potential law** — The other governing equation

# Key Properties

1. Linearity of Kirchhoff's equations enables superposition
2. Multi-source problems decompose into single-source problems
3. Solutions are unique (proved by contradiction on p. 49)
4. The uniqueness proof uses: no flow with no external current can have nonzero edge currents

# Construction / Recognition

To solve a multi-source problem: solve each single-source subproblem separately and add the solutions.

# Context & Application

Superposition simplifies complex network problems by decomposing them. The uniqueness of solutions guarantees that the decomposition gives the correct answer.

# Examples

**Example** (p. 49): The uniqueness proof: if two solutions differ, their difference has no external sources, yet would require positive current around a circuit, contradicting the potential law.

# Relationships

## Builds Upon
- **Electrical network**, **Kirchhoff's current law**, **Kirchhoff's potential law**

## Enables
- Decomposition of complex network problems
- Uniqueness of solutions

# Common Errors

- **Error**: Applying superposition to nonlinear circuit elements
  **Correction**: Superposition only works because Kirchhoff's equations are linear

# Common Confusions

- **Confusion**: Thinking superposition means "any flow is a solution"
  **Clarification**: Superposition means any linear combination of solutions is a solution, not that arbitrary flows satisfy the equations

# Source Reference

Chapter II: Electrical Networks, Section II.1, page 49.

# Verification Notes

- Definition source: Direct from p. 49
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
