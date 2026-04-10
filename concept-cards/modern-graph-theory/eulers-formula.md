---
concept: "Euler's Formula"
slug: eulers-formula
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - "Euler's polyhedron formula"
  - "$n - m + f = 2$"
prerequisites:
  - plane-graph
  - face
  - connected-graph
  - tree
extends: []
related:
  - girth
  - planar-graph
contrasts_with: []
answers_questions:
  - "What is Euler's formula for planar graphs?"
---

# Quick Definition

Euler's formula states that if a connected plane graph has $n$ vertices, $m$ edges, and $f$ faces, then $n - m + f = 2$.

# Core Definition

"**Theorem 15.** If a connected plane graph $G$ has $n$ vertices, $m$ edges, and $f$ faces, then $n - m + f = 2$" (Bollobás, p. 30). The proof uses induction on $f$: the base case $f = 1$ is a tree ($m = n - 1$); for $f > 1$, deleting a cycle edge merges two faces.

# Prerequisites

- **Plane graph** — Euler's formula applies to plane graphs
- **Face** — The formula counts faces
- **Connected graph** — The graph must be connected
- **Tree** — The base case is a tree (one face)

# Key Properties

1. $n - m + f = 2$ for any connected plane graph
2. For a disconnected graph with $k$ components: $n - m + f = k + 1$
3. Combined with face-edge bounds, yields $m \le 3n - 6$ for planar graphs
4. The quantity $n - m + f$ is a topological invariant (Euler characteristic)

# Construction / Recognition

The formula is verified by counting $n$, $m$, and $f$ for any connected plane graph.

# Context & Application

Euler's formula is one of the most beautiful results in mathematics, connecting combinatorics with topology. It underpins the edge bound for planar graphs (Theorem 16), the nonplanarity proofs for $K_5$ and $K_{3,3}$, and the classification of regular polyhedra.

# Examples

**Example** (p. 30): For a tree ($f = 1$): $n - (n-1) + 1 = 2$. Verified.

**Example** (p. 31): For $K_4$ drawn in the plane: $n = 4$, $m = 6$, $f = 4$; $4 - 6 + 4 = 2$.

# Relationships

## Builds Upon
- **Plane graph**, **Face**, **Connected graph**, **Tree**

## Enables
- Edge bound $m \le 3n - 6$ (Theorem 16)
- Nonplanarity proofs for $K_5$ and $K_{3,3}$
- **Girth**-based bounds on planar graph size

# Common Errors

- **Error**: Applying Euler's formula to disconnected graphs without adjustment
  **Correction**: For $k$ components, the formula is $n - m + f = k + 1$

# Common Confusions

- **Confusion**: Thinking Euler's formula holds for all graphs
  **Clarification**: It holds only for plane graphs (planar graphs with a specific embedding)

# Source Reference

Chapter I: Fundamentals, Section I.4, Theorem 15, page 30.

# Verification Notes

- Definition source: Direct theorem statement from p. 30
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
