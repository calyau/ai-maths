---
concept: Tangle
slug: tangle
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 363
section: "Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - tree-width
  - bramble
extends:
  - bramble
related:
  - tree-width-duality-theorem
contrasts_with:
  - bramble
answers_questions:
  - "What is a tangle?"
---

# Quick Definition
A tangle of order k in G is a set T of oriented separations satisfying: (T1) each pair is a separation of order < k; (T2) for every separation of order < k, at least one orientation is in T; (T3) no three "small sides" cover V; (T4) no small side equals V.

# Core Definition
A *tangle of order k* in G = (V, E) is a set T of ordered pairs (A, B) of subsets of V satisfying: (T1) {A, B} is a separation of order < k; (T2) for every separation {A, B} of order < k, at least one of (A,B), (B,A) is in T; (T3) if (A_1,B_1), (A_2,B_2), (A_3,B_3) in T then A_1 union A_2 union A_3 != V; (T4) no (A,B) in T has A = V (Diestel, p. 363, Exercise 36).

# Prerequisites
- **Tree-width** — Tangles arise from large tree-width
- **Bramble** — Tangles are more powerful than brambles

# Key Properties
1. Every graph of tree-width >= 4k has a tangle of order k (Exercise 37)
2. Tangles are the obstructions actually used in the proof of the graph minor theorem
3. More powerful than brambles for structural analysis

# Context & Application
Tangles, not brambles, are the obstructions used in the Robertson-Seymour proof of the graph minor theorem. They capture "high connectivity in a direction" more precisely than brambles.

# Relationships
## Extends
- **Bramble** — Tangles are more refined

# Source Reference
Chapter 12, Exercise 36 on page 363.

# Verification Notes
- Definition from Exercise 36, p. 363
- Confidence: MEDIUM — defined in exercises, not main text
