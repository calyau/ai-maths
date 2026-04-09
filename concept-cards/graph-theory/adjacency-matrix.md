---
concept: Adjacency Matrix
slug: adjacency-matrix

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
  - "A matrix"

prerequisites:
  - graph
  - vertex
  - adjacent
extends: []
related:
  - incidence-matrix
contrasts_with:
  - incidence-matrix

answers_questions:
  - "What is the adjacency matrix of a graph?"
---

# Quick Definition
The adjacency matrix A of a graph G is the n x n matrix where a_{ij} = 1 if v_i and v_j are adjacent, and 0 otherwise.

# Core Definition
The adjacency matrix A = (a_{ij})_{n x n} of G is defined by a_{ij} := 1 if v_iv_j in E, 0 otherwise (Diestel, p. 28).

Proposition 1.9.8: BB^t = A + D, where B is the incidence matrix and D is the diagonal matrix of degrees (over the reals).

# Prerequisites
- **Graph**, **vertex**, **adjacent**

# Key Properties
1. A is symmetric (since the graph is undirected)
2. A has zeros on the diagonal (no loops)
3. The entry (A^k)_{ij} counts the number of walks of length k from v_i to v_j (Exercise 34)
4. BB^t = A + D (Proposition 1.9.8)

# Relationships
## Builds Upon
- **graph**, **adjacent**

## Related
- **incidence-matrix** — related via BB^t = A + D

# Source Reference
Chapter 1: The Basics, Section 1.9, page 28 (pdf p. 38). Proposition 1.9.8.

# Verification Notes
- Direct from p. 28
- Confidence: HIGH
