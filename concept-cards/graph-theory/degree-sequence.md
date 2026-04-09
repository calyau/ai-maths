---
concept: Degree Sequence
slug: degree-sequence
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: high
aliases:
  - "degree sequence of a graph"
prerequisites:
  - graph
  - vertex-degree
extends: []
related:
  - chvatals-theorem
  - hamiltonian-sequence
contrasts_with: []
answers_questions:
  - "What is the degree sequence of a graph?"
  - "How does the degree sequence relate to Hamiltonicity?"
---

# Quick Definition
If G has n vertices with degrees d1 <= d2 <= ... <= dn, the n-tuple (d1, ..., dn) is the degree sequence of G.

# Core Definition
If G is a graph with n vertices and degrees d1 <= ... <= dn, then the n-tuple (d1, ..., dn) is called the **degree sequence** of G. Note that this sequence is unique, even though G has several vertex enumerations giving rise to it (Diestel, p. 289).

# Prerequisites
- **Graph** — degree sequences are properties of graphs
- **Vertex degree** — the components of the sequence

# Key Properties
1. Arranged in non-decreasing order
2. Unique for each graph (up to the ordering convention)
3. The degree sequence determines whether a graph is Hamiltonian via Chvatal's theorem
4. A sequence is called Hamiltonian if every graph with a pointwise greater degree sequence is Hamiltonian
5. The degree sequence does not determine the graph uniquely (many graphs share a degree sequence)

# Construction / Recognition
## To Compute the Degree Sequence
1. For each vertex v, compute d(v)
2. Sort the degrees in non-decreasing order
3. The sorted tuple is the degree sequence

# Context & Application
Degree sequences provide a compact summary of a graph's structure. Chvatal's theorem (10.2.1) characterizes exactly which degree sequences force Hamiltonicity, subsuming Dirac's and Ore's theorems.

# Examples
**Example**: K4 has degree sequence (3,3,3,3). The path P4 has degree sequence (1,2,2,1). The cycle C5 has degree sequence (2,2,2,2,2).

# Relationships
## Builds Upon
- **Graph**, **vertex degree**

## Enables
- **Chvatal's theorem** — characterizes Hamiltonian degree sequences
- **Hamiltonian sequence** — defined in terms of degree sequences

# Source Reference
Chapter 10, Section 10.2, p. 289 (pdf p. 289).

# Verification Notes
- Definition from p. 289
- Confidence: HIGH — explicitly defined
