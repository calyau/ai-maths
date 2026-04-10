---
concept: Circuit
slug: circuit
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
aliases:
  - closed trail
prerequisites:
  - graph
  - trail
extends:
  - trail
related:
  - cycle
  - euler-circuit
contrasts_with:
  - cycle
answers_questions:
  - "What is a circuit in a graph?"
  - "How does a circuit differ from a cycle?"
---

# Quick Definition

A circuit is a closed trail — a trail whose endvertices coincide. Unlike a cycle, a circuit may visit the same vertex more than once.

# Core Definition

"A trail whose endvertices coincide (a closed trail) is called a circuit. To be precise, a circuit is a closed trail without distinguished endvertices and direction" (Bollobás, p. 12). Two triangles sharing a single vertex give rise to precisely two circuits with six edges.

# Prerequisites

- **Graph** — Circuits exist within graphs
- **Trail** — A circuit is a closed trail

# Key Properties

1. All edges are distinct (inherited from trail)
2. The starting vertex equals the ending vertex
3. Vertices (other than the shared start/end) may repeat
4. A circuit has no distinguished starting vertex or direction
5. Every cycle is a circuit, but not every circuit is a cycle

# Construction / Recognition

1. Verify all edges are distinct
2. Verify the walk starts and ends at the same vertex

# Context & Application

Circuits are the natural context for Euler circuits. The distinction between circuit and cycle matters because an Euler circuit may pass through the same vertex multiple times while using each edge exactly once.

# Examples

**Example** (p. 12): Two triangles sharing a single vertex give rise to precisely two circuits with six edges. Each such circuit is not a cycle because a vertex is visited twice.

# Relationships

## Builds Upon
- **Trail** — A circuit is a closed trail

## Enables
- **Euler circuit** — A circuit using every edge of the graph

## Contrasts With
- **Cycle** — A cycle requires all vertices to be distinct

# Common Errors

- **Error**: Using "circuit" and "cycle" interchangeably
  **Correction**: A circuit allows repeated vertices; a cycle does not

# Common Confusions

- **Confusion**: Thinking every circuit is a cycle
  **Clarification**: A circuit that revisits a vertex is not a cycle; only circuits with all distinct internal vertices are cycles

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined with example
- Uncertainties: None
- Cross-reference status: Verified
