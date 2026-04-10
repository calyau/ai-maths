---
concept: Hamilton Path
slug: hamilton-path
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - Hamiltonian path
prerequisites:
  - graph
  - path
extends:
  - path
related:
  - hamilton-cycle
contrasts_with:
  - euler-trail
answers_questions:
  - "What is a Hamilton path?"
---

# Quick Definition

A Hamilton path is a path containing all vertices of a graph. It visits every vertex exactly once without returning to the start.

# Core Definition

"A Hamilton path of a graph is a path containing all the vertices of the graph" (Bollobás, p. 23). For even $n \ge 2$, $K_n$ decomposes into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton paths (Theorem 11).

# Prerequisites

- **Graph** — Hamilton paths exist within graphs
- **Path** — A Hamilton path is a special path

# Key Properties

1. Visits every vertex exactly once
2. Has $n - 1$ edges for a graph of order $n$
3. For even $n$, $K_n$ decomposes into edge-disjoint Hamilton paths
4. Deleting a vertex from a Hamilton cycle yields a Hamilton path

# Construction / Recognition

Like Hamilton cycles, no efficient general algorithm is known for finding Hamilton paths.

# Context & Application

Hamilton paths arise in sequencing problems and the non-cyclic version of the travelling salesman problem.

# Examples

**Example** (p. 24): Fig. I.13 shows three edge-disjoint Hamilton paths in $K_6$.

**Example** (Theorem 11): For even $n \ge 2$, $K_n$ decomposes into $\frac{1}{2}(n-1)$ Hamilton paths.

# Relationships

## Builds Upon
- **Path** — A Hamilton path is a path through all vertices

## Enables
- **Hamilton cycle** — Extending Hamilton paths to Hamilton cycles in $K_n$

## Contrasts With
- **Euler trail** — An Euler trail traverses all edges; a Hamilton path visits all vertices

# Common Errors

- **Error**: Assuming a Hamilton path must be closed
  **Correction**: A Hamilton path is open (has two distinct endpoints); a closed version is a Hamilton cycle

# Common Confusions

- **Confusion**: Confusing Hamilton path with Euler trail
  **Clarification**: Hamilton path = all vertices; Euler trail = all edges

# Source Reference

Chapter I: Fundamentals, Section I.3, pages 23-24; Theorem 11, page 24.

# Verification Notes

- Definition source: Direct from p. 23
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
