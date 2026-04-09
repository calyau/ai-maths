---
concept: "Kuratowski's Theorem"
slug: kuratowski-theorem
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "Theorem 4.4.6"
  - "Kuratowski 1930"
  - "Wagner 1937"
  - "Kuratowski-Wagner theorem"
  - "forbidden minor characterization of planarity"
prerequisites:
  - planar-graph
  - edge-bound-planar
  - topological-minor
extends: []
related:
  - wagner-theorem
  - maclane-theorem
  - whitney-planarity-theorem
contrasts_with: []
answers_questions:
  - "How does planarity relate to forbidden minors (Kuratowski's theorem)?"
  - "How do I test whether a graph is planar?"
  - "What are the Kuratowski graphs?"
---

# Quick Definition
Kuratowski's theorem characterizes planarity by forbidden minors: a graph is planar if and only if it contains neither K^5 nor K_{3,3} as a topological minor (equivalently, as a minor).

# Core Definition
**Theorem 4.4.6** (Kuratowski 1930; Wagner 1937): "The following assertions are equivalent for graphs G: (i) G is planar; (ii) G contains neither K^5 nor K_{3,3} as a minor; (iii) G contains neither K^5 nor K_{3,3} as a topological minor" (Diestel, p. 101).

# Prerequisites
- **Planar graph** -- The property being characterized
- **Edge bound for planar graphs** -- K^5 and K_{3,3} are shown non-planar via edge bounds
- **Topological minor** -- The theorem uses both minor and topological minor concepts

# Key Properties
1. Three equivalent characterizations of planarity
2. Only two forbidden minors needed: K^5 and K_{3,3}
3. K^5 or K_{3,3} minor iff K^5 or K_{3,3} topological minor (Lemma 4.4.2)
4. The 3-connected case (Lemma 4.4.3) is the heart of the proof
5. Edge-maximal graphs without TK^5 or TK_{3,3} are 3-connected (Lemma 4.4.5)

# Construction / Recognition
## To Test Planarity Using Kuratowski's Theorem
1. Search for K^5 or K_{3,3} as a minor in G
2. If found, G is not planar
3. If neither is found, G is planar
4. In practice: use the equivalence with topological minors for explicit certificate

# Context & Application
Kuratowski's theorem is one of the most celebrated results in graph theory. It provides a complete characterization of planarity via a finite list of forbidden substructures. The original version (Kuratowski 1930) was stated for topological minors; the minor version was added by Wagner in 1937. The proof strategy is: (1) prove the 3-connected case by induction using edge contraction, (2) reduce the general case to the 3-connected case.

# Examples
**Example** (p. 92): K^5 has 10 edges on 5 vertices; since 10 > 3(5)-6 = 9, K^5 is non-planar.

**Example** (p. 92): K_{3,3} has 9 edges on 6 vertices; since 9 > 2(6)-4 = 8 (triangle-free bound), K_{3,3} is non-planar.

**Example** (p. 97-98): The Petersen graph contains K_{3,3} as a minor, hence is non-planar.

# Relationships
## Builds Upon
- **Planar graph**, **Edge bound**, **Topological minor**

## Enables
- **MacLane's theorem** -- Proof uses Kuratowski's theorem
- **Planarity testing algorithms** -- Based on forbidden minor search
- **Graph minor theory** -- Kuratowski's theorem is the prototype for forbidden minor characterizations

## Related
- **Wagner's theorem** -- The minor version of Kuratowski's theorem
- **Whitney's planarity theorem** -- Planarity iff abstract dual exists
- **MacLane's theorem** -- Planarity iff cycle space has simple basis

# Common Errors
- **Error**: Thinking only K^5 needs to be excluded
  **Correction**: Both K^5 AND K_{3,3} must be excluded; K_{3,3} is an independent obstruction

- **Error**: Confusing "minor" with "subgraph"
  **Correction**: The theorem uses minors (allowing contraction) or topological minors (allowing subdivision), not just subgraphs

# Common Confusions
- **Confusion**: Thinking Kuratowski's theorem gives an efficient planarity test
  **Clarification**: While theoretically complete, searching for minors is not the most efficient approach; linear-time planarity algorithms use different methods

# Source Reference
Chapter 4, Section 4.4, Theorem 4.4.6, page 101. Proof in Lemmas 4.4.2-4.4.5.

# Verification Notes
- Theorem statement directly quoted from p. 101
- Proof spans Lemmas 4.4.2-4.4.5 (pp. 97-101)
- Confidence: HIGH -- named classical theorem with complete proof
