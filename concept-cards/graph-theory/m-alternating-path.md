---
concept: M-Alternating Path
slug: m-alternating-path
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 44
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "alternating path"
  - "alternating path with respect to M"
prerequisites:
  - matching
  - path
extends:
  - path
related:
  - m-augmenting-path
  - maximum-matching
contrasts_with:
  - m-augmenting-path
answers_questions:
  - "What is an alternating path?"
  - "How do alternating paths relate to matchings?"
---

# Quick Definition
An M-alternating path is a path that starts at an unmatched vertex in A and alternates between edges not in M and edges in M.

# Core Definition
Given a bipartite graph G with bipartition {A, B} and a matching M, a path in G which starts in A at an unmatched vertex and then contains, alternately, edges from E \ M and from M, is an **alternating path** with respect to M (Diestel, p. 44).

# Prerequisites
- **Matching** — alternating paths are defined relative to a matching M
- **Path** — the underlying structure is a path in the graph

# Key Properties
1. Starts at an unmatched vertex in A
2. Edges alternate between non-matching edges (E \ M) and matching edges
3. The first edge is always a non-matching edge (since the start vertex is unmatched)
4. Odd-indexed edges (1st, 3rd, ...) are in E \ M; even-indexed edges (2nd, 4th, ...) are in M
5. An alternating path that ends at an unmatched vertex is an augmenting path

# Construction / Recognition
## To Verify an M-Alternating Path
1. Check the start vertex is unmatched and lies in A
2. Verify the first edge is in E \ M
3. Verify subsequent edges alternate: E \ M, M, E \ M, M, ...
4. Confirm all vertices are distinct (it is a path, not a walk)

# Context & Application
Alternating paths are the key tool for finding maximum matchings. The augmenting path algorithm repeatedly finds alternating paths that end at unmatched vertices and uses them to increase the matching size. The symmetric difference of M with an augmenting path yields a larger matching.

# Examples
**Example** (p. 44, Fig. 2.1.1): The figure shows an alternating path P starting at an unmatched vertex a0 in A, with edges alternating between thin (non-matching) and bold (matching) edges.

# Relationships
## Builds Upon
- **Path** — an alternating path is a path with a special edge-alternation property
- **Matching** — the alternation is defined relative to M

## Enables
- **M-augmenting path** — special case ending at an unmatched vertex
- **Maximum matching** — found by repeatedly augmenting along alternating paths

## Contrasts With
- **M-augmenting path** — an augmenting path is an alternating path with the additional property of ending at an unmatched vertex

# Common Errors
- **Error**: Starting an alternating path at a matched vertex
  **Correction**: By definition, the path starts at an unmatched vertex in A

# Common Confusions
- **Confusion**: Confusing alternating paths with augmenting paths
  **Clarification**: Every augmenting path is alternating, but not every alternating path is augmenting (it must also end at an unmatched vertex)

# Source Reference
Chapter 2, Section 2.1, p. 44 (pdf p. 44).

# Verification Notes
- Definition from p. 44, paragraph 1
- Confidence: HIGH — explicitly defined
