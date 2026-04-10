---
# === CORE IDENTIFICATION ===
concept: Monotone Increasing Property
slug: monotone-increasing-property

# === CLASSIFICATION ===
category: random-graphs
subcategory: property-types
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 241
section: "VII.3 Almost Determined Variables—The Use of the Variance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - increasing property
  - monotone property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
extends: []
related:
  - threshold-function
  - convex-property
  - hitting-time
contrasts_with:
  - convex-property

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a monotone increasing property of graphs?"
---

# Quick Definition

A property $Q$ is monotone increasing if it is preserved under the addition of edges: if $G \in Q$, $G \subset H$, and $V(G) = V(H)$, then $H \in Q$.

# Core Definition

A property $Q$ of graphs is monotone increasing if $Q$ is invariant under the addition of edges: if $G \in Q$, $G \subset H$ and $V(G) = V(H)$ then $H \in Q$. Monotone decreasing is defined analogously for edge deletion. Being connected, being Hamiltonian, and containing $K_s$ are monotone increasing; being at most 3-connected is monotone decreasing; containing an induced 6-cycle is neither (Bollobás, p. 241).

# Prerequisites

- **G(n,p) model** -- Context for studying properties

# Key Properties

1. $\mathbb{P}_p(Q)$ is an increasing function of $p$ for monotone increasing $Q$
2. $\mathbb{P}_M(Q)$ is an increasing function of $M$ for monotone increasing $Q$
3. Every monotone increasing property has threshold functions
4. Monotone increasing properties are convex

# Construction / Recognition

## Examples of Monotone Increasing Properties
- Being connected
- Being Hamiltonian
- Containing a copy of a fixed graph $F$
- Having minimum degree at least $k$
- Being $k$-connected

# Context & Application

Monotone properties are the natural setting for threshold functions and hitting times. The Erdos-Renyi discovery that "all the standard properties of graphs arise rather suddenly" applies specifically to monotone properties.

# Examples

**Example** (p. 241): Being connected is monotone increasing. Being at most 3-connected is monotone decreasing. Containing an induced 6-cycle is neither.

# Relationships

## Builds Upon
- **G(n,p) model** -- Context

## Enables
- **Threshold function** -- Defined for monotone properties
- **Hitting time** -- First appearance in a graph process

## Related
- **Convex property** -- Monotone implies convex

## Contrasts With
- **Convex property** -- Convex is a weaker condition

# Common Errors

- **Error**: Assuming $\mathbb{P}_p(Q)$ is increasing for all properties
  **Correction**: Only for monotone properties; non-monotone properties may have non-monotone probability curves

# Common Confusions

- **Confusion**: Thinking "monotone increasing" means the graph must grow
  **Clarification**: It means the property is preserved when edges are added, not that the vertex set changes

# Source Reference

Chapter VII: Random Graphs, Section VII.3, page 241.

# Verification Notes

- Definition source: Direct from p. 241
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
