---
concept: Graph Isomorphism
slug: graph-isomorphism

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases:
  - "isomorphism"
  - "isomorphic"
  - "automorphism"

prerequisites:
  - graph
  - vertex
  - edge
extends: []
related:
  - graph-property
  - graph-invariant
contrasts_with: []

answers_questions:
  - "When are two graphs isomorphic?"
  - "What is a graph isomorphism?"
  - "What is a graph automorphism?"
---

# Quick Definition
Two graphs G = (V, E) and G' = (V', E') are isomorphic if there exists a bijection from V to V' that preserves adjacency. Such a bijection is an isomorphism; if G = G', it is an automorphism.

# Core Definition
We call G and G' isomorphic, and write G approximately equal to G', if there exists a bijection phi from V to V' with xy in E if and only if phi(x)phi(y) in E' for all x, y in V. Such a map phi is called an isomorphism; if G = G', it is called an automorphism. We do not normally distinguish between isomorphic graphs (Diestel, p. 3).

# Prerequisites
- **Graph**, **vertex**, **edge** — isomorphism relates the structure of two graphs

# Key Properties
1. Isomorphism is an equivalence relation on graphs
2. An isomorphism preserves adjacency and non-adjacency
3. Isomorphic graphs have the same order, size, degree sequence, and all other graph invariants
4. An automorphism is an isomorphism from a graph to itself

# Construction / Recognition
## To Verify an Isomorphism
1. Check that the map is a bijection between vertex sets
2. Verify that for every pair x, y: xy is an edge if and only if phi(x)phi(y) is an edge

# Context & Application
Graph isomorphism is the fundamental equivalence relation in graph theory. We usually do not distinguish between isomorphic graphs, writing G = G' rather than G approximately equal to G'.

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**

## Enables
- **graph-property** — closed under isomorphism
- **graph-invariant** — assigns equal values to isomorphic graphs

# Common Confusions
- **Confusion**: Thinking isomorphic graphs must have the same vertex labels
  **Clarification**: Isomorphism concerns structure only; labels are irrelevant

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
