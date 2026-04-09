---
concept: Edge Space
slug: edge-space

category: algebraic-graph-theory
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 33
section: "1.9 Some linear algebra"

extraction_confidence: high

aliases:
  - "E(G) vector space"

prerequisites:
  - graph
  - edge
extends: []
related:
  - vertex-space
  - cycle-space
  - cut-space
contrasts_with:
  - vertex-space

answers_questions:
  - "What is the edge space of a graph?"
---

# Quick Definition
The edge space E(G) is the vector space over F_2 of all functions E -> F_2. Its elements correspond to subsets of E, with addition being symmetric difference.

# Core Definition
The functions E -> F_2 form the edge space E(G) of G: its elements are the subsets of E, vector addition amounts to symmetric difference, the empty set is the zero, and F = -F for all F. The standard basis is {{e_1}, ..., {e_m}}, and dim E(G) = m (Diestel, p. 23).

An inner product is defined: <F, F'> = sum of lambda_i * lambda'_i in F_2, where lambda_i and lambda'_i are the coefficients. <F, F'> = 0 iff F and F' have an even number of edges in common.

# Prerequisites
- **Graph**, **edge** — the edge space is defined from the edge set

# Key Properties
1. Elements are subsets of E
2. Vector addition = symmetric difference
3. Dimension = m (number of edges)
4. <F, F'> = 0 iff even number of common edges
5. For any subspace F: dim F + dim F-perp = m

# Relationships
## Builds Upon
- **graph**, **edge**

## Enables
- **cycle-space**, **cut-space** — subspaces of the edge space

# Source Reference
Chapter 1: The Basics, Section 1.9, page 23 (pdf p. 33).

# Verification Notes
- Direct from p. 23
- Confidence: HIGH
