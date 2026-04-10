---
concept: Trail
slug: trail
category: paths-and-cycles
subcategory: walks-and-trails
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
  - walk
extends:
  - walk
related:
  - path
  - circuit
  - euler-trail
contrasts_with:
  - path
  - walk
answers_questions:
  - "What is a trail in a graph?"
---

# Quick Definition

A trail is a walk in which all edges are distinct. Vertices may be repeated, but no edge is traversed more than once.

# Core Definition

"This walk $W$ is called a trail if all its edges are distinct. Note that a path is a walk with distinct vertices" (Bollobás, p. 12). A trail whose endvertices coincide (a closed trail) is called a circuit.

# Prerequisites

- **Graph** — Trails exist within graphs
- **Walk** — A trail is a walk with an additional constraint

# Key Properties

1. All edges are distinct; vertices may repeat
2. Every path is a trail, but not every trail is a path
3. A closed trail (one where start = end) is a circuit
4. An Euler trail is a trail using every edge of the graph

# Construction / Recognition

A trail is recognized by verifying that no edge appears more than once in the sequence.

# Context & Application

Trails are the natural generalization of paths when edge-distinctness (rather than vertex-distinctness) is the requirement. Euler trails and circuits are defined as trails, and the theory of Euler circuits is fundamentally about trails.

# Examples

**Example** (p. 12): A closed trail in a triangle $x_1 x_2 x_3 x_1$ is both a circuit and a cycle. A figure-eight traversal through two triangles sharing a vertex gives a circuit that is not a cycle.

# Relationships

## Builds Upon
- **Walk** — A trail is a walk with distinct edges

## Enables
- **Circuit** — A closed trail
- **Euler trail** — A trail using all edges

## Contrasts With
- **Path** — A path requires distinct vertices, not just distinct edges
- **Walk** — A walk allows repeated edges

# Common Errors

- **Error**: Assuming a trail must have distinct vertices
  **Correction**: A trail requires distinct edges only; vertices may repeat

# Common Confusions

- **Confusion**: Confusing "trail" with "path"
  **Clarification**: Trail = distinct edges; path = distinct vertices (which implies distinct edges)

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
