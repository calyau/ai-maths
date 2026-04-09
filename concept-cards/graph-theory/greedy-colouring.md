---
concept: Greedy Colouring
slug: greedy-colouring
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "greedy algorithm for colouring"
  - "sequential colouring"
prerequisites:
  - vertex-colouring
extends: []
related:
  - colouring-number
  - chromatic-number
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "How does the greedy colouring algorithm work?"
  - "What is the worst case for greedy colouring?"
---

# Quick Definition
The greedy colouring algorithm processes vertices in a fixed order, assigning each vertex the smallest colour not used by its already-coloured neighbours. It uses at most Delta(G) + 1 colours, and with an optimal ordering achieves col(G) colours.

# Core Definition
"Starting from a fixed vertex enumeration v_1, ..., v_n of G, we consider the vertices in turn and colour each v_i with the first available colour -- e.g., with the smallest positive integer not already used to colour any neighbour of v_i among v_1, ..., v_{i-1}" (Diestel, p. 114).

# Prerequisites
- **Vertex colouring** -- The algorithm produces a vertex colouring

# Key Properties
1. Never uses more than Delta(G) + 1 colours (for any ordering)
2. With an optimal ordering, uses at most col(G) colours
3. The optimal ordering picks vertices of minimum degree in the remaining graph, from last to first
4. For complete graphs or odd cycles, Delta + 1 is achieved
5. The algorithm is efficient but not optimal in general

# Construction / Recognition
## Greedy Colouring Algorithm
1. Fix an ordering v_1, ..., v_n of the vertices
2. For i = 1, ..., n:
   - Let S = set of colours used by neighbours of v_i in {v_1, ..., v_{i-1}}
   - Assign v_i the smallest positive integer not in S

## Optimal Ordering Strategy
1. Choose v_n as a vertex of minimum degree delta(G)
2. Choose v_{n-1} as a vertex of minimum degree in G - v_n
3. Continue: v_i has minimum degree in G[{v_1, ..., v_i}]
4. This achieves col(G) colours

# Context & Application
The greedy algorithm is the simplest approach to graph colouring and establishes the fundamental upper bound chi(G) <= Delta(G) + 1. With careful vertex ordering, it achieves the colouring number col(G), which is often much better. The algorithm also extends to list colouring and edge colouring contexts.

# Examples
**Example** (p. 114): For a path v_1-v_2-...-v_n, the greedy algorithm alternates two colours, achieving chi = 2.

**Example** (p. 114): For K^n with any ordering, the greedy algorithm uses n colours (each vertex needs a new colour).

# Relationships
## Enables
- **Colouring number** -- The bound achieved with optimal ordering
- **Brooks' theorem** -- Improvement over greedy bound

# Source Reference
Chapter 5, Section 5.2, page 114.

# Verification Notes
- Algorithm description from p. 114
- Confidence: HIGH -- explicit procedural description
