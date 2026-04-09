---
concept: M-Augmenting Path
slug: m-augmenting-path
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
  - "augmenting path"
prerequisites:
  - m-alternating-path
  - matching
extends:
  - m-alternating-path
related:
  - maximum-matching
  - matched-vertex
  - unmatched-vertex
contrasts_with:
  - m-alternating-path
answers_questions:
  - "What is an augmenting path?"
  - "How can a matching be enlarged?"
---

# Quick Definition
An M-augmenting path is an M-alternating path that ends at an unmatched vertex. Its symmetric difference with M produces a matching with one more edge.

# Core Definition
An alternating path P that ends in an unmatched vertex of B is called an **augmenting path** (with respect to M), because we can use it to turn M into a larger matching: the symmetric difference of E(P) with M is again a matching, and the set of matched vertices is increased by two (the ends of P) (Diestel, p. 44).

# Prerequisites
- **M-alternating path** — an augmenting path is a special case of an alternating path
- **Matching** — augmentation modifies the matching M

# Key Properties
1. Starts at an unmatched vertex in A and ends at an unmatched vertex in B
2. Edges alternate between E \ M and M
3. Has one more non-matching edge than matching edge (odd total length)
4. The symmetric difference M' = M triangle E(P) is a matching with |M'| = |M| + 1
5. A matching M is maximum if and only if no M-augmenting path exists (Exercise 1, p. 51)

# Construction / Recognition
## To Augment a Matching
1. Find an M-augmenting path P
2. Compute M' = M symmetric-difference E(P)
3. Edges of P that were in M are removed; edges of P not in M are added
4. The result M' is a matching with |M'| = |M| + 1

## To Recognize an Augmenting Path
1. Verify it is an alternating path (starts at unmatched vertex, alternates edges)
2. Check that the terminal vertex is also unmatched by M

# Context & Application
Augmenting paths are the engine of matching algorithms. The foundational result (Exercise 1) states that a matching is maximum if and only if no augmenting path exists. This reduces the maximum matching problem to the problem of finding augmenting paths, which is algorithmically tractable.

# Examples
**Example** (p. 44, Fig. 2.1.1): The augmenting path P starts at an unmatched vertex in A and ends at an unmatched vertex in B. Bold edges are in M; the symmetric difference replaces matching edges on P with non-matching edges, gaining two newly matched vertices.

# Relationships
## Builds Upon
- **M-alternating path** — an augmenting path is an alternating path ending at an unmatched vertex

## Enables
- **Maximum matching** — found by repeatedly augmenting until no augmenting path exists
- **Konig's theorem** — proof uses augmenting paths

## Related
- **Hall's marriage theorem** — first proof constructs augmenting paths

## Contrasts With
- **M-alternating path** — not every alternating path is augmenting

# Common Errors
- **Error**: Augmenting along a path that does not end at an unmatched vertex
  **Correction**: Both endpoints must be unmatched for the symmetric difference to yield a valid larger matching

# Common Confusions
- **Confusion**: Thinking augmentation adds the entire path to M
  **Clarification**: Augmentation takes the symmetric difference: edges of P in M are removed, edges of P not in M are added

# Source Reference
Chapter 2, Section 2.1, p. 44 (pdf p. 44). See Fig. 2.1.1.

# Verification Notes
- Definition from p. 44, paragraph 1
- Property 5 (optimality characterization) from Exercise 1, p. 51
- Confidence: HIGH — explicitly defined with illustration
