---
concept: Tutte-Berge Formula
slug: tutte-berge-formula
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 53
section: "2.2 Matching in general graphs"
extraction_confidence: medium
aliases:
  - "Berge formula"
  - "maximum matching size formula"
prerequisites:
  - tuttes-theorem
  - gallai-edmonds-structure
  - maximum-matching
extends:
  - tuttes-theorem
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "What determines the size of a maximum matching?"
---

# Quick Definition
The maximum matching size in a graph G = (V, E) is |S| + (|V| - |S| - |C|)/2, where S is a set from the Gallai-Edmonds decomposition and C is the set of components of G-S.

# Core Definition
From the analysis following Theorem 2.2.3 (p. 53), the maximum matching size is given by |M_0| = |S| + (|V| - |S| - |C|)/2, where S is a set satisfying properties (i) and (ii) of Theorem 2.2.3 and C = C_{G-S}. This is equivalent to the **Tutte-Berge formula**: the maximum matching size equals (1/2)(|V| - max_S(q(G-S) - |S|)).

# Prerequisites
- **Tutte's theorem** — foundational for the formula
- **Gallai-Edmonds structure** — provides the set S
- **Maximum matching** — the formula gives its size

# Key Properties
1. max |M| = |S| + (|V| - |S| - |C|)/2, where C counts components of G-S
2. Equivalently: max |M| = (|V| - d(G))/2, where d(G) = max_S(q(G-S) - |S|) is the deficiency
3. Every maximum matching M has k_S = |S| edges touching S and k_C = (|V| - |S| - |C|)/2 edges within G-S
4. d(G) = 0 iff G has a 1-factor (Tutte's theorem)
5. The number of unmatched vertices is d(G) = max_S(q(G-S) - |S|)

# Construction / Recognition
## Computing Maximum Matching Size
1. Find the Gallai-Edmonds decomposition set S
2. Count components C of G-S
3. Maximum matching size = |S| + (|V| - |S| - |C|)/2

# Context & Application
The Tutte-Berge formula is the non-bipartite generalization of Konig's min-max theorem. It gives an exact formula for the maximum matching size in any graph, expressed as a min-max relation.

# Examples
**Example** (p. 53): Every maximum matching M has exactly |S| edges with at least one end in S, and exactly (|C|-1)/2 edges within each component C of G-S.

# Relationships
## Builds Upon
- **Tutte's theorem**, **Gallai-Edmonds structure**

## Related
- **Konig's theorem** — the bipartite special case

# Common Errors
- **Error**: Using the formula without the correct S
  **Correction**: S must be a set maximizing d(T) = q(G-T) - |T|

# Common Confusions
- **Confusion**: Confusing deficiency d(G) with the matching number
  **Clarification**: d(G) = number of unmatched vertices; matching number = (|V| - d(G))/2

# Source Reference
Chapter 2, Section 2.2, pp. 53-54 (pdf pp. 53-54). Derived from Theorem 2.2.3.

# Verification Notes
- Formula derived from the analysis following Theorem 2.2.3
- Confidence: MEDIUM — the formula is presented implicitly; the name "Tutte-Berge" is standard but not explicitly used in the text
