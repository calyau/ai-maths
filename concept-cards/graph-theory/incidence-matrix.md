---
concept: Incidence Matrix
slug: incidence-matrix

category: algebraic-graph-theory
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 37
section: "1.9 Some linear algebra"

extraction_confidence: high

aliases:
  - "B matrix"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - adjacency-matrix
  - cycle-space
  - cut-space
contrasts_with:
  - adjacency-matrix

answers_questions:
  - "What is the incidence matrix of a graph?"
---

# Quick Definition
The incidence matrix B of a graph G is the n x m matrix over F_2 where b_{ij} = 1 if vertex v_i is an endpoint of edge e_j, and 0 otherwise.

# Core Definition
The incidence matrix B = (b_{ij})_{n x m} of a graph G with V = {v_1, ..., v_n} and E = {e_1, ..., e_m} is defined over F_2 by b_{ij} := 1 if v_i in e_j, 0 otherwise (Diestel, p. 27).

# Prerequisites
- **Graph**, **vertex**, **edge**

# Key Properties
1. The kernel of B is C(G) (Proposition 1.9.7(i))
2. The image of B^t is C*(G) (Proposition 1.9.7(ii))
3. BB^t = A + D where A is the adjacency matrix and D is the degree diagonal matrix (Proposition 1.9.8, over the reals)

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Related
- **cycle-space** — kernel of B
- **cut-space** — image of B^t
- **adjacency-matrix** — related via BB^t = A + D

## Contrasts With
- **adjacency-matrix** — vertex-vertex vs. vertex-edge relationship

# Source Reference
Chapter 1: The Basics, Section 1.9, page 27 (pdf p. 37). Propositions 1.9.7-1.9.8.

# Verification Notes
- Direct from p. 27
- Confidence: HIGH
